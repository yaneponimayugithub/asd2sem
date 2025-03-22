import random
import unittest, time
from lab2.utils import get_memory_usage
from lab3.task6.src.bfs_short_path import *

filename = os.path.basename(__file__)

class MyTestCase(unittest.TestCase):
    def test_should_bfs_short(self):
        # given
        data = [(7,7),(1,2),(3,4),(4,5),(1,3),(5,7),(3,6),(2,6)]

        expected_data = 3
        # when
        nodes = {}
        a, b = map(int, data[0])
        for i in range(a):
            nodes[i + 1] = Node(i + 1)

        # Чтение всех строк, включая первую и последнюю
        for line in data[1:-1]:
            u, v = map(int, line)
            # Ищем или создаем узлы для u и v
            if u not in nodes:
                nodes[u] = Node(u)
            if v not in nodes:
                nodes[v] = Node(v)

            nodes[u].add_child(nodes[v])  # u -> v
            nodes[v].add_child(nodes[u])  # Добавляем ребро v-u (граф неориентированный)

        # Вводим начальный и целевой города
        u, v = map(int, data[-1])  # Города, для которых ищем кратчайший путь

        # Ищем кратчайший путь между городами u и v
        result = nodes[u].bfs_shortest_path(v)

        # then
        self.assertEqual(result, expected_data)

    def test_should_bfs_short_time_and_memory_hard(self):
        # given
        data = [(random.randint(1,10**5),random.randint(1,10**5)) for _ in range(10**5)]
        max_time = 5.0
        max_memory = 512.0
        # when
        t_start = time.perf_counter()
        nodes = {}
        a, b = map(int, data[0])
        for i in range(a):
            nodes[i + 1] = Node(i + 1)

        # Чтение всех строк, включая первую и последнюю
        for line in data[1:-1]:
            u, v = map(int, line)
            # Ищем или создаем узлы для u и v
            if u not in nodes:
                nodes[u] = Node(u)
            if v not in nodes:
                nodes[v] = Node(v)

            nodes[u].add_child(nodes[v])  # u -> v
            nodes[v].add_child(nodes[u])  # Добавляем ребро v-u (граф неориентированный)

        # Вводим начальный и целевой города
        u, v = map(int, data[-1])  # Города, для которых ищем кратчайший путь

        # Ищем кратчайший путь между городами u и v
        result = nodes[u].bfs_shortest_path(v)

        elapsed_time = time.perf_counter() - t_start

        initial_memory = get_memory_usage()
        nodes = {}
        a, b = map(int, data[0])
        for i in range(a):
            nodes[i + 1] = Node(i + 1)

        # Чтение всех строк, включая первую и последнюю
        for line in data[1:-1]:
            u, v = map(int, line)
            # Ищем или создаем узлы для u и v
            if u not in nodes:
                nodes[u] = Node(u)
            if v not in nodes:
                nodes[v] = Node(v)

            nodes[u].add_child(nodes[v])  # u -> v
            nodes[v].add_child(nodes[u])  # Добавляем ребро v-u (граф неориентированный)

        # Вводим начальный и целевой города
        u, v = map(int, data[-1])  # Города, для которых ищем кратчайший путь

        # Ищем кратчайший путь между городами u и v
        result = nodes[u].bfs_shortest_path(v)

        final_memory = get_memory_usage() - initial_memory

        # then
        self.assertLess(elapsed_time, max_time,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Время работы слишком долго: {elapsed_time:.8f} секунд")
        self.assertLess(final_memory, max_memory,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Используемая память слишком велика: {final_memory:.8f} МБ")

if __name__ == '__main__':
    unittest.main()
