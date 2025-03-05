import random
import unittest, time
from lab2.utils import get_memory_usage
from lab2.task1.src.binary_tree_in_depth import *

filename = os.path.basename(__file__)


class MyTestCase(unittest.TestCase):

    def test_should_alisa_apple_time_and_memory_hard(self):
        # given
        data = set()
        used_vetki = set()

        for _ in range(10 ** 2):
            while True:
                rand_number = [random.randint(-1, 10 ** 2 - 1), random.randint(-1, 10 ** 2 - 1)]
                main_vet = random.randint(0, 10 ** 9)

                if rand_number[0] in used_vetki or rand_number[1] in used_vetki or any(v[0] == main_vet for v in data):
                    continue
                else:
                    data.add((main_vet, rand_number[0], rand_number[1]))  # Исправлено
                    used_vetki.add(main_vet)  # Добавляем rand_number в used_vetki
                    break
        Tree = BinaryTreeDFS(data)
        max_time = 5.0
        max_memory = 512.0
        print(data) and exit()
        # when
        t_start = time.perf_counter()
        Tree.postorderTraversal(Tree.root)
        Tree.preorderTraversal(Tree.root)
        Tree.inorderTraversal(Tree.root)
        elapsed_time = time.perf_counter() - t_start

        initial_memory = get_memory_usage()
        Tree.postorderTraversal(Tree.root)
        Tree.preorderTraversal(Tree.root)
        Tree.inorderTraversal(Tree.root)
        final_memory = get_memory_usage() - initial_memory

        # then
        self.assertLess(elapsed_time, max_time,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Время работы слишком долго: {elapsed_time:.8f} секунд")
        self.assertLess(final_memory, max_memory,
                        f"[lab - {filename[3]} | task - {filename[9]} ] Используемая память слишком велика: {final_memory:.8f} МБ")


if __name__ == '__main__':
    unittest.main()
