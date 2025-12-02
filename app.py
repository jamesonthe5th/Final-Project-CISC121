#!/usr/bin/env python3
from typing import List, Tuple

import gradio as gr

def mergesort(a, steps):
    """Takes an unsorted list and sorts it using merge sort while recording steps."""
    steps.append(f"Merge sort initiated on {a}")

    if len(a) <= 1:
        steps.append(f"Reached length of 1 or 0 ({a}); list is already sorted; returning unchanged list")
        return a
        print (a)# already sorted array

    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]  # split into two halves
    steps.append(f"Dividing into two halves\n Left half: {left}\n Right half: {right}")

    # recursive sorting part:
    steps.append(f"Sorting the left half: {left}")
    left_sort = mergesort(left, steps)

    steps.append(f"Sorting the right half: {right}")
    right_sort = mergesort(right, steps)

    return merge(left_sort, right_sort, steps)  # call other function to return merged list

def merge(left, right, steps):
    steps.append(f"Initiating the merge between the sorted left: {left} and right: {right} arrays")
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        # compare elements and append the smaller
        if left[i] < right[j]:
            result.append(left[i])
            steps.append(f"Comparing {left[i]} (left) and {right[j]} (right) -> {left[i]} is smaller; adding to result: {result}")
            i += 1
        else:
            result.append(right[j])
            steps.append(f"Comparing {right[j]} (right) and {left[i]} (left) -> {right[j]} is smaller; adding to result: {result}")
            j += 1

    while i < len(left):
        result.append(left[i])
        steps.append(f"Right list is empty; adding leftover element {left[i]} from left list to result {result}")
        i += 1

    while j < len(right):
        result.append(right[j])
        steps.append(f"Left list is empty; adding leftover element {right[j]} from right list to result {result}")
        j += 1

    steps.append(f"Merging complete. Final merged list: {result}")
    return result



import gradio as gr

def gradio_merge_sort(input_text: str):
    """Gradio wrapper: parses input_text into integers and runs mergesort with steps returned."""
    if not input_text or not input_text.strip():
        return "", "Error: input is empty. Enter integers separated by spaces or commas."

    # accept commas or spaces as separators
    parts = input_text.replace(",", " ").split()
    try:
        arr = [int(x) for x in parts]
    except ValueError:
        return "", "Error: input must be integers separated by commas or spaces."

    steps: List[str] = []
    sorted_a = mergesort(arr, steps)
    return " ".join(map(str, sorted_a)), "\n".join(steps)


iface = gr.Interface(
    fn=gradio_merge_sort,
    inputs=gr.Textbox(label="Enter numbers seperated by commas or spaces. (e.g. 5 2 8 1)", lines=1),
    outputs=[
        gr.Textbox(label="Sorted Output", lines=1),
        gr.Textbox(label="Merge Sort Steps", lines=20),
    ],
    title="Merge Sort App",
    description="Enter a list of numbers to see the magic take place (merge sorting).",
)

if __name__ == "__main__":
    # When run directly, launch the UI. When imported (for tests), do not auto-launch.
    iface.launch()
