import random
import unittest, time
from lab1.utils import get_memory_usage
from lab1.task2.src.gas_stations import *

filename = os.path.basename(__file__)


class MyTestCase(unittest.TestCase):
    def test_should_max_cost_resources(self):
        # given
        data = 1240, 320,7, [200,500,630,650,750,1000,1005]
        expected_data = 4

        # when
        result = count_gas_stations(data[0], data[1], data[2],data[3])

        # then
        self.assertEqual(result, expected_data)

    def test_should_max_cost_resources_time_and_hard(self):
        # given
        dist = 10**5
        full_fuel = random.randint(0,400)
        count_stations = 300
        values = []
        for _ in range(count_stations): # 300 чисел, которые не повторяются и до 10**5
            while True:
                value = random.randint(1, 10 ** 5)
                if value not in values:
                    values.append(value)
                    break
        values.sort()
        max_time = 2.0

        # when
        t_start = time.perf_counter()
        count_gas_stations(dist,full_fuel,count_stations,values)
        elapsed_time = time.perf_counter() - t_start

        # then
        self.assertLess(elapsed_time, max_time,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Время работы слишком долго: {elapsed_time:.8f} секунд")

    def test_should_max_cost_resources_time_and_easy(self):
        # given
        dist = 10 ** 3
        full_fuel = random.randint(0, 40)
        count_stations = 30
        values = []
        for _ in range(count_stations):  # 300 чисел, которые не повторяются и до 10**5
            while True:
                value = random.randint(1, 10 ** 3)
                if value not in values:
                    values.append(value)
                    break
        values.sort()
        max_time = 2.0

        # when
        t_start = time.perf_counter()
        count_gas_stations(dist, full_fuel, count_stations, values)
        elapsed_time = time.perf_counter() - t_start

        # then
        self.assertLess(elapsed_time, max_time,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Время работы слишком долго: {elapsed_time:.8f} секунд")


if __name__ == '__main__':
    unittest.main()
