import requests

import all_data_for_testing as data

url = 'http://127.0.0.1:8000/get_form'


def get_form(url, *data):
    """Отправляем тестовые данные и получаем результат"""
    res = []
    for item in data:
        try:
            response = requests.post(url, data=item)
            res.append(response.json())
        except ValueError:
            return 'Указанные данные не прошли валидацию!!'
    return res


print('# Указанны верные данные:\n', get_form(url, data.data_1, data.data_2))
print('# Верные данные + доп значения\n', get_form(url, data.data_3))
print('# Неверные данные с верными типами\n', get_form(url, data.data_4))
print('# Данные неправильного формата и типа\n', get_form(url, data.data_5))
