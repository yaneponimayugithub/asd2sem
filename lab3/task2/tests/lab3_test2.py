import random
import unittest, time
from lab2.utils import get_memory_usage
from lab3.task2.src.components import *

filename = os.path.basename(__file__)


class MyTestCase(unittest.TestCase):
    def test_should_components(self):
        # given
        data = [(1,2),(3,4),(4,5),(1,3),(7,8),(3,6),(9,1)]

        expected_data = 2
        # when
        nodes = {}
        a, b = map(int, data[0])
        for i in range(a):
            nodes[i + 1] = Node(i + 1)

        # Чтение всех строк, включая первую и последнюю
        for line in data[1:]:
            u, v = map(int, line)
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
        result = cc
        # then
        self.assertEqual(result, expected_data)

    def test_should_components_time_and_memory_hard(self):
        # given
        data = [(random.randint(1,10**3),random.randint(1,10**3)) for _ in range(10**3)]
        max_time = 5.0
        max_memory = 512.0
        # when
        t_start = time.perf_counter()
        nodes = {}
        a, b = map(int, data[0])
        for i in range(a):
            nodes[i + 1] = Node(i + 1)

        # Чтение всех строк, включая первую и последнюю
        for line in data[1:]:
            u, v = map(int, line)
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
        result = cc
        elapsed_time = time.perf_counter() - t_start

        initial_memory = get_memory_usage()
        nodes = {}
        a, b = map(int, data[0])
        for i in range(a):
            nodes[i + 1] = Node(i + 1)

        # Чтение всех строк, включая первую и последнюю
        for line in data[1:]:
            u, v = map(int, line)
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
        result = cc
        final_memory = get_memory_usage() - initial_memory

        # then
        self.assertLess(elapsed_time, max_time,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Время работы слишком долго: {elapsed_time:.8f} секунд")
        self.assertLess(final_memory, max_memory,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Используемая память слишком велика: {final_memory:.8f} МБ")

if __name__ == '__main__':
    unittest.main()
