import random
import unittest, time
from lab1.utils import get_memory_usage
from lab1.task10.src.alisa_apple import *

filename = os.path.basename(__file__)


class MyTestCase(unittest.TestCase):
    def test_should_alisa_apple(self):
        # given
        data = 15, [[14,15],[6,5],[2,6],[6,9],[8,10]]
        expected_data = [3, 4, 5, 1, 2]

        # when
        result = alisa_apple_eat(data[0],data[1])

        # then
        self.assertEqual(result, expected_data)

    def test_should_alisa_apple_time_and_memory_hard(self):
        # given
        height = random.randint(1,1000)
        data = [[random.randint(1,1000),random.randint(1,1000)] for _ in range(1000)]
        max_time = 5.0
        max_memory = 256.0

        # when
        t_start = time.perf_counter()
        alisa_apple_eat(height,data)
        elapsed_time = time.perf_counter() - t_start

        initial_memory = get_memory_usage()
        alisa_apple_eat(height,data)
        final_memory = get_memory_usage() - initial_memory

        # then
        self.assertLess(elapsed_time, max_time,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Время работы слишком долго: {elapsed_time:.8f} секунд")
        self.assertLess(final_memory, max_memory,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Используемая память слишком велика: {final_memory:.8f} МБ")

    def test_should_alisa_apple_time_and_memory_easy(self):
        # given
        height = random.randint(500,1000)
        data = [[random.randint(1,100),random.randint(50,100)] for _ in range(100)]
        max_time = 5.0
        max_memory = 256.0

        # when
        t_start = time.perf_counter()
        alisa_apple_eat(height,data)
        elapsed_time = time.perf_counter() - t_start

        initial_memory = get_memory_usage()
        alisa_apple_eat(height,data)
        final_memory = get_memory_usage() - initial_memory

        # then
        self.assertLess(elapsed_time, max_time,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Время работы слишком долго: {elapsed_time:.8f} секунд")
        self.assertLess(final_memory, max_memory,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Используемая память слишком велика: {final_memory:.8f} МБ")

if __name__ == '__main__':
    unittest.main()
