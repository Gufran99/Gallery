from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
from utilities import get_valid_input

class Rental(Vehicle):
    def __init__(self, rent='', duration='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.duration = duration
        self.rent = rent

    def display(self):
        super().display()
        print(f'Rent Detail\n'
              f'============\n'
              f'Rent: {self.rent}\n'
              f'Rental Period: {self.duration}')

    def prompt_init():
        return dict(
            rent=input('What is the estimated montly rent?'),
            duration=get_valid_input(
                'How many days? ',
                ('1', '2', '3', '5', '7')
            )
        )

class CarRental(Car, Rental):
    def prompt_init():
        init = Car.prompt_init()
        init.update(Rental.prompt_init())

        return init

    prompt_init = staticmethod(prompt_init)


class MotorcycleRental(Motorcycle, Rental):
    def prompt_init():
        init = Motorcycle.prompt_init()
        init.update(Rental.prompt_init())

        return init

    prompt_init = staticmethod(prompt_init)
    