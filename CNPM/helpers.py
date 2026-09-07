def parse_positive_float(value, field_name):
    try:
        number = float(value.strip())
    except ValueError:
        raise ValueError(f"Vui lòng nhập đúng {field_name}.")
    if number <= 0:
        raise ValueError(f"{field_name.capitalize()} phải lớn hơn 0.")
    return number


def parse_natural_number(value, field_name="số tự nhiên n"):
    try:
        number = int(value.strip())
    except ValueError:
        raise ValueError(f"Vui lòng nhập đúng {field_name}.")
    if number < 0:
        raise ValueError(f"{field_name.capitalize()} phải lớn hơn hoặc bằng 0.")
    return number


def normalize_spaces(value):
    return " ".join(value.split())
