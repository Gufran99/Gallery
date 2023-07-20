def get_valid_input(input_quastion: str, valid_options: tuple):
    input_quastion += "({})".format(",".join(valid_options))

    response = input(input_quastion)

    while response.lower() not in valid_options:
        print('Plase type into valid options..!')
        response = input(input_quastion)

    return response
