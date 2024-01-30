import random

numbers = [random.randint(0, 1000000) for x in range(1000000)]

def quicksort(values):
  if len(values) <= 1:
    return values
  less = []
  greater = []
  pivot = values[0]
  for value in values[1:]:
    if value <= pivot:
      less.append(value)
    else:
      greater.append(value)
  return quicksort(less) + [pivot] + quicksort(greater)
  
sortedNumbers = quicksort(numbers)
print(sortedNumbers)