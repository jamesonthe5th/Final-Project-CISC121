# Final-Project-CISC121
Algorithm selected:
I chose to use merge sort for my algorithm of choice because first it is quite good at dealing with larger input sizes as it has a time complexity of O(nlogn).
- It also demonstrates a divide and conquer algorithm which I understand more than other algorithms. 
- It is also easy to test edge cases.

Decomposition of the merge sort:
Start with getting input values from user interface
Store the initial input
Recursively split the arrays in half until length 1 or 0. (the dividing part)
Begin the merge step comparing two halves of original array with index values i and j whichever is lesser is appended to the sorted full array
Continue until no more merges are made then either append leftover elements and return or return.

Pattern recognition of the merge sort:
the pattern is quite simple first it begins with split, split, split until length 1 or 0 base case, then it switches to merge merge merge until fully merged. 
comparision pattern also made comparion list1[0] with list2[0] to find lesser. 

Abstraction of merge sort:
What were going to hide:
pointer index manipulation
temporary lists uses
recursive function call stack

What were going to show:
current lists or sublists
each split step
each merge
comparisions
newly formed list after each merge
final sorted list

Algorithm design for merge sort:
Input:
a list of values of integer type seperated by spaces or commas.
Output:
Gradio will output a final sorted value in ascending order, the merge sort steps and the merging steps along with a visual representation of the actual code and line numbers for easy referencing from where values came from. 
Flow chart:
[User enters list through GUI]
[Call Merge_sort algorithm with snapshots]
[Base case len(list0) == 1 or 0]
yes [return list] (document in steps)
no [split into left and right] (document in steps)
[continue splitting until base case reached] (documented in steps)
[Call merging algorithm] (documented in steps)
[Compare values using pointers] (documented in steps)
[The smaller value of left[i] or right[j] will be appeneded to the resulting list] (documented)
[Once one side (left or right) is empty, algorithm will append all leftover elements] (documented)
[return result](documented)
