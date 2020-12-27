class Laptop:
    def __init__(self):
        hardware1 = Hardware('Memory is 16GB')
        hardware2 = Hardware('SSD is 512GB')
        self.hardware = [hardware1, hardware2]

    def print_configuration(self):
        print(self.hardware)
        for hardware in self.hardware:
            print(hardware.description)


class Hardware:
    def __init__(self, description):
        self.description = description


laptop = Laptop()
laptop.print_configuration()

