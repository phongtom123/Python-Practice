import math

from calculator import format_number
from helpers import parse_positive_float


def build_circle_result(form):
    try:
        radius = parse_positive_float(form.get("radius", ""), "bán kính")
    except ValueError as error:
        return None, str(error)

    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return {
        "radius": format_number(radius),
        "area": format_number(area),
        "circumference": format_number(circumference),
    }, None
