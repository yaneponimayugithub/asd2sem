import os
import lab1.utils as utils

input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

def alisa_apple_eat(height:int,apples:list):
    sorted_apples = apples.copy()
    sorted_apples.sort(key=lambda apple_params: apple_params[1] - apple_params[0], reverse=True)   # сортируем в самом выгодном порядке
                                                                                            # чтобы максимально избежать неположительного роста
    order_apples = []
    print(apples)



    while len(order_apples) != len(apples):
        for idx in range(len(sorted_apples)):
            if height - sorted_apples[idx][0] > 0 and idx not in order_apples:
                height += sorted_apples[idx][1] - sorted_apples[idx][0]
                order_apples.append(apples.index(sorted_apples[idx]))
                break
        else: return -1
    return order_apples


def alisa_apple_eat(height: int, apples: list):
    sorted_apples = sorted(apples, key=lambda apple_params: apple_params[1] - apple_params[0], reverse=True)# сортируем в самом выгодном порядке
                                                                                            # чтобы максимально избежать неположительного роста

    order_apples = []  # хранение порядка яблок

    while sorted_apples:
        for idx, apple in enumerate(sorted_apples):
            decreasing, increasing = apple  # decreasing - уменьшение роста, increasing - увеличение роста

            # если рост останется положительным, то извлекаем яблоко
            if height - decreasing > 0:
                height += increasing - decreasing  # Сначала уменьшаем рост на decreasing, потом увеличиваем на increasing
                order_apples.append(apples.index(apple))  # добавим индекс из начального списка т.к. там порядок верный
                sorted_apples.pop(idx)  # извлекаем съеденное яблоко
                break
        else:
            # Если не удалось съесть яблоко в цикле, то значит невозможно съесть яблоки чтобы рост оставался положительным
            return -1

    # иначе возвращаем номера( начиная с 1 )
    return [idx+1 for idx in order_apples]


if __name__ == '__main__':
    @utils.measure_time_and_memory
    def task():
        lines = utils.read_input(input_path)
        height = int(lines[0].split()[1])
        apples = [list(map(int,apple.split())) for apple in lines[1::]]
        result = alisa_apple_eat(height,apples)
        if result == -1:
            utils.write_output(output_path, result)
        else:
            utils.write_output_list(output_path, result)


    task()
