def mergesort(a):
  """ Takes unsorted list and sorts using merge sort and merge"""
  if len(a) < = 1:
    return a #already sorted array

  mid = len(a) //2
  left = a[:mid] 
  right = a[mid:] #split into two halves

  #recursive sorting part:
  left_sort = mergesort(left)
  right_sort = mergesort(right)

  return merge(left_sort,right_sort) #call other function to return merged list

def merge(left,right):
  result = [] #initialize list
  i = j = 0 #set equal to 0

  while i < len(left) and j < len(right): #compare elements and append the smaller
    if left[i] < right[j]:
      result.append(left[i])
      i +=1 #increment i by 1
    else:
      result.append(right[j])
      j +=1 #increment j by one

  result.extend(left[i:]) #appends leftover elements
  result.extend(right[j:]) #ai disclaimer needed help with this part didn't know how to append the leftover elements


