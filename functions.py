import os
import re
from typing import Iterable

from werkzeug.exceptions import BadRequest

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def do_cmd(cmd: str, value: str, data: list[str]) -> list[str]:
    """ Обрабатывает запрос с командами """
    if cmd == 'filter':
        result = list(filter(lambda line: value in line, data))
    elif cmd == 'map':
        result = list(map(lambda line: line.split()[int(value)], data))
    elif cmd == 'unique':
        result = list(set(data))
    elif cmd == 'sort':
        reverse = (value == 'desc')
        result = sorted(data, reverse=reverse)
    elif cmd == 'limit':
        result = data[:int(value)]
    elif cmd == 'regex':
        regex = re.compile(value)
        result = list(filter(lambda v: regex.search(v), data))
    else:
        raise BadRequest
    return result


def do_query(params: dict) -> Iterable:
    """ Считывает файл и возвращает обработанный результат """
    with open(os.path.join(DATA_DIR, params['file_name'])) as f:
        file_data = f.readlines()  # f.read().split('\n')
    result = file_data
    if "cmd1" in params.keys():
        result = do_cmd(params['cmd1'], params['value1'], result)
    if "cmd2" in params.keys():
        result = do_cmd(params['cmd2'], params['value2'], result)
    return result
