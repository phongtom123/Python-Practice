from helpers import parse_natural_number


def build_even_odd_result(form):
    try:
        number = parse_natural_number(form.get("number", ""))
    except ValueError as error:
        return None, str(error)

    kind = "chẵn" if number % 2 == 0 else "lẻ"
    return {"number": number, "kind": kind}, None
