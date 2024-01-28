class Node:
  """An Object for storing a single node of a linked list.
  Models two attributes - data and the link to the next node in the list."""
  data = None
  nextNode = None
  
  def __init__(self, data):
    self.data = data
  
  def __repr__(self):
    return "<Node data: %s>" % self.data

class LinkedList:
  """Singly linked list"""
  def __init__(self):
    self.head = None

  def isEmpty(self):
    return self.head == None

  def size(self):
    """Returns the number of nodes in the list.
    Takes O(n) time."""
    current = self.head
    count = 0

    while current:
      count += 1
      current = current.nextNode
    return count
  
  def add(self, data):
    """
    Adds a new Node containing data at the head of the list.
    Takes O(1) time.
    """
    newNode = Node(data)
    newNode.nextNode = self.head
    self.head = newNode

  def search(self, key):
    """Search for the first node containing data that matches the key.
    Returns the node or 'None" if not found.
    Takes O(n) time."""

    current = self.head
    while current:
      if current.data == key:
        return current
      else:
        current =  current.nextNode
    return None  
  
  def insert(self, data, index):
    """Inserts a new Node containing data at index position.
    Insertion takes O(1) time but finding the node at the insertion point takes O(n) time.
    Takes overall O(n) time."""
    if index == 0:
      self.add(data)

    if index > 0:
      new = Node(data)
      
      position = index
      current = self.head

      while position > 1:
        current = current.nextNode
        position -= 1
      
      prev = current
      nxt = current.nextNode

      prev.nextNode = new
      new.nextNode = nxt

  def remove(self, key):
    """Removes Node containing data that matches the key.
    Returns the node or None if key doesn't exist
    Takes O(n) time."""
    current = self.head
    previous = None
    found = False

    while current and not found:
      if current.data == key and current == self.head:
        found == True
        self.head = current.nextNode
      elif current.data == key:
        found = True
        previous.nextNode = current.nextNode
      else:
        previous = current
        current = current.nextNode
      
    return current

  def removeIndex(self, index):
    """Removes Node at index.
    I made this one myself so I will have to figure out what the time and complexity is.s"""
    current = self.head
    
    if index == 0:
      self.head = current.nextNode
    
    if index > 0:
      position = index
      
      while position > 0:
        prev = current
        current = current.nextNode
        position -= 1
        

      
      nxt = current.nextNode
      print(prev)
      print(current)
      print(nxt)

      prev.nextNode = nxt
  

  def __repr__(self):
    """Return a string representation of the list.
    Takes O(n) time."""

    nodes = []
    current = self.head

    while current:
      if current is self.head:
        nodes.append("[Head: %s]" % current.data)
      elif current.nextNode is None:
        nodes.append("[Tail: %s]" % current.data)
      else:
        nodes.append("[%s]" % current.data)

      current = current.nextNode
    return '->'.join(nodes)

l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.insert(4, 2)
print(l)
l.removeIndex(2)
print(l)

