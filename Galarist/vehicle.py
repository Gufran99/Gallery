from utilities import get_valid_input

class Vehicle:
    def __init__(self, gasoline='', diesel='', *args, **kwargs):
        self.gasoline = gasoline
        self.diesel = diesel

    def display(self):
        print(f'Fuel İnformation\n'
              f'==================\n'
              f'Gasoline: {self.gasoline}\n'
              f'Diesal: {self.diesel}')

    def prompt_init():
        return dict(
            gasoline=get_valid_input('Gasoline: ',
                                     ('yes', 'no')),
            diesel=get_valid_input('Diesal: ',
                                   ('yes', 'no'))
        )

    prompt_init = staticmethod(prompt_init)
