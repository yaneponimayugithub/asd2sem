import os
import lab1.utils as utils

input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))


def max_cost_items(n, W, items):
    items.sort(key=lambda item_params: float('inf') if item_params[1] == 0 else item_params[0] / item_params[1], reverse=True)   # сортировка по убыванию ценности, если вес = 0, то присвоим inf

    finish_cost = 0.0  # окончательная стоимость
    for value, weight in items:
        if W == 0:
            break
        if weight <= W:
            # Если весь предмет помещается в рюкзак
            W -= weight
            finish_cost += value
        else:
            # Если можем взять только часть предмета
            finish_cost += value * (W / weight)
            W = 0

    return finish_cost

if __name__ == '__main__':
    @utils.measure_time_and_memory
    def task():
        lines = utils.read_input(input_path)
        n, W = map(int, lines[0].split())
        items = [list(map(int, line.split())) for line in lines[1:]]
        result = max_cost_items(n, W, items)
        utils.write_output(output_path, result)


    task()
