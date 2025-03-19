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

        # Запускаем DFS с текущего узла
        dfs(self)

        # Возвращаем множество значений узлов, а не сами узлы
        return {node.value for node in visited}

if __name__ == '__main__':
    @utils.measure_time_and_memory
    def task():
        lines = utils.read_input(input_path)

        nodes = {}

        # Чтение всех строк, включая первую и последнюю
        for line in lines[1:-1]:
            u, v = map(int, line.split())
            # Ищем или создаем узлы для u и v
            if u not in nodes:
                nodes[u] = Node(u)
            if v not in nodes:
                nodes[v] = Node(v)

            nodes[u].add_child(nodes[v])  # u -> v
            nodes[v].add_child(nodes[u])  # v -> u

        # Обработка последней строки для проверки наличия пути
        u, v = map(int, lines[-1].split())


        if u not in nodes or v not in nodes:
            # Обработка ошибки, если одного из узлов нет в графе
            return utils.write_output(output_path, 0)

        u_node, v_node = nodes[u], nodes[v]

        # Проверка существования пути
        if v in u_node.explore():  # Теперь проверяем значение v в множестве
            utils.write_output(output_path, 1)
        else:
            utils.write_output(output_path, 0)


    task()

