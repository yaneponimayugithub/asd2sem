import os
import lab2.utils as utils

input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BTS:
    def __init__(self):
        self.root = None

    def insert(self, key, root: Node):
        if root is None:
            return Node(key)  # Создаем новый узел с переданным ключом
        if key == root.key: # игнор сущ.значений
            return root
        if key < root.key:
            root.left = self.insert(key, root.left)  # Вставляем в левое поддерево
        elif key > root.key:
            root.right = self.insert(key, root.right)  # Вставляем в правое поддерево

        return root  # Возвращаем корень дерева для родительского вызова

    def getmin(self,x):
        current = self.root
        candidate = None

        while current:
            if current.key > x:
                candidate = current  # Нашли кандидата, который больше x
                current = current.left  # Идем влево, возможно найдем меньший элемент
            else:
                current = current.right  # Идем вправо, все элементы в левом поддереве меньше или равны x

        if candidate:
            return candidate.key  # Возвращаем найденный элемент
        else:
            return 0  # Если не нашли элемента, возвращаем 0


if __name__ == '__main__':
    @utils.measure_time_and_memory
    def task():
        lines = utils.read_input(input_path)
        tree = BTS()
        result = []
        for line in lines:
            if line[0] == "+":
                tree.root = tree.insert(int(line[2]), tree.root)
            elif line[0] == ">":
                result.append(tree.getmin(int(line[2])))

        utils.write_output_list_row(output_path, result)


    task()
