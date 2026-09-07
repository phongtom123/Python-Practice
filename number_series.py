from helpers import parse_natural_number
from prime import is_prime


def first_primes(count):
    primes = []
    candidate = 2
    while len(primes) < count:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes


def build_number_list_result(form):
    try:
        number = parse_natural_number(form.get("number", ""))
    except ValueError as error:
        return None, str(error)

    mode = form.get("mode", "all")
    values = list(range(1, number + 1))

    if mode == "all":
        label = f"Các số tự nhiên <= {number}"
        selected = values
    elif mode == "even":
        label = f"Các số tự nhiên chẵn <= {number}"
        selected = [value for value in values if value % 2 == 0]
    elif mode == "odd":
        label = f"Các số tự nhiên lẻ <= {number}"
        selected = [value for value in values if value % 2 != 0]
    elif mode == "prime":
        label = f"Các số nguyên tố <= {number}"
        selected = [value for value in values if is_prime(value)]
    elif mode == "first_primes":
        label = f"{number} số nguyên tố đầu tiên"
        selected = first_primes(number)
    else:
        return None, "Vui lòng chọn yêu cầu hợp lệ."

    return {
        "label": label,
        "values": selected,
        "total": sum(selected),
    }, None
