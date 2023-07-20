from vehicle import Vehicle
from utilities import get_valid_input

class Motorcycle(Vehicle):
    def __init__(self, brand='', model='', cc='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.brand = brand
        self.model = model
        self.cc = cc

    def display(self):
        super().display()
        print(f'Brand: {self.brand}\n'
              f'Model: {self.model}\n'
              f'CC: {self.cc}')

    def prompt_init():
        buyer_init = Vehicle.prompt_init()

        brand = input('Which brand do you want? ')
        model = input('Which model do you want? ')
        cc = get_valid_input(
            'What is your engine cc power? ',
            ('125', '200', '300', '500')
        )

        return buyer_init

    prompt_init = staticmethod(prompt_init)
    