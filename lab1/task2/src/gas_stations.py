import os
import lab1.utils as utils

input_path, output_path = utils.get_file_paths(os.path.abspath(__file__))

def count_gas_stations(distance: int, distance_on_full_fuel: int, count_gas_stations: int, dist_gas_stations: list):
    dist_gas_stations.insert(0, 0)  # добавляем 0 чтобы сравнивать с начальной точкой

    if distance <= distance_on_full_fuel: return 0  # если можно доехать на полном баке без заправки

    if dist_gas_stations[-1] + distance_on_full_fuel < distance: return -1  # проверка на возможность проезда назначенной пути

    if count_gas_stations == 0 and distance > distance_on_full_fuel: return -1 # если заправок 0 и нельзя проехать на фулл баке
    numRefills = 0  # количество заправок
    current_gas_station = 0  # начальная станция

    while current_gas_station < count_gas_stations:
        last_gas_station = current_gas_station
        # ищем самую дальнюю заправку, до которой можно доехать
        # учитывается так же расстояние между заправками на полном баке
        while current_gas_station < count_gas_stations and dist_gas_stations[current_gas_station + 1] - dist_gas_stations[last_gas_station] <= distance_on_full_fuel:
            current_gas_station += 1

        # если не можем найти заправку, до которой можно доехать
        if current_gas_station == last_gas_station:
            return -1

        numRefills += 1  # увеличиваем количество заправок

        # если на текущей заправке можем доехать до цели
        if dist_gas_stations[current_gas_station] + distance_on_full_fuel >= distance:
            break

    return numRefills


if __name__ == '__main__':
    @utils.measure_time_and_memory
    def task():
        lines = utils.read_input(input_path)
        dist, max_dist_full_fuel, count_stations = int(lines[0]), int(lines[1]), int(lines[2])
        stations = list(map(int, lines[3].split()))
        result = count_gas_stations(dist, max_dist_full_fuel, count_stations, stations)
        utils.write_output(output_path, result)


    task()
