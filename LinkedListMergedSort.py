from Linked_List import LinkedList

def mergeSort(linkedList):
  """
  Sorts a linked list in ascending order.
  - Recursively divide the linked list into sublists containing a single node.
  - Repeatedly merge the sublists to produce sorted sublists until one remains.

  Returns a sorted linked list.
  """

  if linkedList.size() == 1:
    return linkedList
  elif linkedList.head == None:
    return linkedList
  
  leftHalf, rightHalf = split(linkedList)
  left = mergeSort(leftHalf)
  right = mergeSort(rightHalf)

  return merge(left, right)

def split(linkedList):
  """
  Divide the unsorted list at midpoint into sublists.
  """

  if linkedList == None or linkedList.head == None:
    leftHalf = linkedList
    rightHalf = None

    return leftHalf, rightHalf
  else:
    size = linkedList.size()
    mid = size // 2

    midNode = linkedList.nodeAtIndex(mid - 1)

    leftHalf = linkedList
    rightHalf = LinkedList()
    rightHalf.head = midNode.nextNode
    midNode.nextNode = None

    return leftHalf, rightHalf
  
def merge(left, right):
  """
  Merges two linked lists, sorting by data in nodes.
  Returns a new, merged list.
  """

  # Create a new linked list that contains node from
  # merging left and right

  merged = LinkedList()

  # Add a fake head that is discarded later
  merged.add(0)

  # Set current to the head of the linked list
  current = merged.head

  # Obtain head nodes for left and right linked lists
  leftHead = left.head
  rightHead = right.head

  # Iterate over left and right until we reach the tail node of either
  while leftHead or rightHead:
    # If the head node of left is None, we are past the tail
    # Add the node form right to merged linked list
    if leftHead is None:
      current.nextNode = rightHead
      # Call next on right to set loop condition to false
      rightHead = rightHead.nextNode
    # If the head node of right is None, we are past the tail
    # Add the tail node form left to merged linked list
    elif rightHead is None:
      current.nextNode = leftHead
      # Call next on left to set loop condition to False
      leftHead = leftHead.nextNode
    else:
      # not at either tail node
      # Obtain node data to perform comparison operations
      leftData = leftHead.data
      rightData = rightHead.data
      # If data on left is less than right, set current to left node
      if leftData < rightData:
        current.nextNode = leftHead
        # Move left head to next node
        leftHead = leftHead.nextNode
      # If data on left is greater than right, set current to right node
      else:
        current.nextNode = rightHead
        # Move right head to next nodee
        rightHead = rightHead.nextNode
    # Move current to next node
    current = current.nextNode
  
  # discard fake head and set first merged node as head
  head = merged.head.nextNode
  merged.head = head

  return merged

l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)

print(l)
sortedLinkedList = mergeSort(l)
print(sortedLinkedList)