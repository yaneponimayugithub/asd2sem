import time
import os
import psutil
import inspect


def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 ** 2)


# ДЕКОРАТОР
def measure_time_and_memory(func):
    calling_file = inspect.getfile(func)
    absolute_path = os.path.abspath(calling_file)
    labnum, tasknum = absolute_path[absolute_path.find("lab") + 3], absolute_path[
                                                                    absolute_path.find("task") + 4:absolute_path.find(
                                                                        "src") - 1]
    task_name = absolute_path[absolute_path.find("src") + 4:]

    def wrapper(*args, **kwargs):
        initial_memory = get_memory_usage()
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        final_memory = get_memory_usage()
        print(f"continuation-------/ lab - {labnum} | task - {tasknum} /------------------")
        print(f"------------------ / {task_name} /-----------------------")
        print(f"Время выполнения: {end_time - start_time:.6f} секунд")
        print(f"Использование памяти: {final_memory - initial_memory:.8f} МБ")
        print(f"end----------------/ lab - {labnum} | task - {tasknum} /------------------\n\n")
        return result

    return wrapper


def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    numlab = file_path[file_path.find('lab') + 3]
    numtask = file_path[file_path.find('task') + 4:file_path.find('txtf') - 1]
    print(f'start--------------/ lab - {numlab} | task - {numtask} /------------------',
          'Входные данные:', sep='\n')
    for line in lines:
        print(f'{line}')
    return lines


def write_output_list(file_path, data):
    with open(file_path, 'w') as f:
        out = ' '.join(map(str, data))
        f.write(out)
        print(f'Выходные данные: \n{out}\n')


def write_output(file_path, data):
    with open(file_path, 'w') as f:
        out = str(data)
        f.write(out)
        print(f'Выходные данные: \n{out}\n')


def write_output_list_row(file_path, data):
    with open(file_path, 'w') as f:
        out = '\n'.join(map(str, data))
        f.write(out)
        print(f'Выходные данные: \n{out}\n')


def get_file_paths(path):
    current_script_dir = os.path.dirname(path)
    relative_path = os.path.join(current_script_dir, '..', 'txtf')

    input_path = os.path.abspath(relative_path + "/input.txt")
    output_path = os.path.abspath(relative_path + "/output.txt")

    return input_path, output_path
