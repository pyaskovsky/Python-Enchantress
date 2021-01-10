HOUSES = [
    {'area': 40, 'cost': 40000},
    {'area': 50, 'cost': 50000},
    {'area': 20, 'cost': 20000},
    {'area': 60, 'cost': 60000}
]


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.availability_money = 0
        self.has_home = []

    def info(self):
        has_own_home = 'Yes' if len(self.has_home) else 'No'

        print(f'''
Person information:
Name: {self.name}
Age: {self.age}
Availability of money: ${self.availability_money}
Having your own home: {has_own_home}
''')

    def earn_money(self, money):
        self.availability_money += money

    def buy_house(self):
        print('Choose home:')

        index = 1
        for home in HOUSES:
            print(f'{index}. Home with area: {home["area"]}m2 and cost: ${home["cost"]}')
            index += 1

        home_position = int(input("Home: "))

        home_area = HOUSES[home_position - 1]["area"]
        home_cost = HOUSES[home_position - 1]["cost"]

        if self.availability_money >= home_cost:
            print("You bought:")
            self.has_home.append(House(home_area, home_cost))
        else:
            print("Please earn more money")

    def show_available_houses(self):
        for home in self.has_home:
            area = home.area
            cost = home.cost

            home = House(area, cost)
            home.show_home_info()


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def show_home_info(self):
        small_home = 40
        price = self.cost
        discount = 15 if self.area > small_home else 0
        if discount > 0:
            price = int(price - (discount / 100) * price)

        print(f'Home with area: {self.area}m2 and cost: ${price} and your discount is {discount}%')


if __name__ == '__main__':
    human1 = Person("Ihor", 35)
    human1.earn_money(50000)
    human1.info()
    human1.buy_house()
    human1.show_available_houses()

    human2 = Person("Ivan", 30)
    human2.earn_money(600000)
    human2.info()
    human2.buy_house()
    human2.show_available_houses()
