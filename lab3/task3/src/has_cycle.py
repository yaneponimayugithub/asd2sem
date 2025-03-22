import os
import lab2.utils as utils

input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

class Node:
    def __init__(self, value):
        self.value = value
        self.children = [] # содержит не значения а объекты класса Node

    def add_child(self, child):
        self.children.append(child)

    def has_cycle(self):
        """Проверка на цикл с помощью DFS"""
        visited = set()  # Множество для посещённых узлов
        stack = set()  # Множество для узлов в процессе обхода

        # Рекурсивная функция для обхода в глубину (DFS)
        def dfs(node):
            if node in stack:  # Если узел в стеке, то найден цикл
                return True
            if node in visited:  # Если узел уже посещён, пропускаем его
                return False

            stack.add(node)  # Добавляем узел в стек (пока в процессе обхода)
            for child in node.children:
                if dfs(child):  # Рекурсивно ищем цикл среди детей
                    return True
            stack.remove(node)  # Убираем узел из стека после обработки всех детей
            visited.add(node)  # Добавляем узел в посещённые

            return False

        # Начинаем DFS с текущего узла
        return dfs(self)

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


        def check_cycles_in_graph(nodes):
            """Проверка на циклы в графе"""
            visited = set()

            for node in nodes.values():
                if node not in visited:  # Если узел ещё не посещён
                    if node.has_cycle():  # Если найден цикл в компоненте связности
                        return True
                    visited.add(node)  # Добавляем узел в посещённые

            return False

        utils.write_output(output_path, check_cycles_in_graph(nodes))

    task()

