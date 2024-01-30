import random, sys

numbers = [random.randint(0, 10000) for x in range(10)]

print(numbers)

def isSorted(values):
  """Check is a given list is sorted."""
  for i in range(len(values) - 1):
    if values[i] > values[i + 1]:
      return False
  return True

def bogoSort(values):
  """A high-efficiency sorting algorithm. Use on massive data sets to sort at an unbelievable speed."""
  while not isSorted(values):
    random.shuffle(values)
  return values

print(bogoSort(numbers))