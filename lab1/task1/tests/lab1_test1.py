import random
import unittest, time
from lab1.utils import get_memory_usage
from lab1.task1.src.max_cost_resources import *

filename = os.path.basename(__file__)


class MyTestCase(unittest.TestCase):
    def test_should_max_cost_resources(self):
        # given
        data = 5, 45, [[30, 15], [40, 25], [10, 10], [5, 0], [60, 25]]
        expected_data = 103

        # when
        result = max_cost_items(data[0], data[1], data[2])

        # then
        self.assertEqual(result, expected_data)

    def test_should_max_cost_resources_time_and_memory_hard(self):
        # given
        n = 10 ** 3
        W = random.randint(0, 2 * 10 ** 6)
        items = [tuple((random.randint(0, 2 * 10 ** 6), random.randint(0, 2 * 10 ** 6))) for _ in range(n)]
        max_time = 2.0

        # when
        t_start = time.perf_counter()
        max_cost_items(n, W, items)
        elapsed_time = time.perf_counter() - t_start

        # then
        self.assertLess(elapsed_time, max_time,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Время работы слишком долго: {elapsed_time:.8f} секунд")

    def test_should_max_cost_resources_time_and_memory_easy(self):
        # given
        n = 10 ** 2
        W = random.randint(0, 2 * 10 ** 3)
        items = [tuple((random.randint(0, 2 * 10 ** 3), random.randint(0, 2 * 10 ** 3))) for _ in range(n)]
        max_time = 2.0

        # when
        t_start = time.perf_counter()
        max_cost_items(n, W, items)
        elapsed_time = time.perf_counter() - t_start

        # then
        self.assertLess(elapsed_time, max_time,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Время работы слишком долго: {elapsed_time:.8f} секунд")


if __name__ == '__main__':
    unittest.main()
