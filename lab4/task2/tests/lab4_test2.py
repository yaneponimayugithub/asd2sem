import random
import unittest, time
from lab4.utils import get_memory_usage
from lab4.task2.src.map import *

filename = os.path.basename(__file__)


class MyTestCase(unittest.TestCase):

    def test_should_map_time_and_memory_hard(self):
        # given
        data = [random.choice([' ',chr(random.randint(ord('a'), ord('z')))]) for _ in range(3*10 ** 5)]
        data = ''.join(data)

        max_time = 2.0
        max_memory = 256.0
        # when
        initial_memory = get_memory_usage()
        t_start = time.perf_counter()
        count_palindromic_substrings(data)
        elapsed_time = time.perf_counter() - t_start
        final_memory = get_memory_usage() - initial_memory

        # then
        self.assertLess(elapsed_time, max_time,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Время работы слишком долго: {elapsed_time:.8f} секунд")
        self.assertLess(final_memory, max_memory,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Используемая память слишком велика: {final_memory:.8f} МБ")
if __name__ == '__main__':
    unittest.main()
