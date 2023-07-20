from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle

class Purchase(Vehicle):
    def __init__(self, price='', taxes='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print(f'Purchase Detail\n'
              f'================\n'
              f'SellingPrice: {self.price}\n'
              f'Taxes: {self.taxes}')

    def prompt_init():
        return dict(
            price=input('What is the selling price: '),
            taxes=input('What is the estimaed taxes: ')
        )

    prompt_init = staticmethod(prompt_init)

class CarPurchase(Car, Purchase):
    def prompt_init():
        init = Car.prompt_init()
        init.update(Purchase.prompt_init())

        return init

    prompt_init = staticmethod(prompt_init)


class MotorcyclePurchase(Motorcycle, Purchase):
    def prompt_init():
        init = Motorcycle.prompt_init()
        init.update(Purchase.prompt_init())

        return init

    prompt_init = staticmethod(prompt_init)