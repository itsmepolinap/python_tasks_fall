import decimal
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '\n'


def read_file(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_employees_info() -> list[str]:
    """Внешнее апи, которое возвращает вам список строк с данными по сотрудникам."""
    return read_file(os.path.join(
        BASE_DIR, '1_task', 'input_data.txt',
    )).split(SPLIT_SYMBOL)


def get_parsed_employees_info() -> list[dict[str, int | str]]:
    """Функция парсит данные, полученные из внешнего API и приводит их к стандартизированному виду."""
    employees_info = get_employees_info()
    parsed_employees_info = []
    for emp in employees_info:
        employee_card = {}
        emp = emp.split()
        keys_list = emp[::2]
        values_list = emp[1::2]
        for key, value in zip(keys_list, values_list):
            #id:int, name, last_name, age:int, salary:decimal, position
            if key in ["id", "age"]:
                employee_card[key] = int(value)
            elif key == "salary":
                employee_card[key] = decimal.Decimal(value)
            elif key in ["name", "last_name", "position"]:
                employee_card[key] = value

        parsed_employees_info.append(employee_card)
    

    # Ваш код ниже
    return parsed_employees_info

