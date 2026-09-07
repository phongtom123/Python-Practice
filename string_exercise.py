from helpers import normalize_spaces, parse_natural_number


def build_string_result(form):
    text = form.get("text", "")
    mode = form.get("mode", "length")

    if mode == "length":
        return {"label": "Độ dài của chuỗi", "lines": [str(len(text))]}, None
    if mode == "trim":
        return {"label": "Chuỗi sau khi xóa khoảng trắng thừa", "lines": [normalize_spaces(text)]}, None
    if mode == "words":
        words = normalize_spaces(text).split()
        return {
            "label": f"Số từ của chuỗi: {len(words)}",
            "lines": words or ["Chuỗi không có từ nào."],
        }, None
    if mode == "left_right":
        try:
            count = parse_natural_number(form.get("count", ""), "k")
        except ValueError as error:
            return None, str(error)
        return {
            "label": f"{count} ký tự bên trái và bên phải",
            "lines": [f"Bên trái: {text[:count]}", f"Bên phải: {text[-count:] if count else ''}"],
        }, None
    if mode == "substring":
        try:
            start = parse_natural_number(form.get("start", ""), "k")
            count = parse_natural_number(form.get("substring_count", ""), "n")
        except ValueError as error:
            return None, str(error)
        if start < 1:
            return None, "Vị trí k được tính từ 1."
        start_index = start - 1
        return {
            "label": f"{count} ký tự kể từ vị trí {start}",
            "lines": [text[start_index : start_index + count]],
        }, None

    return None, "Vui lòng chọn yêu cầu hợp lệ."
