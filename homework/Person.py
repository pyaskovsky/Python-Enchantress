from abc import ABC, abstractmethod

HOUSES = [
    {'area': 40, 'cost': 40000},
    {'area': 50, 'cost': 50000},
    {'area': 20, 'cost': 20000},
    {'area': 60, 'cost': 60000}
]


class House:
    def __init__(self, area: int, cost: int):
        self.area = area
        self.cost = cost

    def show_home_info(self):
        print(f'Home with area: {self.area}m2 and cost: ${self.cost}')


class Human(ABC):
    @abstractmethod
    def info(self):
        raise NotImplemented('No data to display.')

    @abstractmethod
    def earn_money(self, money: int):
        raise NotImplemented("I haven't money.")

    @abstractmethod
    def buy_house(self):
        raise NotImplemented("Choose house")


class Person(Human):
    def __init__(self, name, age, has_home):
        self.name = name
        self.age = age
        self.availability_money = 0
        self.has_home = has_home

    def info(self):
        print(f'''
Person information:
Name: {self.name}
Age: {self.age}
Availability of money: ${self.availability_money}
Having your own home: {self.has_home}
''')

    def earn_money(self, money):
        self.availability_money += money

    @staticmethod
    def apply_discount(house: House) -> None:
        small_home = 40
        price = house.cost
        discount = 15 if house.area > small_home else 0
        if discount > 0:
            price = int(price - (discount / 100) * price)
        print(f'Home with area: {house.area}m2 and cost: ${price} and your discount is {discount}%')

    def buy_house(self):
        print('Choose home:')

        index = 1
        for home in HOUSES:
            print(f'{index}. Home with area: {home["area"]}m2 and cost: ${home["cost"]}')
            index += 1

        home_position = int(input("Home: "))

        house = HOUSES[home_position - 1]
        home_area = house["area"]
        home_cost = house["cost"]

        if self.availability_money >= home_cost:
            self.has_home = True
            print("You bought:")

            self.apply_discount(House(home_area, home_cost))
        else:
            print("Please earn more money")


if __name__ == '__main__':
    human1 = Person("Ihor", 35, True)
    human1.earn_money(50000)
    human1.info()
    human1.buy_house()

    human2 = Person("Ivan", 30, False)
    human2.earn_money(600000)
    human2.info()
    human2.buy_house()
