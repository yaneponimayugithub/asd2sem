import os
import lab1.utils as utils

input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

def count_gas_stations(distance: int, distance_on_full_fuel: int, count_gas_stations: int, dist_gas_stations: list):
    dist_gas_stations.insert(0, 0)  # добавляем 0 чтобы сравнивать с начальной точки

    if distance <= distance_on_full_fuel: return 0  # если можно доехать на полном баке без заправки

    if dist_gas_stations[-1] + distance_on_full_fuel < distance: return -1  # проверка на возможность проезда назначенной пути

    stations = []  # посещенные станции
    current_gas_station = 0  # начальная станция

    while current_gas_station < count_gas_stations:
        next_gas_station = current_gas_station
        # ищем самую дальнюю заправку до которой можно доехать
        for current_idx in range(current_gas_station + 1, count_gas_stations + 1):
            if dist_gas_stations[current_idx] - dist_gas_stations[current_gas_station] <= distance_on_full_fuel:
                next_gas_station = current_idx  # обновляем индекс заправки
            else:
                break  # если не хватит бенз, то прерываем цикл и изменение след.станции

        # проверка на то, что ближайшая заправка не дальше чем distance_on_full_fuel
        if next_gas_station == current_gas_station: return -1

        stations.append(dist_gas_stations[next_gas_station])  # добавим заправку в список посещенныъ
        current_gas_station = next_gas_station  # обновляем текущую заправку

        # проверка хватит ли бенз чтобы доехать без заправок
        if dist_gas_stations[current_gas_station] + distance_on_full_fuel >= distance: break

    return len(stations)

if __name__ == '__main__':
    @utils.measure_time_and_memory
    def task():
        lines = utils.read_input(input_path)
        dist, max_dist_full_fuel, count_stations = int(lines[0]), int(lines[1]), int(lines[2])
        stations = list(map(int, lines[3].split()))
        result = count_gas_stations(dist, max_dist_full_fuel, count_stations, stations)
        utils.write_output(output_path, result)


    task()
