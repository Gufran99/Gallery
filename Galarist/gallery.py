from purchase import CarPurchase, MotorcyclePurchase
from rental import CarRental, MotorcycleRental
from utilities import get_valid_input

class Gallery:
    def __init__(self):
        self.properties = []

    def displat_proparties(self):
        for i in self.properties:
            i.display()

    process_type = {
        ('car', 'rental'): CarRental,
        ('motorcycle', 'rental'): MotorcycleRental,
        ('car', 'purchase'): CarPurchase,
        ('motorcycle', 'purchase'): MotorcyclePurchase
    }

    def request_vehicle(self):
        property_type = get_valid_input(
            'What type of property do you wont?', ('car', 'motorcycle')
        )
        payment_type = get_valid_input(
            'What pyment type do you prefer?', ('purchase', 'rental')
        )

        property_class = self.process_type[(property_type, payment_type)]
        init_args = property_class.prompt_init()
        self.properties.append(property_class(**init_args))


gallery = Gallery()
gallery.request_vehicle()
gallery.displat_proparties()

