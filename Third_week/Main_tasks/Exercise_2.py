import csv

class CarBase:

    def __init__(self, brand, photo_file_name, carrying):

        # Проверим на правильность название фото-файла
        def test_photo_file_name(file_name):
            parts_file_name = file_name.split(".")

            # Если в названии файла больше одной точки ,или нет расширения - название файла неверно
            if len(parts_file_name) != 2:
                raise SyntaxError("Invalid photo file name")

            # Если расширения файла нет в списке по заданию - название файла неверно
            elif parts_file_name[1] != "jpg" and parts_file_name[1] != "jpeg" and parts_file_name[1] != "png" and \
                    parts_file_name[1] != "gif":
                raise SyntaxError("Invalid photo file name")
            else:
                return file_name

        self.car_type = None
        self.brand = brand
        self.photo_file_name = test_photo_file_name(photo_file_name)
        self.carrying = carrying

    # Метод, возвращающий расширение файла photo_file_name
    def get_photo_file_ext(self):
        exp = self.photo_file_name.split(".")
        extension = "." + exp[1]
        return extension


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying, car_type=None)
        self.car_type = "car"
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying, car_type=None)
        self.car_type = "truck"
        self.body_whl = body_whl

        # Передадим значения параметрам грузовика: длина, ширина, высота
        try:
            body = body_whl.split("x")
            self.body_length = float(body[0])
            self.body_width = float(body[1])
            self.body_height = float(body[2])
        except:
            self.body_length = 0
            self.body_width = 0
            self.body_height = 0

    # Найдем объём кузова
    def get_body_volume(self):
        volume = self.body_length * self.body_width * self.body_height
        return volume


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying, car_type=None)
        self.car_type = "spec_machine"
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, 'r') as file:
        lines = csv.reader(file, delimiter=';')


        for line_list in lines:

            if len(line_list) < 4:
                continue

            # Проверим, данные из файла на валидность
            match line_list[0]:
                case "car":
                    try:
                        car_list.append(Car(line_list[1], line_list[3], line_list[5], line_list[2]))
                    except:
                        pass
                case "truck":
                    try:
                        car_list.append(Truck(line_list[1], line_list[3], line_list[5], line_list[4]))
                    except:
                        pass
                case "spec_machine":
                    try:
                        car_list.append(SpecMachine(line_list[1], line_list[3], line_list[5], line_list[6]))
                    except:
                        pass

    return car_list

