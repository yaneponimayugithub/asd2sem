import random
import unittest, time
from lab2.utils import get_memory_usage
from lab3.task1.src.labirint import *

filename = os.path.basename(__file__)


class MyTestCase(unittest.TestCase):
    def test_should_labirint(self):
        # given
        data = [(1,2),(3,4),(4,5),(1,3),(7,8),(3,6),(9,1),(1,7)]

        expected_data = 0
        nodes = {}
        # when
        for line in data[:-1]:
            u, v = map(int, line)
            # Ищем или создаем узлы для u и v
            if u not in nodes:
                nodes[u] = Node(u)
            if v not in nodes:
                nodes[v] = Node(v)

            nodes[u].add_child(nodes[v])  # u -> v
            nodes[v].add_child(nodes[u])  # v -> u

        # Обработка последней строки для проверки наличия пути
        u, v = map(int, data[-1])

        if u not in nodes or v not in nodes:
            # Обработка ошибки, если одного из узлов нет в графе
            result = 0
        else:

            u_node, v_node = nodes[u], nodes[v]

            # Проверка существования пути
            if v in u_node.explore():  # Теперь проверяем значение v в множестве
                result = 1
            else:
                result = 0

        # then
        self.assertEqual(result, expected_data)

    def test_should_labirint_time_and_memory_hard(self):
        # given
        data = [(random.randint(1,10**3),random.randint(1,10**3)) for _ in range(10**3)]
        max_time = 5.0
        max_memory = 512.0
        nodes = {}
        # when
        t_start = time.perf_counter()
        for line in data[:-1]:
            u, v = map(int, line)
            # Ищем или создаем узлы для u и v
            if u not in nodes:
                nodes[u] = Node(u)
            if v not in nodes:
                nodes[v] = Node(v)

            nodes[u].add_child(nodes[v])  # u -> v
            nodes[v].add_child(nodes[u])  # v -> u

        # Обработка последней строки для проверки наличия пути
        u, v = map(int, data[-1])

        if u not in nodes or v not in nodes:
            # Обработка ошибки, если одного из узлов нет в графе
            result = 0
        else:

            u_node, v_node = nodes[u], nodes[v]

            # Проверка существования пути
            if v in u_node.explore():  # Теперь проверяем значение v в множестве
                result = 1
            else:
                result = 0
        elapsed_time = time.perf_counter() - t_start
        nodes = {}
        initial_memory = get_memory_usage()
        for line in data[:-1]:
            u, v = map(int, line)
            # Ищем или создаем узлы для u и v
            if u not in nodes:
                nodes[u] = Node(u)
            if v not in nodes:
                nodes[v] = Node(v)

            nodes[u].add_child(nodes[v])  # u -> v
            nodes[v].add_child(nodes[u])  # v -> u

        # Обработка последней строки для проверки наличия пути
        u, v = map(int, data[-1])

        if u not in nodes or v not in nodes:
            # Обработка ошибки, если одного из узлов нет в графе
            result = 0
        else:

            u_node, v_node = nodes[u], nodes[v]

            # Проверка существования пути
            if v in u_node.explore():  # Теперь проверяем значение v в множестве
                result = 1
            else:
                result = 0
        final_memory = get_memory_usage() - initial_memory

        # then
        self.assertLess(elapsed_time, max_time,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Время работы слишком долго: {elapsed_time:.8f} секунд")
        self.assertLess(final_memory, max_memory,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Используемая память слишком велика: {final_memory:.8f} МБ")

if __name__ == '__main__':
    unittest.main()
