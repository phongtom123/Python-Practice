import re

from helpers import parse_natural_number
from prime import is_prime


def parse_integer_array(raw_values):
    values = re.split(r"[\s,;]+", raw_values.strip())
    values = [value for value in values if value]
    if not values:
        raise ValueError("Vui lòng nhập các phần tử của mảng.")

    try:
        return [int(value) for value in values]
    except ValueError:
        raise ValueError("Mảng chỉ được chứa các số nguyên.")


def validate_array_size(form, values):
    raw_size = form.get("size", "").strip()
    if not raw_size:
        return None

    size = parse_natural_number(raw_size, "N")
    if size != len(values):
        return f"Bạn nhập N = {size}, nhưng mảng có {len(values)} phần tử."
    return None


def build_array_result(form):
    try:
        values = parse_integer_array(form.get("values", ""))
        size_error = validate_array_size(form, values)
        if size_error:
            return None, size_error
    except ValueError as error:
        return None, str(error)

    mode = form.get("mode", "all")
    result_values = list(values)
    label = "Các phần tử của mảng"
    extra = ""

    if mode == "all":
        pass
    elif mode == "even":
        label = "Các phần tử chẵn của mảng"
        result_values = [value for value in values if value % 2 == 0]
    elif mode == "odd":
        label = "Các phần tử lẻ của mảng"
        result_values = [value for value in values if value % 2 != 0]
    elif mode == "prime":
        label = "Các phần tử là số nguyên tố của mảng"
        result_values = [value for value in values if is_prime(value)]
    elif mode == "add":
        try:
            new_value = int(form.get("new_value", "").strip())
        except ValueError:
            return None, "Vui lòng nhập phần tử mới là số nguyên."
        result_values = values + [new_value]
        label = "Mảng sau khi thêm phần tử mới"
    elif mode == "delete":
        try:
            index = parse_natural_number(form.get("index", ""), "vị trí k")
        except ValueError as error:
            return None, str(error)
        if index < 1 or index > len(values):
            return None, "Vị trí k phải nằm trong mảng."
        result_values = values[: index - 1] + values[index:]
        label = f"Mảng sau khi xóa phần tử thứ {index}"
    elif mode == "search":
        try:
            target = int(form.get("target", "").strip())
        except ValueError:
            return None, "Vui lòng nhập x là số nguyên."
        positions = [index + 1 for index, value in enumerate(values) if value == target]
        result_values = values
        label = f"Tìm số {target} trong mảng"
        extra = (
            f"Tìm thấy tại vị trí: {', '.join(map(str, positions))}"
            if positions
            else "Không tìm thấy x trong mảng."
        )
    else:
        return None, "Vui lòng chọn yêu cầu hợp lệ."

    return {
        "label": label,
        "values": result_values,
        "total": sum(result_values),
        "extra": extra,
    }, None
