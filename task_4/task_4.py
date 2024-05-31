import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

class MinHeap:
    def __init__(self):
        self.heap = []
        self.node_count = 0

    def parent(self, i):
        return (i - 1) // 2

    def insert(self, key):
        self.heap.append(key)
        self.node_count += 1
        i = self.node_count - 1
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def min_heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < self.node_count and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < self.node_count and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

    def build_heap(self, keys):
        self.heap = keys
        self.node_count = len(self.heap)
        for i in range(self.node_count // 2, -1, -1):
            self.min_heapify(i)

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def visualize_heap(heap):
    root = Node(heap.heap[0])  
    for i in range(1, heap.node_count):
        add_node_to_heap_tree(root, heap.heap[i])  

    draw_tree(root)  

def add_node_to_heap_tree(node, key):
    if not node.left:
        node.left = Node(key)
    elif not node.right:
        node.right = Node(key)
    elif node.left and not node.right:
        add_node_to_heap_tree(node.right, key)
    else:
        add_node_to_heap_tree(node.left, key)

# Приклад використання
heap = MinHeap()
elements = [0, 4, 1, 5, 10, 3]
for element in elements:
    heap.insert(element)

visualize_heap(heap)
