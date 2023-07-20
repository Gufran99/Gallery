from vehicle import Vehicle
from utilities import get_valid_input

class Car(Vehicle):
    def __init__(self, brand='', model='', doors_number='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.brand = brand
        self.model = model
        self.doors_number = doors_number

    def display(self):
        super().display()
        print(f'Brand: {self.brand}\n'
              f'Model: {self.model}\n'
              f'Number of Doors: {self.doors_number}')

    def prompt_init():
        buyer_init = Vehicle.prompt_init()

        brand = input('Which brand do you want? ')
        model = input('Which model do you want? ')
        doors_number = get_valid_input(
            'How many doors do you want? ',
            ('2', '4')
        )

        return buyer_init

    prompt_init = staticmethod(prompt_init)
