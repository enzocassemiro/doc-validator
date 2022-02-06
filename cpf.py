from random import randint

def check_cfp(cpf: str) -> list:
    '''
        Return True or False to a CPF validation

        Parameters:
            cpf (str): Input in HTML page

        Returns:
            A list with True or False and new_cpf(str) if cpf is valid
            True: If cpf is valid, and return new_cpf
            False: If cpf is not valid
    '''
    new_cpf = cpf[:9]
    reverse = 10
    total_digit = 0

    for index in range(19):
        if index > 8:
            index -= 9

        try:
            int(cpf)
            if len(cpf) < 11:
                return [False, '']
        except:
            return [False, '']

        total_digit += int(new_cpf[index]) * reverse

        reverse -= 1
        if reverse < 2:
            reverse = 11
            first_digit = 11 - (total_digit % 11)

            if first_digit > 9:
                first_digit = 0

            total_digit = 0
            new_cpf += str(first_digit)

    sequence = new_cpf == str(new_cpf[0]) * len(cpf)

    if cpf==new_cpf and not sequence:
        return [True, new_cpf]
    else:
        return [False, '']

def generate_cpf():
    '''
        Generate a random CPF number (Mathematicaly)

        Parameters:

        Return:
            return a list with True argument and CPF generated
    '''

    random_number = str(randint(100000000,999999999))

    new_cpf = random_number[:9]
    reverse = 10
    total_digit = 0

    for index in range(19):
        if index > 8:
            index -= 9

        total_digit += int(new_cpf[index]) * reverse

        reverse -= 1
        if reverse < 2:
            reverse = 11
            first_digit = 11 - (total_digit % 11)

            if first_digit > 9:
                first_digit = 0

            total_digit = 0
            new_cpf += str(first_digit)

    return [True, new_cpf]
