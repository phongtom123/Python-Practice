import math

from helpers import parse_natural_number


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    limit = int(math.sqrt(number)) + 1
    for divisor in range(3, limit, 2):
        if number % divisor == 0:
            return False
    return True


def build_prime_check_result(form):
    try:
        number = parse_natural_number(form.get("number", ""))
    except ValueError as error:
        return None, str(error)

    return {"number": number, "is_prime": is_prime(number)}, None
