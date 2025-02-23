import random
import unittest, time
from lab1.utils import get_memory_usage
from lab1.task14.src.max_value import *

filename = os.path.basename(__file__)


class MyTestCase(unittest.TestCase):
    def test_should_max_value(self):
        # given
        data = "2*3+5-6*4-5*4"
        expected_data = 208

        # when
        result = max_value(data)

        # then
        self.assertEqual(result, expected_data)

    def test_should_max_value_time_hard(self):
        # given
        op = "+-*"
        data = [str(random.randint(0, 9)) if i % 2 == 0 else op[random.randint(0, 2)] for i in range(29)]
        data = "".join(data)
        max_time = 5.0

        # when
        t_start = time.perf_counter()
        max_value(data)
        elapsed_time = time.perf_counter() - t_start

        # then
        self.assertLess(elapsed_time, max_time,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Время работы слишком долго: {elapsed_time:.8f} секунд")

    def test_should_max_value_time_easy(self):
        # given
        op = "+-*"
        data = [str(random.randint(0, 9)) if i % 2 == 0 else op[random.randint(0, 2)] for i in range(9)]
        data = "".join(data)
        max_time = 5.0

        # when
        t_start = time.perf_counter()
        max_value(data)
        elapsed_time = time.perf_counter() - t_start

        # then
        self.assertLess(elapsed_time, max_time,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Время работы слишком долго: {elapsed_time:.8f} секунд")

if __name__ == '__main__':
    unittest.main()
