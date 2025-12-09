# Final-Project-CISC121
Algorithm Name:
Merge Sort

Test Demos:
Negative values:
<img width="1715" height="994" alt="Screenshot 2025-12-09 at 12 45 23 PM" src="https://github.com/user-attachments/assets/1a0b58a1-0046-4d38-80fb-7b04408988c4" />
<img width="920" height="573" alt="Screenshot 2025-12-09 at 12 45 34 PM" src="https://github.com/user-attachments/assets/702a55b1-c023-4b38-adc4-9c7dc5e4522b" />

Strings input:
<img width="1661" height="689" alt="Screenshot 2025-12-09 at 12 45 55 PM" src="https://github.com/user-attachments/assets/7271aefc-0eff-4a81-8915-053788ff5416" />

Long list: descending
<img width="1669" height="1007" alt="Screenshot 2025-12-09 at 12 47 19 PM" src="https://github.com/user-attachments/assets/2f720b18-084a-46c2-b85f-cc0ed403d035" />
<img width="928" height="551" alt="Screenshot 2025-12-09 at 12 47 29 PM" src="https://github.com/user-attachments/assets/1b540058-3869-48ee-a357-8f1c5c8e3a4c" />

Empty Input:
<img width="1715" height="617" alt="Screenshot 2025-12-09 at 12 50 59 PM" src="https://github.com/user-attachments/assets/1effa18e-f1f3-4873-a791-fb11877a95d7" />


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

Steps to run:
Paste hugging face link into browser
wait to load
insert list of numbers (no strings or floats)

Hugging Face Link:
