import gradio as gr
import matplotlib.pyplot as plt

#Merge sort with added steps

def mergesort(a, steps, depth=0, parent_split_line=None, which=None):
    """This algorithm takes in an array, our steps strings, depth for the indentation,
    a parent line so that we can take the parent split and get to its children,and which, this means either left or right"""
    indent = "    " * depth #recursive indentation
    steps.append(f"{indent}Merge sort initiated on {a}") #steps

    if len(a) <= 1:
        steps.append(f"{indent}Reached length of 1 or 0 ({a}); list is already sorted; returning unchanged list") #steps
        return a

    # Split
    mid = len(a) // 2 
    left = a[:mid]
    right = a[mid:]
    split_index = len(steps)

    steps.append(f"{indent}Dividing into two halves\n"f"{indent} Left half: {left}\n"f"{indent} Right half: {right}") #documenting steps

    # Sort Left
    steps.append(f"{indent}Sorting the left half: {left}")
    left_sort = mergesort(left, steps, depth + 1, parent_split_line=split_index, which="left") #sort the left half, increment depth,
    #set parent split to the index and which split, indicate which side

    # Sort Right
    steps.append(f"{indent}Sorting the right half: {right}")
    right_sort = mergesort(right, steps, depth + 1, parent_split_line=split_index, which="right") #same as above but which is right

    # Merge
    merged = merge(left_sort, right_sort, steps, depth)
    steps.append(f"{indent}Merge complete for {a}; sorted = {merged}") #steps

    if parent_split_line is not None and len(a) > 1: #if our parent isnt none and is greater than 1
        steps.append(f"{indent}Finished sorting {which} half {a}; created at line {parent_split_line + 1}") #steps

    return merged #merged


def merge(left, right, steps, depth): 
    """Algorithm takes in left and right lists, the steps and recursion depth"""
    indent = "    " * depth #recursion depth indent
    steps.append(f"{indent}Initiating the merge between the sorted left: {left} and right: {right} arrays") #steps

    result = []
    i = j = 0

    while i < len(left) and j < len(right): #index is not at the end
        if left[i] < right[j]: #compare left for smaller 
            result.append(left[i]) #yes then append
            steps.append(f"{indent}Comparing {left[i]} (left) and {right[j]} (right) = {left[i]} added") #document steps
            i += 1 #increment left by one
        else: #no then
            result.append(right[j]) #right is smaller append
            steps.append(f"{indent}Comparing {right[j]} (right) and {left[i]} (left) = {right[j]} added") #document steps
            j += 1 #increment right by 1

    while i < len(left): #append leftover left side elements
        result.append(left[i]) 
        steps.append(f"{indent}Right list empty → adding leftover {left[i]} from left")
        i += 1

    while j < len(right): #append leftover right side elements
        result.append(right[j])
        steps.append(f"{indent}Left list empty → adding leftover {right[j]} from right")
        j += 1

    steps.append(f"{indent}Merging complete. Final merged list: {result}") #document
    return result #return final result




def run_collect(a):
    """This small function collects all the steps and the sorted list, taking in the array"""
    steps = []
    sorted_list = mergesort(a.copy(), steps)
    return sorted_list, steps


def format_line_numbers(steps):
    """This function adds line numbers to each step, taking in steps"""
    return [f"{i + 1}: {s}" for i, s in enumerate(steps)]




def build_tree(a):
    """This function builds the recursion tree for the visual representation taking in the array"""
    
    # base case
    if len(a) <= 1:#check base case
        return (str(a), None, None)

    mid = len(a) // 2

    #get sorted version of run collect
    sorted_a, _ = run_collect(a)

    #get the children of parent run collect left and right halfs
    left_sorted, _ = run_collect(a[:mid])
    right_sorted, _ = run_collect(a[mid:])

     #build the nodes eg children from the left sorted and right sorted
    left_node = build_tree(left_sorted)
    right_node = build_tree(right_sorted)

    # label this node with the fully sorted sublist
    return (str(sorted_a), left_node, right_node)#return them

def collect_nodes(node, nodes=None):
    """This function collects the nodes for the visual into a list"""
    if nodes is None: #check empty
        nodes = []
    if node is None: #if no more nodes
        return nodes

    nodes.append(node) 
    _, left, right = node
    collect_nodes(left, nodes)
    collect_nodes(right, nodes)

    return nodes


def assign_positions(node, x=0.5, y=1.0, layer=0, coords=None):
    """This part is where the matplot lib comes in to play and the AI disclaimer: I will be honest I did not know what to do here especially for assigning the spacing and the x y values
    However this function takes the individual nodes, gives it an x and y value and a layer and then exact coordinates will be established"""
    if coords is None: #check its empty
        coords = {}

    coords[node] = (x, y) #set coordinate
    spacing = 0.15 / (layer + 1) #set spacing
    value, left, right = node #set value of node

    if left:
        assign_positions(left, x - spacing, y - 0.13, layer + 1, coords) #put it in place
    if right:
        assign_positions(right, x + spacing, y - 0.13, layer + 1, coords) #put in place

    return coords


def plot_tree(node, filename="recursion_tree.png"):
    """This function is what actually builds the image, this had a lot of help from AI, 
    However it takes in individual nodes and the image name, and will output a plot of all values inputted following a merge sort visual"""
    coords = assign_positions(node) #coordinates
    nodes = collect_nodes(node) #all nodes

    fig, ax = plt.subplots(figsize=(10, 6)) #build the figure size
    ax.axis("off") #turn of the axis

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


#Gradio UI input

def gradio_merge_sort(input_text):
    """This algorithm takes in the input text from the app and breaks it down so that the algorithm can run using the values"""
    if not input_text or not input_text.strip(): #if its empty
        return "", "Error: Input empty.", "Error: Input empty.", None

    parts = input_text.replace(",", " ").split() #split the commas and spaces

    try:
        a = [int(x) for x in parts] #try to check if integer
    except ValueError:
        return "", "Error: input must be integers.", "Error: input must be integers.", None

    sorted_a, steps = run_collect(a) #collect the sorted and steps for a
    numbered = format_line_numbers(steps) #get line numbers

    # initiate keywords used in splitting steps
    split_keywords = ["Merge sort initiated","Dividing","Sorting the left half","Sorting the right half","Finished sorting"]

    splitting = [s for s in numbered if any(k in s for k in split_keywords)] #split steps

    # intiate keywords used in merging steps
    merge_keywords = ["Initiating the merge","Comparing","leftover","Merging complete","Merge complete"]

    merging = [s for s in numbered if any(k in s for k in merge_keywords)]#merge steps

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


#Actual gradio output interface

iface = gr.Interface(
    fn=gradio_merge_sort,
    inputs=gr.Textbox(label="Enter numbers separated by commas or spaces", lines=1), #input box
    outputs=[
        gr.Textbox(label="Sorted Output", lines=1), #this is the first output
        gr.Textbox(label="Splitting Steps", lines=20), #split steps
        gr.Textbox(label="Merging Steps", lines=20),#merge steps
        gr.Image(type="filepath", label="Merge Sort Visual") #visual
    ],
    title="Merge Sort App", #title
    description="Enter a list of numbers to visualize merge sort splitting, merging, and recursion tree." #description
)

if __name__ == "__main__":
    iface.launch()
