class Transport:
    def __init__(self, the_model, the_year, the_color):
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        self.color = new_color

class Car(Transport):
    numbers_of_wheels = 4
    counter = 0

    def __init__(self, the_model, the_year, the_color, penalties=0):  # constructor
        # object attributes / fields
        super().__init__(the_model, the_year, the_color)
        self.penalties = penalties
        Car.counter += 1

    # method
    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')


class Truck(Car):
    numbers_of_wheels = 10
    def __init__(self, the_model, the_year, the_color, penalties=0, load_capacity=0):
        super().__init__(the_model, the_year, the_color, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, type, weight):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity} kg')
        else:
            print(f'Cargo of {type} {weight} kg was successfully loaded on {self.model}')


class Plane(Transport):
    def __init__(self, the_model, the_year, the_color):
        super().__init__(the_model, the_year, the_color)


bmw_car = Car('BMW X7', 2020, 'Red')
print(bmw_car)
print(f'Model: {bmw_car.model} year: {bmw_car.year} color: {bmw_car.color} '
      f'penalties: {bmw_car.penalties}')

nissan_car = Car(the_year=2021, the_color='Blue', the_model='Nissan Skyline', penalties=1000)
print(f'Model: {nissan_car.model} year: {nissan_car.year} color: {nissan_car.color} '
      f'penalties: {nissan_car.penalties}')
nissan_car.drive('Osh')
bmw_car.drive('Bishkek')

# nissan_car.color = 'Yellow'
nissan_car.change_color('Yellow')
print(f'Model: {nissan_car.model} year: {nissan_car.year} color: {nissan_car.color} '
      f'penalties: {nissan_car.penalties}')

print(f'We need {Car.numbers_of_wheels * 10 * 5000} soms for winter lastics')
Car.numbers_of_wheels = 5
print(f'We need {Car.numbers_of_wheels * 10 * 5000} soms for winter lastics')

print(f'Was contructed {Car.counter} cars')

boeing_plane = Plane('Boening 737', 2022, 'White')
print(f'Model: {boeing_plane.model} year: {boeing_plane.year} color: {boeing_plane.color}')

kamaz_truck = Truck('Kamaz 12', 2009, 'Green', 1500, 35000)
print(f'Model: {kamaz_truck.model} year: {kamaz_truck.year} color: {kamaz_truck.color} '
      f'penalties: {kamaz_truck.penalties} load capacity: {kamaz_truck.load_capacity} kg')
kamaz_truck.load_cargo('Apples', 40000)
kamaz_truck.load_cargo('Tomatoes', 30000)
kamaz_truck.drive('Naryn')

print(f'{Truck.numbers_of_wheels}')