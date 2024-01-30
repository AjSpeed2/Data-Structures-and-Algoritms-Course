import random

numbers = [random.randint(0, 1000) for x in range(1000)]

def selectionSort(values):
  sortedList=[]
  for i in range(0, len(values)):
    indexToMove = indexOfMin(values)
    sortedList.append(values.pop(indexToMove))
  return sortedList

def indexOfMin(values):
  minIndex = 0
  for i in range(1, len(values)):
    if values[i] < values[minIndex]:
      minIndex = i
  return minIndex

print(selectionSort(numbers))