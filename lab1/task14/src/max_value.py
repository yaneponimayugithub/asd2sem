import os
import lab1.utils as utils

input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))


def operations(a, b, operation):
    if operation == "+": return a + b
    if operation == "-": return a - b
    if operation == "*": return a * b


def max_value(example: str):
    numbers, signs = [int(number) for number in example[::2]], list(example[1::2])
    n = len(numbers)

    #таблицы для min и max значенинй
    max_matrix = [[float("-inf")] * n for _ in range(n)]
    min_matrix = [[float("inf")] * n for _ in range(n)]

    #выставляем на диаг.позиции сами числа т.к на подотрезок содержит само число
    for i in range(n):
        max_matrix[i][i] = min_matrix[i][i] = numbers[i]

    # теперь заполним для выражений где длина больше 1
    for length in range(1, n):  # длина подвыражения от 2 до n
        for i in range(n - length):
            j = i + length

            # для каждого возможного разбиения
            for k in range(i, j):
                op = signs[k]  # берем операцию
                #выполняются все возможные комбинации для нахождения в дальнейшем max и min
                a = operations(max_matrix[i][k], max_matrix[k + 1][j], op)
                b = operations(max_matrix[i][k], min_matrix[k + 1][j], op)
                c = operations(min_matrix[i][k], max_matrix[k + 1][j], op)
                d = operations(min_matrix[i][k], min_matrix[k + 1][j], op)

                max_val = max(a, b, c, d)
                min_val = min(a, b, c, d)

                if max_val > max_matrix[i][j]:
                    max_matrix[i][j] = max_val
                if min_val < min_matrix[i][j]:
                    min_matrix[i][j] = min_val

    return max_matrix[0][n - 1]

if __name__ == '__main__':
    @utils.measure_time_and_memory
    def task():
        lines = utils.read_input(input_path)
        result = max_value(lines[0])
        utils.write_output(output_path, result)


    task()
