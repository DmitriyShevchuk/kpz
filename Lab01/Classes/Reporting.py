from pathlib import Path
import os
from datetime import datetime

from Lab01.configs.config import report_path
from Lab01.Classes.Product import Product

class Reporting:
    @staticmethod
    def __check_exists():
        if not os.path.exists(report_path):
            os.makedirs(report_path)

    @staticmethod
    def __get_index(name : str):
        Reporting.__check_exists()

        print(os.listdir(report_path))

        try:
            return max([int(item.split('.')[0].split('#')[1]) for item in os.listdir(report_path) if name in item]) + 1
        except ValueError:
            return 1

    @staticmethod
    def __create_file(name : str, text : str):
        with open(f'{report_path}{name}.txt', 'w') as file:
            file.write(text)

    @staticmethod
    def create_invoice(name : str, products : list, last_delivery : datetime):
        name_file = f'{name} #{Reporting.__get_index(name)}'
        text_file = (f'{name_file}\n\n'
                     f'{'\n'.join([str(product) for product in products])}\n'
                     f'Last delivery - {last_delivery}')

        Reporting.__create_file(name_file, text_file)