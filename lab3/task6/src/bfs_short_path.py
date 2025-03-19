import os
import lab2.utils as utils
from collections import deque

input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []  # Список смежности (соседи)

    def add_child(self, child):
        self.children.append(child)

    def bfs_shortest_path(self, target):
        """Реализация поиска кратчайшего пути с помощью BFS"""
        visited = set()  # Множество для посещённых узлов
        distance = {self.value: 0}  # Словарь для хранения расстояний от начальной вершины
        queue = deque([self])  # Очередь для BFS

        visited.add(self.value)

        while queue:
            current_node = queue.popleft()

            # Если мы нашли целевой узел, возвращаем расстояние
            if current_node.value == target:
                return distance[current_node.value]

            # Проходим по всем соседям текущей вершины
            for child in current_node.children:
                if child.value not in visited:
                    visited.add(child.value)
                    distance[child.value] = distance[current_node.value] + 1
                    queue.append(child)

        # Если путь не найден
        return -1


if __name__ == '__main__':
    @utils.measure_time_and_memory
    def task():
        lines = utils.read_input(input_path)
        nodes = {}
        n, m = map(int, lines[0].split())  # Чтение количества городов и рёбер

        # Создаём узлы для каждого города
        for i in range(1, n + 1):
            nodes[i] = Node(i)

        # Строим граф
        for line in lines[1:-1]:
            u, v = map(int, line.split())
            nodes[u].add_child(nodes[v])  # Добавляем ребро u-v
            nodes[v].add_child(nodes[u])  # Добавляем ребро v-u (граф неориентированный)

        # Вводим начальный и целевой города
        u, v = map(int, lines[-1].split())  # Города, для которых ищем кратчайший путь

        # Ищем кратчайший путь между городами u и v
        shortest_path = nodes[u].bfs_shortest_path(v)

        # Выводим результат
        utils.write_output(output_path, str(shortest_path))


    task()
