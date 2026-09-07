import math

from calculator import calculate, format_number
from helpers import parse_natural_number


def build_kid_math_result(form):
    try:
        first_number = parse_natural_number(form.get("first_number", ""), "số thứ nhất")
        second_number = parse_natural_number(form.get("second_number", ""), "số thứ hai")
        answer = float(form.get("answer", "").strip())
    except ValueError as error:
        return None, str(error)

    operation = form.get("operation", "sum")
    try:
        result = calculate(first_number, second_number, operation)
    except ValueError:
        return None, "Vui lòng chọn phép toán hợp lệ."

    if isinstance(result, str):
        return None, result

    is_correct = math.isclose(answer, result, rel_tol=1e-9, abs_tol=1e-9)
    return {
        "correct": is_correct,
        "answer": format_number(answer),
        "correct_answer": format_number(result),
    }, None
