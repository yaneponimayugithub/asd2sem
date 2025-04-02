import random
import unittest, time
from lab4.utils import get_memory_usage
from lab4.task1.src.find_substring import *

filename = os.path.basename(__file__)


class MyTestCase(unittest.TestCase):

    def test_should_find_substring_time_and_memory_hard(self):
        # given
        data = [chr(random.randint(ord('a'), ord('z'))) for _ in range(10 ** 4)]
        data2 = [chr(random.randint(ord('a'), ord('z'))) for _ in range(random.randint(1,10**4))]
        data = ''.join(data)
        data2 = ''.join(data2)
        max_time = 2.0
        max_memory = 256.0
        # when
        initial_memory = get_memory_usage()
        t_start = time.perf_counter()
        kmp_search(data,data2)
        elapsed_time = time.perf_counter() - t_start
        final_memory = get_memory_usage() - initial_memory

        # then
        self.assertLess(elapsed_time, max_time,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Время работы слишком долго: {elapsed_time:.8f} секунд")
        self.assertLess(final_memory, max_memory,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Используемая память слишком велика: {final_memory:.8f} МБ")
if __name__ == '__main__':
    unittest.main()
