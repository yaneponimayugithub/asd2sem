import os
import lab2.utils as utils

input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))


def count_palindromic_substrings(s):
    s = s.replace(' ', '')  # Удаляем пробелы
    n = len(s)
    if n < 3:
        return 0

    # Префиксные суммы для каждого символа
    prefix = [[0] * 26 for _ in range(n + 1)]  # prefix[i] — частоты до i-й позиции
    suffix = [[0] * 26 for _ in range(n + 1)]  # suffix[i] — частоты после i-й позиции

    # Заполняем префиксные суммы
    for i in range(n):
        for c in range(26):
            prefix[i + 1][c] = prefix[i][c]
        char = ord(s[i]) - ord('a')
        prefix[i + 1][char] += 1

    # Заполняем суффиксные суммы
    for i in range(n - 1, -1, -1):
        for c in range(26):
            suffix[i][c] = suffix[i + 1][c]
        char = ord(s[i]) - ord('a')
        suffix[i][char] += 1

    total = 0
    # Проходим по всем возможным средним символам (aba)
    for mid in range(1, n - 1):
        # Количество символов слева от mid (индексы 0..mid-1)
        left = [prefix[mid][c] for c in range(26)]
        # Количество символов справа от mid (индексы mid+1..n-1)
        right = [suffix[mid + 1][c] for c in range(26)]
        # Суммируем произведения частот
        for c in range(26):
            total += left[c] * right[c]

    return total

if __name__ == '__main__':
    @utils.measure_time_and_memory
    def task():
        lines = utils.read_input(input_path)
        result = count_palindromic_substrings(lines[0])
        utils.write_output(output_path,result)


    task()
