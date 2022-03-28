import re
import random

regressive_numbers = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

def validator(cnpj):
    '''
        Validate  a random CNPJ number (Mathematicaly)

        Parameters: cnpj

        Return: return boolean value
    '''

    cnpj = regex_cnpj(cnpj)

    try:
        if is_sequence(cnpj):
            return False
    except Exception as error:
        return False

    try:
        new_cnpj = calc_digit(cnpj=cnpj,digit=1)
        new_cnpj = calc_digit(cnpj=new_cnpj,digit=2)
    except Exception as error:
        return False

    if new_cnpj == cnpj:
        return True
    else:
        return False

def calc_digit(cnpj, digit):
    '''
        Get cnpj and calculate digits

        Parameters: cnpj and digit to calculate first or second digit

        Return: return new cnpj with digit
    '''

    if digit == 1:
        regressive = regressive_numbers[1:]
        new_cnpj = cnpj[:-2]
    elif digit == 2:
        regressive = regressive_numbers
        new_cnpj = cnpj
    else:
        regressive = None

    total = 0

    for index,regressive in enumerate(regressive):
        total += int(cnpj[index]) * regressive


    digit = 11 - (total % 11)
    digit = digit if digit <= 9 else 0

    return f'{new_cnpj}{digit}'

def is_sequence(cnpj):
    '''
        Get cnpj and check if is not a sequence

        Parameters: cnpj

        Return: return a boolean value
    '''

    sequence = cnpj[0] * len(cnpj)
    if sequence == cnpj:
        return True
    else:
        return False

def regex_cnpj(cnpj):
    '''
        Get cnpj and remove any symbol

        Parameters: cnpj

        Return: return a CNPJ without - and /
    '''
    return re.sub(r'[^0-9]', '', cnpj)

def generate():
    '''
        Generate a cnpj

        Parameters:

        Return: return a generated CNPJ without symbols - and /
    '''

    first_digit = random.randint(0, 9)
    second_digit = random.randint(0, 9)
    first_block = random.randint(100, 999)
    second_block = random.randint(100, 999)
    third_block = '0001'

    initial_cnpj = f'{first_digit}{second_digit}{first_block}{second_block}{third_block}00'

    new_cnpj = calc_digit(cnpj=initial_cnpj, digit=1)
    new_cnpj = calc_digit(cnpj=new_cnpj, digit=2)

    return new_cnpj

def cnpj_format(cnpj):
    '''
        Format a CNPJ with - and / symbols

        Parameters: cnpj

        Return: return a generated CNPJ with - and /
    '''

    cnpj = regex_cnpj(cnpj)
    cnpj_new_format = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'
    return cnpj_new_format
