CALCULATOR_OPERATIONS = {
    "sum": ("Tổng", "Tổng", "+"),
    "diff": ("Hiệu", "Hiệu", "-"),
    "product": ("Tích", "Tích", "*"),
    "quotient": ("Thương", "Thương", "/"),
}

# Tên cũ giúp các file đang import OPERATIONS vẫn chạy bình thường.
OPERATIONS = CALCULATOR_OPERATIONS


def format_number(value):
    if isinstance(value, str):
        return value
    if value == int(value):
        return str(int(value))
    return f"{value:.6f}".rstrip("0").rstrip(".")


def calculate(first_number, second_number, operation):
    if operation == "sum":
        return first_number + second_number
    if operation == "diff":
        return first_number - second_number
    if operation == "product":
        return first_number * second_number
    if operation == "quotient":
        if second_number == 0:
            return "Không thể chia cho 0"
        return first_number / second_number
    raise ValueError("Phép tính không hợp lệ")


def build_result(form):
    try:
        first_number = float(form.get("first_number", "").strip())
        second_number = float(form.get("second_number", "").strip())
    except ValueError:
        return None, "Vui lòng nhập đúng 2 số."

    operation = form.get("operation", "sum")
    if operation not in CALCULATOR_OPERATIONS:
        return None, "Vui lòng chọn phép tính hợp lệ."

    result = calculate(first_number, second_number, operation)
    label, _, symbol = CALCULATOR_OPERATIONS[operation]
    expression = (
        f"{format_number(first_number)} {symbol} "
        f"{format_number(second_number)} = {format_number(result)}"
    )
    return {"label": label, "expression": expression}, None
