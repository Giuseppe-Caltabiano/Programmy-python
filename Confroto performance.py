import time
import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
    def search(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = BSTNode(value)
        else:
            self._insert_rec(self.root, value)
            
    def _insert_rec(self, node, value):
        if value < node.value:
            if node.left: self._insert_rec(node.left, value)
            else: node.left = BSTNode(value)
        else:
            if node.right: self._insert_rec(node.right, value)
            else: node.right = BSTNode(value)
            
    def search(self, value):
        return self._search_rec(self.root, value)
        
    def _search_rec(self, node, value):
        if not node: return False
        if node.value == value: return True
        if value < node.value: return self._search_rec(node.left, value)
        return self._search_rec(node.right, value)

numbers = [random.randint(1, 10000) for _ in range(1000)]

ll = LinkedList()
bst = BST()
for n in numbers:
    ll.insert(n)
    bst.insert(n)

target = numbers[499]

start_ll = time.perf_counter()
ll.search(target)
end_ll = time.perf_counter()
ll_time = end_ll - start_ll

start_bst = time.perf_counter()
bst.search(target)
end_bst = time.perf_counter()
bst_time = end_bst - start_bst

print(f"Tempo LinkedList: {ll_time:.10f} secondi")
print(f"Tempo BST: {bst_time:.10f} secondi")

if bst_time > 0:
    ratio = ll_time / bst_time
    print(f"Il BST è {ratio:.2f} volte più veloce della LinkedList")