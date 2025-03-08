import random
import unittest, time
from lab2.utils import get_memory_usage
from lab2.task3.src.easiest_BST import *

filename = os.path.basename(__file__)


class MyTestCase(unittest.TestCase):
    def test_should_easiest_BST(self):
        # given
        data = ['+ 2','+ 4','+ 6','> 3','> 4','+ 5','+ 10','> 1','> 11','+ 5','+ 22','> 16','+ 2','+ 76','> 23','> 55','> 2','> 4','+ 3','> 3','> 4']
        Tree = BTS()
        expected_data = [4, 6, 2, 0, 22, 76, 76, 4, 5, 4, 5]
        result = []

        # when
        for line in data:
            if line[0] == "+":
                Tree.root = Tree.insert(int(line[2:]), Tree.root)
            elif line[0] == ">":
                result.append(Tree.getmin(int(line[2:])))

        # then
        self.assertEqual(result, expected_data)

    def test_should_easiest_BST_time_and_memory_hard(self):
        # given
        data = [f'{random.choice((">","+"))} {random.randint(0,10**9)}' for _ in range(300000)]
        max_time = 2.0
        max_memory = 256.0
        Tree = BTS()
        Tree2 = BTS()
        # when
        t_start = time.perf_counter()
        for line in data:
            if line[0] == "+":
                Tree.root = Tree.insert(int(line[2:]), Tree.root)
            elif line[0] == ">":
                Tree.getmin(int(line[2:]))
        elapsed_time = time.perf_counter() - t_start

        initial_memory = get_memory_usage()
        for line in data:
            if line[0] == "+":
                Tree2.root = Tree2.insert(int(line[2:]), Tree2.root)
            elif line[0] == ">":
                Tree2.getmin(int(line[2:]))
        final_memory = get_memory_usage() - initial_memory

        # then
        self.assertLess(elapsed_time, max_time,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Время работы слишком долго: {elapsed_time:.8f} секунд")
        self.assertLess(final_memory, max_memory,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Используемая память слишком велика: {final_memory:.8f} МБ")

    def test_should_alisa_apple_time_and_memory_easy(self):
        # given
        data = [f'{random.choice((">", "+"))} {random.randint(0, 10 ** 4)}' for _ in range(5000)]
        max_time = 2.0
        max_memory = 256.0
        Tree = BTS()
        Tree2 = BTS()
        # when
        t_start = time.perf_counter()
        for line in data:
            if line[0] == "+":
                Tree.root = Tree.insert(int(line[2:]), Tree.root)
            elif line[0] == ">":
                Tree.getmin(int(line[2:]))
        elapsed_time = time.perf_counter() - t_start

        initial_memory = get_memory_usage()
        for line in data:
            if line[0] == "+":
                Tree2.root = Tree2.insert(int(line[2:]), Tree2.root)
            elif line[0] == ">":
                Tree2.getmin(int(line[2:]))
        final_memory = get_memory_usage() - initial_memory

        # then
        self.assertLess(elapsed_time, max_time,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Время работы слишком долго: {elapsed_time:.8f} секунд")
        self.assertLess(final_memory, max_memory,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Используемая память слишком велика: {final_memory:.8f} МБ")
if __name__ == '__main__':
    unittest.main()
