
import gradio as gr
import matplotlib.pyplot as plt

# ----------------------------------------------------
# MERGE SORT WITH STEP LOGGING
# ----------------------------------------------------

def mergesort(a, steps, depth=0, parent_split_line=None, which=None):
    indent = "    " * depth
    steps.append(f"{indent}Merge sort initiated on {a}")

    if len(a) <= 1:
        steps.append(f"{indent}Reached length of 1 or 0 ({a}); list is already sorted; returning unchanged list")
        return a

    # Split
    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]
    split_index = len(steps)

    steps.append(
        f"{indent}Dividing into two halves\n"
        f"{indent} Left half: {left}\n"
        f"{indent} Right half: {right}"
    )

    # Sort Left
    steps.append(f"{indent}Sorting the left half: {left}")
    left_sort = mergesort(left, steps, depth + 1, parent_split_line=split_index, which="left")

    # Sort Right
    steps.append(f"{indent}Sorting the right half: {right}")
    right_sort = mergesort(right, steps, depth + 1, parent_split_line=split_index, which="right")

    # Merge
    merged = merge(left_sort, right_sort, steps, depth)
    steps.append(f"{indent}Merge complete for {a}; sorted = {merged}")

    if parent_split_line is not None and len(a) > 1:
        steps.append(f"{indent}Finished sorting {which} half {a}; created at line {parent_split_line + 1}")

    return merged


def merge(left, right, steps, depth):
    indent = "    " * depth
    steps.append(f"{indent}Initiating the merge between the sorted left: {left} and right: {right} arrays")

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            steps.append(f"{indent}Comparing {left[i]} (left) and {right[j]} (right) → {left[i]} added")
            i += 1
        else:
            result.append(right[j])
            steps.append(f"{indent}Comparing {right[j]} (right) and {left[i]} (left) → {right[j]} added")
            j += 1

    while i < len(left):
        result.append(left[i])
        steps.append(f"{indent}Right list empty → adding leftover {left[i]} from left")
        i += 1

    while j < len(right):
        result.append(right[j])
        steps.append(f"{indent}Left list empty → adding leftover {right[j]} from right")
        j += 1

    steps.append(f"{indent}Merging complete. Final merged list: {result}")
    return result


# ----------------------------------------------------
# MERGE SORT DRIVER
# ----------------------------------------------------

def run_collect(a):
    steps = []
    sorted_list = mergesort(a.copy(), steps)
    return sorted_list, steps


def format_line_numbers(steps):
    return [f"{i + 1}: {s}" for i, s in enumerate(steps)]


# ----------------------------------------------------
# TREE BUILDING FOR IMAGE
# ----------------------------------------------------

def build_tree(a):
    # base case
    if len(a) <= 1:
        return (str(a), None, None)

    mid = len(a) // 2

    # get sorted version for this sublist (uses your run_collect which runs mergesort)
    sorted_a, _ = run_collect(a)

    # also get the sorted halves so children reflect the sorted order
    # note: run_collect(left) returns (sorted_left, steps), so we take sorted_left
    left_sorted, _ = run_collect(a[:mid])
    right_sorted, _ = run_collect(a[mid:])

    # build children from the *sorted halves* so leaf positions match merge order
    left_node = build_tree(left_sorted)
    right_node = build_tree(right_sorted)

    # label this node with the fully sorted sublist
    return (str(sorted_a), left_node, right_node)

def collect_nodes(node, nodes=None):
    if nodes is None:
        nodes = []
    if node is None:
        return nodes

    nodes.append(node)
    _, left, right = node
    collect_nodes(left, nodes)
    collect_nodes(right, nodes)

    return nodes


def assign_positions(node, x=0.5, y=1.0, layer=0, coords=None):
    if coords is None:
        coords = {}

    coords[node] = (x, y)
    spacing = 0.15 / (layer + 1)
    value, left, right = node

    if left:
        assign_positions(left, x - spacing, y - 0.13, layer + 1, coords)
    if right:
        assign_positions(right, x + spacing, y - 0.13, layer + 1, coords)

    return coords


def plot_tree(node, filename="recursion_tree.png"):
    coords = assign_positions(node)
    nodes = collect_nodes(node)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis("off")

    # Draw edges
    for n in nodes:
        value, left, right = n
        x, y = coords[n]

        if left:
            x2, y2 = coords[left]
            ax.plot([x, x2], [y, y2])

        if right:
            x2, y2 = coords[right]
            ax.plot([x, x2], [y, y2])

    # Draw nodes
    for n in nodes:
        value, left, right = n
        x, y = coords[n]

        ax.text(
            x, y, value,
            ha="center", va="center",
            bbox=dict(boxstyle="round", facecolor="white"),
            fontsize=9
        )

    fig.savefig(filename, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return filename


# ----------------------------------------------------
# GRADIO WRAPPER
# ----------------------------------------------------

def gradio_merge_sort(input_text):
    if not input_text or not input_text.strip():
        return "", "Error: Input empty.", "Error: Input empty.", None

    parts = input_text.replace(",", " ").split()

    try:
        a = [int(x) for x in parts]
    except ValueError:
        return "", "Error: input must be integers.", "Error: input must be integers.", None

    sorted_a, steps = run_collect(a)
    numbered = format_line_numbers(steps)

    # Split logs
    split_keywords = [
        "Merge sort initiated",
        "Dividing",
        "Sorting the left half",
        "Sorting the right half",
        "Finished sorting"
    ]

    splitting = [s for s in numbered if any(k in s for k in split_keywords)]

    # Merge logs
    merge_keywords = [
        "Initiating the merge",
        "Comparing",
        "leftover",
        "Merging complete",
        "Merge complete"
    ]

    merging = [s for s in numbered if any(k in s for k in merge_keywords)]

    # Generate image
    tree = build_tree(a)
    img_path = "recursion_tree.png"
    plot_tree(tree, filename=img_path)

    return (
        " ".join(map(str, sorted_a)),
        "\n".join(splitting),
        "\n".join(merging),
        img_path
    )


# ----------------------------------------------------
# GRADIO INTERFACE
# ----------------------------------------------------

iface = gr.Interface(
    fn=gradio_merge_sort,
    inputs=gr.Textbox(label="Enter numbers separated by commas or spaces", lines=1),
    outputs=[
        gr.Textbox(label="Sorted Output", lines=1),
        gr.Textbox(label="Splitting Steps", lines=20),
        gr.Textbox(label="Merging Steps", lines=20),
        gr.Image(type="filepath", label="Merge Sort Visual")
    ],
    title="Merge Sort App",
    description="Enter a list of numbers to visualize merge sort splitting, merging, and recursion tree."
)

if __name__ == "__main__":
    iface.launch()
