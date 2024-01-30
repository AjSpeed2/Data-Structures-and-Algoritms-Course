import random
def mergeSort(list):
  """
  Sorts given list in ascending order.
  Returns a new sorted list.

  Divide: Find the midpoint of the list and divide inot sublists.
  Conquer: Recursively sort the sublists created in previous step.
  Combine: Merge the sorted sublists created in previous step.

  Takes O(n log n) time.
  
  """

  if len(list) <= 1:
    return list
  

  leftHalf, rightHalf = split(list)
  left = mergeSort(leftHalf)
  right = mergeSort(rightHalf)
   
  return merge(left, right)

def split(list):
  """
  Divide the unsorted list at midpoint into sublists.
  Returns two sublists - left and right.
  Takes overall O(n) time.
  """
  mid = len(list) // 2
  left = list[:mid]
  right = list[mid:]

  return left, right

def merge(left, right):
  """
  Merges two lists (arrays), sorting them in the process.
  Returns a new merged list.
  Runs in overall O(log n) time.
  """

  l = []
  i = 0
  j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      l.append(left[i])
      i += 1
    else:
      l.append(right[j])
      j += 1

  while i < len(left):
    l.append(left[i])
    i += 1

  while j < len(right):
    l.append(right[j])
    j += 1

  return l

def verifySorted(list):
  n = len(list)

  if n <= 1:
    return True
  
  return list[0] <= list[1] and verifySorted(list[1:])

numbers = [random.randint(0, 10000000) for x in range(10000000)]
print(mergeSort(numbers))