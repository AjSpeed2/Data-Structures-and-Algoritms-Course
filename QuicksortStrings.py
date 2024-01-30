names = ["mary conner"]

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
  
sortedNames = quicksort(names)
print(sortedNames)