import os
import lab4.utils as utils

input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))


def decompose_string(s):
    n = len(s)
    if n == 0:
        return ""

    # Динамическое программирование: dp[i] = (min_length, components)
    dp = [(float('inf'), []) for _ in range(n + 1)]
    dp[0] = (0, [])

    for i in range(n):
        current_length, current_components = dp[i]
        if current_length == float('inf'):
            continue

        # Рассматриваем все возможные длины паттерна
        for l in range(1, n - i + 1):
            substr = s[i:i + l]
            max_k = 1

            # Находим максимальное количество повторений
            for k in range(2, (n - i) // l + 1):
                if s[i:i + l * k] == substr * k:
                    max_k = k
                else:
                    break

            # Перебираем все возможные k от 1 до max_k
            for k in range(1, max_k + 1):
                end = i + l * k
                if end > n:
                    break

                # Формируем компонент
                if k == 1:
                    component = substr
                else:
                    component = f"{substr}*{k}"

                # Обновляем dp[end]
                new_length = current_length + len(component)
                if i > 0:
                    new_length += 1  # Добавляем "+"

                if new_length < dp[end][0]:
                    new_components = current_components.copy()
                    if i > 0:
                        new_components.append("+")
                    new_components.append(component)
                    dp[end] = (new_length, new_components)

    # Сбор ответа
    min_length, components = dp[n]
    return ''.join(components)

if __name__ == '__main__':
    @utils.measure_time_and_memory
    def task():
        lines = utils.read_input(input_path)
        print(lines[0])
        result = decompose_string(lines[0])
        utils.write_output(output_path,result)


    task()