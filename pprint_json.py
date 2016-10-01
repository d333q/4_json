import json
from pprint import pprint
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as json_content:
        return json.load(json_content)


def pretty_print_json(filepath):
    return pprint(data)


if __name__ == '__main__':
    data = load_data(input(
        'Введите название файла со списком московских алкогольных магазинов '))
    pretty_print_json(data)
