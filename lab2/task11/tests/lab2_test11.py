import random
import unittest, time
from lab2.utils import get_memory_usage
from lab2.task11.src.balanced_binary_tree import *

filename = os.path.basename(__file__)


class MyTestCase(unittest.TestCase):

    def test_should_easiest_BST_time_and_memory_hard(self):
        # given
        op = ["insert", "delete", "exists", "next", "prev"]
        data = [(random.choice(op), random.randint(-10**9,10**9)) for _ in range(10**5)]
        max_time = 2.0
        max_memory = 512.0
        Tree = BinTree()

        # when
        initial_memory = get_memory_usage()
        t_start = time.perf_counter()
        for cmd, value in data:
            value = int(value)
            match cmd:
                case 'insert':
                    Tree.insert(value)
                case 'delete':
                    Tree.delete(value)
                case 'exists':
                    Tree.exists(value)
                case 'next':
                    Tree.next(value)
                case 'prev':
                    Tree.prev(value)
        elapsed_time = time.perf_counter() - t_start
        final_memory = get_memory_usage() - initial_memory

        # then
        self.assertLess(elapsed_time, max_time,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Время работы слишком долго: {elapsed_time:.8f} секунд")
        self.assertLess(final_memory, max_memory,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Используемая память слишком велика: {final_memory:.8f} МБ")
if __name__ == '__main__':
    unittest.main()
