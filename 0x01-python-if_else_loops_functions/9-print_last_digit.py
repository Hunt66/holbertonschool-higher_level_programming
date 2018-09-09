#!/ust/bin/python3

def print_last_digit(number):
    number = abs(number)
    number = number % 10
    print(number, end='')
    return number
