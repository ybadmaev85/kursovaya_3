import json
from datetime import datetime



def read_file(path):
    """"Выгружает json файл"""
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def sort_state(date):
    """ последние 5 выполненных операций"""
    new_operations = []
    for el in date:
        if  el['state'] == "EXECUTED":
            new_operations.append(el)
            if len(new_operations) == 5:
                break
    return new_operations

def sort_5_operatons(data):
    """
    Берем 5 последних операция и фильтруем по дате
    """
    items = data
    items.sort(key=lambda x: x.get('date'), reverse=True)
    return items

def masked_number(operation):
    """
    маскирует номер
    """
    number = operation.split()[-1]
    if len(number) == 16:
        musk_count = number[:4] + " " + number[4:6] + "** ****" + number[-4:]
        return ' '.join(operation.split()[:-1]) + ' ' + musk_count
    else:
        musk_count = "**" + number[-4:]
        return ' '.join(operation.split()[:-1]) + ' ' + musk_count

def change_date(self):
    """
    метод изменяет дату в нужном формате
    """
    date_from_str = datetime.strptime(self, '%Y-%m-%dT%H:%M:%S.%f')
    return date_from_str.strftime('%d.%m.%Y')
