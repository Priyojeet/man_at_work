class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class Slinklist:
    def __init__(self):
        self.head = None

list1 = Slinklist()
list1.head = Node('jeet')
ex2 = Node('priyo')
ex3 = Node('bhunia')
list1.head.nextval = ex2
ex2.nextval = ex3
