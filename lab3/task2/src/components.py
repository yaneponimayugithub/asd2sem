import os
import lab2.utils as utils

input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

class Node:
    def __init__(self, value):
        self.value = value
        self.children = [] # содержит не значения а объекты класса Node

    def add_child(self, child):
        self.children.append(child)

    def explore(self):
        """Реализация поиска в глубину (DFS)"""
        visited = set()  # Множество для отслеживания посещенных узлов

        # Вспомогательная рекурсивная функция для DFS
        def dfs(node):
            """Рекурсивный DFS"""
            if node in visited:
                return 1
            visited.add(node)  # Отмечаем узел как посещенный
            # Рекурсивно обходим всех детей узла
            for child in node.children:
                dfs(child)


        dfs(self)

        # Возвращаем множество значений узлов, а не сами узлы
        return {node.value for node in visited}

if __name__ == '__main__':
    @utils.measure_time_and_memory
    def task():
        lines = utils.read_input(input_path)
        nodes = {}
        a,b = map(int,lines[0].split())
        for i in range(a):
            nodes[i+1]=Node(i+1)


        # Чтение всех строк, включая первую и последнюю
        for line in lines[1:]:
            u, v = map(int, line.split())
            # Ищем или создаем узлы для u и v
            if u not in nodes:
                nodes[u] = Node(u)
            if v not in nodes:
                nodes[v] = Node(v)

            nodes[u].add_child(nodes[v])  # u -> v
            nodes[v].add_child(nodes[u])  # v -> u

        visited = set()  # Для отслеживания посещенных вершин
        cc = 0  # Счётчик компонент связности

        # Запускаем DFS для каждой вершины, если она еще не была посещена
        for node in nodes.values():
            if node.value not in visited:  # Если вершина не посещена
                # Запускаем DFS из этой вершины
                component = node.explore()
                visited.update(component)  # Отметим все вершины этой компоненты как посещенные
                cc += 1  # Увеличиваем количество компонент связности

        # Записываем количество компонент связности в файл
        utils.write_output(output_path, cc)

    task()

