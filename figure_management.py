import json


class FigureManagement:
    @staticmethod
    def save_square_data_to_a_file(path: str, data_figure: dict):
        with open(path, "w") as file:
            json.dump(data_figure, file)
            print(f"Данные фигуры класса  успешно сохранены в файл {path}")

    @staticmethod
    def read_data_to_a_file(path: str):
        with open(path, "r") as file:
            text = json.load(file)
            print(f"Данные успешно считаны из файла {path}.")
            return text


