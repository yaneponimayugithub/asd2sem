import os
import lab2.utils as utils

input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))


class Node:
    def __init__(self, key):
        self.key = key
        self.right = self.left = self.parent = None


class BinTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)  # Если дерево пустое, создаём корень
        else:
            self._insert_if(self.root, key)

    def _insert_if(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)

            else:
                self._insert_if(node.left, key)

        elif key > node.key:
            if node.right is None:
                node.right = Node(key)

            else:
                self._insert_if(node.right, key)

    def delete(self, key):
        self.root = self._delete_node(self.root, key)  # Начинаем с корня

    def _delete_node(self, node, key):
        if node is None:
            return node  # Если узел не найден, возвращаем None

        if key < node.key:
            # Если ключ меньше текущего узла, ищем в левом поддереве
            node.left = self._delete_node(node.left, key)
        elif key > node.key:
            # Если ключ больше текущего узла, ищем в правом поддереве
            node.right = self._delete_node(node.right, key)
        else:
            # Нашли узел, который нужно удалить
            if node.left is None and node.right is None:
                # У узла нет детей
                node = None
            elif node.left is None:
                # У узла только правый потомок
                node = node.right
            elif node.right is None:
                # У узла только левый потомок
                node = node.left
            else:
                # У узла два потомка
                # Находим минимальный узел в правом поддереве
                min_node = self._find_min(node.right)
                node.key = min_node.key  # Копируем ключ минимального узла
                # Удаляем этот минимальный узел из правого поддерева
                node.right = self._delete_node(node.right, min_node.key)

        return node

    def exists(self, key):

        return "true" if self._find_node(self.root, key) is not None else "false"

    def _find_node(self, node, key):

        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._find_node(node.left, key)
        else:
            return self._find_node(node.right, key)

    def next(self, key):
        current = self.root
        nexter = None
        while current is not None:
            if current.key > key:
                nexter = current
                current = current.left
            else:
                current = current.right
        return str(nexter.key) if nexter is not None else "none"

    def prev(self, key):
        current = self.root
        prever = None
        while current is not None:
            if current.key < key:
                prever = current
                current = current.right
            else:
                current = current.left
        return str(prever.key) if prever is not None else "none"

    @staticmethod
    def _find_min(node):
        current = node
        while current.left is not None:
            current = current.left
        return current




if __name__ == '__main__':
    @utils.measure_time_and_memory
    def task():
        lines = utils.read_input(input_path)
        lines = [line.split() for line in lines]
        Tree = BinTree()
        result = []
        for cmd,value in lines:
            value = int(value)
            match cmd:
                case 'insert':
                    Tree.insert(value)
                case 'delete':
                    Tree.delete(value)
                case 'exists':
                    result.append(Tree.exists(value))
                case 'next':
                    result.append(Tree.next(value))
                case 'prev':
                    result.append(Tree.prev(value))

        utils.write_output_list_row(output_path, result)
    task()
