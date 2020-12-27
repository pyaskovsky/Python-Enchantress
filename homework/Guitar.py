class Guitar:
    def __init__(self, g_type):
        self.g_type = g_type

    def connect(self):
        print(f'The guitar is {self.g_type.guitar_type} and connected to acoustic system')


class Guitar_type:
    def __init__(self, guitar_type):
        self.guitar_type = guitar_type


g_type = Guitar_type('acoustic')
guitar = Guitar(g_type)
guitar.connect()





