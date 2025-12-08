
import gradio as gr

def mergesort(a, steps, depth = 0, parent_split_line=None, which = None):
    """Takes an unsorted list and sorts it using merge sort while recording steps."""
    indent = "   " * depth
    steps.append(f"{indent}Merge sort initiated on {a}")
    

    if len(a) <= 1:
        steps.append(f"{indent}Reached length of 1 or 0 ({a}); list is already sorted; returning unchanged list")
        if parent_split_line is not None :
            steps.append(f"{indent}Finished sorting {which} half {a}; created at line {parent_split_line +1}") #referencing which line it came from 
        return a# already sorted array

    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]  # split into two halves
    split_index = len(steps)
    steps.append(f"{indent}Dividing into two halves\n {indent} Left half: {left}\n {indent} Right half: {right}")

    # recursive sorting part:
    steps.append(f"{indent} Sorting the left half: {left}")
    left_sort = mergesort(left, steps, depth +1, parent_split_line = split_index, which = "left")

    steps.append(f"{indent}Sorting the right half: {right}")
    right_sort = mergesort(right, steps, depth +1, parent_split_line = split_index, which = "right")

    merged = merge(left_sort, right_sort, steps, depth)
    steps.append(f"{indent} Merge complete for {a}; sorted = {merged}")

    if parent_split_line is not None:
        steps.append(f"{indent} Finished sorting {which} half {a}; created at line {parent_split_line +1}")

    return merged # call other function to return merged list

def merge(left, right, steps, depth):
    indent = "    " * depth
    steps.append(f"{indent}Initiating the merge between the sorted left: {left} and right: {right} arrays")
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        # compare elements and append the smaller
        if left[i] < right[j]:
            result.append(left[i])
            steps.append(f"{indent}Comparing {left[i]} (left) and {right[j]} (right) -> {left[i]} (left) is smaller; adding to result: {result}")
            i += 1
        else:
            result.append(right[j])
            steps.append(f"{indent}Comparing {right[j]} (right) and {left[i]} (left) -> {right[j]} (right) is smaller; adding to result: {result}")
            j += 1

    while i < len(left):
        result.append(left[i])
        steps.append(f"{indent}Right list is empty; adding leftover element {left[i]} from left list to result {result}")
        i += 1

    while j < len(right):
        result.append(right[j])
        steps.append(f"{indent}Left list is empty; adding leftover element {right[j]} from right list to result {result}")
        j += 1

    steps.append(f"{indent} Merging complete. Final merged list: {result}")
    return result



import gradio as gr

def run_collect(a):
    steps =[]
    sorted_list = mergesort(a.copy(),steps)
    return sorted_list, steps

def format_line_numbers(steps):
    return [f"{i +1}: {s}" for i,s in enumerate(steps)]
    
def split_steps(input_text):
    """Return only the splitting-related steps (with line numbers) for the given input_text."""
    if not input_text or not input_text.strip():
        return "Error: input is empty. Enter integers separated by spaces or commas."

    parts = input_text.replace(",", " ").split()
    try:
        arr = [int(x) for x in parts]
    except ValueError:
        return "Error: input must be integers separated by commas or spaces."
    steps = run_collect(a)
    numbered = format_line_numbers(steps)
    
    split_keywords = ["Dividing", "Sorting the left half", "Sorting the right half", "Merge sort initiated", "Finished sorting"]
    split_log = [line for line in numbered if any(k in line for k in split_keywords)]
    return "\n".join(split_log)

def merging_steps(input_text):
    """Return only the merging-related steps (with line numbers) for the given input_text."""
    if not input_text or not input_text.strip():
        return "Error: input is empty. Enter integers separated by spaces or commas."

    parts = input_text.replace(",", " ").split()
    try:
        arr = [int(x) for x in parts]
    except ValueError:
        return "Error: input must be integers separated by commas or spaces."
    steps = run_collect(a)
    numbered = format_line_numbers(steps)

    # keywords that indicate merging operations
    merge_keywords = ["Initiating merge", "Comparing", "Adding leftover", "Merging complete", "Merge complete"]
    merge_log = [line for line in numbered if any(k in line for k in merge_keywords)]
    return "\n".join(merge_log)

def gradio_merge_sort(input_text):
    """Gradio wrapper: parses input_text into integers and runs mergesort with steps returned."""
    if not input_text or not input_text.strip():
        return "", "Error: input is empty. Enter integers separated by spaces or commas."

    # accept commas or spaces as separators
    parts = input_text.replace(",", " ").split()
    try:
        arr = [int(x) for x in parts]
    except ValueError:
        return "", "Error: input must be integers separated by commas or spaces."

    sorted_a, steps = run_collect(a)
    numbered = format_line_numbers(steps)


    for s in steps:
        if ("Dividing" in s or "Initiated" in s or "Left half" in s or "Right half" in s or "Sorting left half" in s or "Sorting right half" in s):
            splitting.append(s)

        elif ("Merge" in s or "Comparing" in s or "Adding to result" in s or "Left list empty" in s or "Right list empty" in s or "Merging finished" in s):
            merging.append(s)
    return " ".join(map(str, sorted_a)), "\n".join(splitting), "\n".join(merging)


iface = gr.Interface(
    fn=gradio_merge_sort,
    inputs=gr.Textbox(label="Enter numbers seperated by commas or spaces. (e.g. 7 3 2 1 or 7,3,2,1)", lines=1),
    outputs=[
        gr.Textbox(label="Sorted Output", lines=1),
        gr.Textbox(label="Splitting steps", lines = 20),
        gr.Textbox(label="Merging Steps", lines=20),
    ],
    title="Merge Sort App",
    description="Enter a list of numbers to be sorted along with steps.",
)

if __name__ == "__main__":
    # When run directly, launch the UI. When imported (for tests), do not auto-launch.
    iface.launch()
