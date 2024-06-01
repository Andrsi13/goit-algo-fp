import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
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
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def depth_first_traversal(root):
    if root is None:
        return
    stack = [(root, 0)]
    visited = set()
    visit_order = 0
    while stack:
        node, depth = stack.pop()
        if node not in visited:
            node.visit_order = visit_order
            visited.add(node)
            visit_order += 1
            # Визначення кольору вузла на основі порядку обходу (менш насичені кольори голубого)
            color = (0, 0, max(0.2, 1 - node.visit_order / visit_order))  # RGB
            node.color = color
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))

def breadth_first_traversal(root):
    if root is None:
        return
    queue = [(root, 0)]
    visited = set()
    visit_order = 0
    while queue:
        node, depth = queue.pop(0)
        if node not in visited:
            node.visit_order = visit_order
            visited.add(node)
            visit_order += 1
            # Визначення кольору вузла на основі порядку обходу (менш насичені кольори голубого)
            color = (0, 0, max(0.2, 1 - node.visit_order / visit_order))  # RGB
            node.color = color
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

# Візуалізація дерева з обходом
def draw_tree_with_traversal(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, font_color='white')
    plt.show()

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
draw_tree(root)

print("Depth First Traversal:")
depth_first_traversal(root)
draw_tree_with_traversal(root)

print("\nBreadth First Traversal:")
breadth_first_traversal(root)
draw_tree_with_traversal(root)