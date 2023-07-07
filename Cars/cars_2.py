import random


class Car:
    def __init__(self, brand, model, color, economy):
        self.mileage = 0
        self.fuel = 100
        self.brand = brand
        self.model = model
        self.color = color
        self.economy = economy
        self.fuel_consumed = 0

    def drive(self, distance):
        fuel_needed = distance / 100 * self.economy
        if fuel_needed <= self.fuel:
            self.mileage += distance
            self.fuel -= fuel_needed
            self.fuel_consumed += fuel_needed
            print(f"Автомобіль {self.brand} {self.model} ({self.color}) проїхав {distance} км.")
        else:
            print("Недостатньо палива для завершення поїздки.")

    def distance_left(self):
        return self.fuel / self.economy * 100

    def fuel_up(self):
        self.fuel = min(self.fuel + 20, 100)  # Запас палива не перевищує 100%
        print(f"Автомобіль {self.brand} {self.model} ({self.color}) заправився.")


def generate_random_cars(num_cars):
    brands = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
    toyota_models = ["Corolla", "Camry"]
    honda_models = ["Accord", "Civic"]
    ford_models = ["Fiesta", "Focus"]
    chevrolet_models = ["Aveo", "Lacetti"]
    nissan_models = ["Juke", "Note"]
    colors = ["Червоний", "Синій", "Зелений", "Жовтий"]
    cars = []
    for _ in range(num_cars):
        brand = random.choice(brands)
        if brand == "Toyota":
            model = random.choice(toyota_models)
        elif brand == "Honda":
            model = random.choice(honda_models)
        elif brand == "Ford":
            model = random.choice(ford_models)
        elif brand == "Chevrolet":
            model = random.choice(chevrolet_models)
        elif brand == "Nissan":
            model = random.choice(nissan_models)
        color = random.choice(colors)
        economy = random.uniform(5, 15)
        car = Car(brand, model, color, economy)
        cars.append(car)
    return cars


def drive_and_refuel(auto, distance1, distance2):
    for car in auto:
        car.drive(distance1)
        car.fuel_up()
        car.drive(distance2)
        print(f"Автомобіль {car.brand} {car.model} ({car.color}) завершив свій маршрут.")
        fuel_consumption = (distance1 / car.economy + distance2 / car.economy) / (distance1 + distance2) * 100
        print(f"Витрати палива: {fuel_consumption:.2f} л/100км")
        print(f"Загальна кількість витраченого палива: {car.fuel_consumed:.2f} л\n")


def find_car_with_most_fuel(cars):
    car_with_most_fuel = max(cars, key=lambda car: car.fuel)
    return car_with_most_fuel


def find_car_with_least_fuel(cars):
    car_with_least_fuel = min(cars, key=lambda car: car.fuel)
    return car_with_least_fuel


def print_car_description(car):
    print(f"Автомобіль:")
    print(f"Бренд: {car.brand}")
    print(f"Модель: {car.model}")
    print(f"Колір: {car.color}")
    print(f"Залишок палива: {car.fuel:.2f}л")


# Генерація 10 випадкових машин
cars = generate_random_cars(10)

# Проїзд, дозаправка та ще проїзд для кожної машини
drive_and_refuel(cars, 200, 100)

# Знаходження машини з найбільшим та найменшим запасом палива
car_with_most_fuel = find_car_with_most_fuel(cars)
car_with_least_fuel = find_car_with_least_fuel(cars)

# Виведення опису машини з найбільшим запасом
print("Автомобіль з найбільшим запасом палива:")
print_car_description(car_with_most_fuel)

# Виведення опису машини з найменшим запасом
print("Автомобіль з найменшим запасом палива:")
print_car_description(car_with_least_fuel)













