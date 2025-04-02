import os
import lab4.utils as utils

input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))


def compute_prefix(pattern):
    """Вычисляет префикс-функцию для шаблона."""
    m = len(pattern)
    prefix = [0] * (m + 1)  # Создаем массив длиной m+1
    prefix[0] = -1  # Специальное значение для удобства
    i, j = 1, 0

    while i < m:
        if pattern[i] == pattern[j]:
            # Совпадение символов
            prefix[i + 1] = j + 1
            i += 1
            j += 1
        else:
            if j > 0:
                # Возвращаемся к предыдущему бордеру
                j = prefix[j]
            else:
                # Нет совпадений, переходим к следующему символу
                prefix[i + 1] = 0
                i += 1
    return prefix

def kmp_search(text, pattern):
    """Ищет все вхождения pattern в text с помощью алгоритма KMP."""
    n, m = len(text), len(pattern)
    if m == 0:
        return []

    prefix = compute_prefix(pattern)
    result = []
    i = j = 0  # Индексы для text и pattern

    while i < n:
        if text[i] == pattern[j]:
            # Совпадение символов
            i += 1
            j += 1
            if j == m:
                # Найдено вхождение
                result.append(i - j)
                # Сдвигаем j для поиска следующих вхождений
                j = prefix[j]
        else:
            # Несовпадение, используем префикс-функцию
            if j > 0:
                j = prefix[j]
            else:
                i += 1
    return [char+1 for char in result]

if __name__ == '__main__':
    @utils.measure_time_and_memory
    def task():
        lines = utils.read_input(input_path)
        result = [len(kmp_search(lines[1],lines[0])),kmp_search(lines[1],lines[0])]
        utils.write_output_list_row(output_path,result)


    task()