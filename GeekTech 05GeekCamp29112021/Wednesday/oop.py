
# Создаем класс Car
class Car:
    # создаем атрибуты класса
    name = "lada"
    model = "chetyrka"
    year = 1985

    # создаем методы класса
    def start(self):
        print("Заводим калымагу!")

    def drive(self):
        print("КАТИТСЯ!")

    def stop(self):
        print("ЗАГЛОХЛА!")

car1 = Car()

car1.start()
car1.drive()
car1.stop()
