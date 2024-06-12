import json
import datetime from datetime

def load_operations():
    """
    Чтение json файла с  операциями, совершенных клиентом банка
    """

    with open('operations.json', encoding='utf-8') as file:
        return json.load(file)


def mask_cart_number(cart_number):
    """
    Макскирует номер карты и не отображает целиком в формате XXXX XX** **** XXXX
    (видны первые 6 цифр и последние 4  разбито по блокам по 4 цифры, разделенных пробелом).
    """

    return f'{cart_number[:-12]} {cart_number[-12:-10]}** **** {cart_number[-4:]}'

def mask_acc(acc_number):
    """
    Макскирует номер счета и не отображает целиком в формате  **XXXX
    (видны только последние 4 цифры номера счета).
    """

    return f'**{acc_number[-4:]}'

def get_operations(operations):
    """
    Фильтрует, сортирует и выводит последние пять выполненных (EXECUTED) операци.
    Переводит дату в формат ДД.ММ.ГГГГ.
    """

    pass

