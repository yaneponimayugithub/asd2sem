import os
import lab2.utils as utils

input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTreeDFS:
    def __init__(self, data):
        self.root = None

        nodes = {i: Node(key) for i, (key, _, _) in enumerate(data)}  # Создаём узлы для всех данных

        # Создаём связи между узлами
        for i, (key, left, right) in enumerate(data):
            if left != -1:
                nodes[i].left = nodes[left]
            if right != -1:
                nodes[i].right = nodes[right]

        # Корень дерева (первый элемент в списке)
        self.root = nodes[0]
    # Обходит левое поддерево, затем текущий узел, затем правое поддерево
    def inorderTraversal(self, node):
        result = []
        if node is not None:
            result.extend(self.inorderTraversal(node.left))
            result.append(node.key)
            result.extend(self.inorderTraversal(node.right))
        return result
    # Сначала посещает текущий узел, затем левое поддерево, потом правое
    def preorderTraversal(self, node):
        result = []
        if node is not None:
            result.append(node.key)
            result.extend(self.preorderTraversal(node.left))
            result.extend(self.preorderTraversal(node.right))
        return result
    # Сначала обход левого и правого поддеревьев, затем текущий узел
    def postorderTraversal(self, node):
        result = []
        if node is not None:
            result.extend(self.postorderTraversal(node.left))
            result.extend(self.postorderTraversal(node.right))
            result.append(node.key)
        return result



if __name__ == '__main__':
    @utils.measure_time_and_memory
    def task():
        lines = utils.read_input(input_path)
        data = list()
        for line in lines[1::]:
            data.append(tuple(int(x) for x in line.split(" ")))
        result = BinaryTreeDFS(data)

        utils.write_output_list_row(output_path,
                                    [result.inorderTraversal(result.root), result.preorderTraversal(result.root),
                                     result.postorderTraversal(result.root)])


    task()
