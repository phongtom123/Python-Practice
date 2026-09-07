from calculator import format_number


def calculate_rectangle(length, width):
    area = length * width
    perimeter = (length + width) * 2
    return area, perimeter


def build_rectangle_result(form):
    try:
        length = float(form.get("length", "").strip())
        width = float(form.get("width", "").strip())
    except ValueError:
        return None, "Vui lòng nhập đúng chiều dài và chiều rộng."

    if length <= 0 or width <= 0:
        return None, "Chiều dài và chiều rộng phải lớn hơn 0."

    area, perimeter = calculate_rectangle(length, width)
    return {
        "length": format_number(length),
        "width": format_number(width),
        "area": format_number(area),
        "perimeter": format_number(perimeter),
    }, None
