import heapq

class Graph:
    def __init__(self):
        self.edges = {}
    
    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.edges:
            self.edges[from_vertex] = []
        self.edges[from_vertex].append((to_vertex, weight))
        
        # Додатково додаємо ребро назад для неорієнтованого графа
        if to_vertex not in self.edges:
            self.edges[to_vertex] = []
        self.edges[to_vertex].append((from_vertex, weight))

def dijkstra(graph, start):
    # Відстані до всіх вершин (інфініті на початку)
    distances = {vertex: float('infinity') for vertex in graph.edges}
    distances[start] = 0
    
    # Мін-купа для вершин, які треба обробити
    priority_queue = [(0, start)]
    
    # Словник для зберігання попередників вершин у найкоротших шляхах
    predecessors = {}
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Якщо знайдено коротший шлях до вершини, пропускаємо
        if current_distance > distances[current_vertex]:
            continue
        
        # Переглядаємо суміжні вершини
        for neighbor, weight in graph.edges[current_vertex]:
            distance = current_distance + weight
            
            # Якщо знайдено коротший шлях до сусідньої вершини, оновлюємо
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, predecessors

def shortest_paths(graph, start):
    all_shortest_paths = {}
    distances, predecessors = dijkstra(graph, start)
    for vertex in graph.edges:
        if vertex != start:
            path = []
            current_vertex = vertex
            while current_vertex != start:
                path.append(current_vertex)
                current_vertex = predecessors[current_vertex]
            path.append(start)
            all_shortest_paths[vertex] = (distances[vertex], path[::-1])
    return all_shortest_paths

# Приклад використання
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)
graph.add_edge('C', 'E', 4)
graph.add_edge('E', 'A', 10)

start_vertex = 'A'
all_shortest_paths = shortest_paths(graph, start_vertex)

print(f"Найкоротші шляхи від вершини {start_vertex}:")
for vertex, (distance, path) in all_shortest_paths.items():
    print(f"До вершини {vertex}:")
    print(f"Довжина шляху: {distance}")
    print(f"Шлях: {' -> '.join(path)}")
    print()
