import json


class FigureManagement:
    @staticmethod
    def save_data_to_a_file(path: str, data_figure: dict, class_name: str = '"не определено"'):
        with open(path, "w") as file:
            json.dump(data_figure, file)
            print(f"Данные фигуры класса {class_name} успешно сохранены в файл {path}")

    @staticmethod
    def read_data_to_a_file(path: str):
        with open(path, "r") as file:
            text = json.load(file)
            coord = text["Координаты"]
            text["Координаты"] = tuple(coord)
            print(f"Данные успешно считаны из файла {path}.")
            return text


