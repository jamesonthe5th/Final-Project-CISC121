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
  steps.append("Recursively sorting the left half: {left}")
  left_sort = mergesort(left,steps)
  
  steps.append("Recursively sorting the right half: {right}")
  right_sort = mergesort(right,steps)

  return merge(left_sort,right_sort,steps) #call other function to return merged list

def merge(left,right, steps):
  steps.append{"Inititating the merge between the sorted left: {left} and right: {right} arrays")
  result = [] #initialize list
  i = j = 0 #set equal to 0

  while i < len(left) and j < len(right): #compare elements and append the smaller
    if left[i] < right[j]:
      result.append(left[i])
      steps.append("Comparing {left[i]} left and {right[j]} right\n {left[i]} is smaller than; adding to result: {result}")
      i +=1 #increment i by 1
    else:
      result.append(right[j])
      steps.append("Comparing {right[j]} right and {left[i]} left\n {right[j]} is smaller than; adding to the result: {result}")
      j +=1 #increment j by one


  while i < len(left):
    result.append(left[i])
    steps.append("Right list is empty\n Adding leftover element {left[i]} from left list to result {result}")
    i +=1

  while j < len(right):
    result.append(right[j])
    steps.append("Left list is empty \n Adding leftover element {right[i]} from right list to result {result}")
    j+=1


  steps.append("Merging complete. Final merged list: {result}")





