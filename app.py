def mergesort(a,steps):
  """ Takes unsorted list and sorts using merge sort and merge"""
  steps.append("Merge sort initiated on {a}")
  
  if len(a) < = 1:
    steps.append("Reached length of 1 or 0 ({a}); list is already sorted; returning unchanged list")
    return a #already sorted array

  mid = len(a) //2
  left = a[:mid] 
  right = a[mid:]#split into two halves
  steps.append("Dividing into two halfs \n Left half: {left}\n Right half:{right}")

  #recursive sorting part:
  left_sort = mergesort(left,steps)
  right_sort = mergesort(right,steps)

  return merge(left_sort,right_sort,steps) #call other function to return merged list

def merge(left,right, steps):
  steps.append{"Merging the sorted {left} and {right} arrays")
  result = [] #initialize list
  i = j = 0 #set equal to 0

  while i < len(left) and j < len(right): #compare elements and append the smaller
    if left[i] < right[j]:
      result.append(left[i])
      steps.append("")
      i +=1 #increment i by 1
    else:
      result.append(right[j])
      steps.append("")
      j +=1 #increment j by one



def merge_sort_steps_display(


