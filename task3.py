import heapq

def dijkstra(graph, start):
    # Ініціалізація відстаней та бінарної купи
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо поточна відстань більше вже знайденої, продовжуємо
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Тестування
if __name__ == "__main__":
    graph = {
        'A': {'B': 5, 'C': 10},
        'B': {'A': 5, 'D': 3},
        'C': {'A': 10, 'D': 2},
        'D': {'B': 3, 'C': 2, 'E': 4},
        'E': {'D': 4}
    }

    # Виклик функції для вершини A
    print(dijkstra(graph, 'A'))
