from calculator import format_number
from helpers import normalize_spaces


STUDENTS = []


def classify_average(average):
    if average >= 8:
        return "Giỏi"
    if average >= 6.5:
        return "Khá"
    if average >= 5:
        return "Trung bình"
    return "Yếu"


def parse_score(value, field_name):
    try:
        score = float(value.strip())
    except ValueError:
        raise ValueError(f"Vui lòng nhập đúng {field_name}.")
    if score < 0 or score > 10:
        raise ValueError(f"{field_name.capitalize()} phải từ 0 đến 10.")
    return score


def build_student_result(form):
    action = form.get("action", "add")
    if action == "clear":
        STUDENTS.clear()
        return {"students": STUDENTS, "message": "Đã xóa danh sách sinh viên."}, None

    student_id = form.get("student_id", "").strip()
    full_name = normalize_spaces(form.get("full_name", ""))
    if not student_id or not full_name:
        return None, "Vui lòng nhập mã sinh viên và họ tên."

    try:
        score_1 = parse_score(form.get("score_1", ""), "điểm 1")
        score_2 = parse_score(form.get("score_2", ""), "điểm 2")
        score_3 = parse_score(form.get("score_3", ""), "điểm 3")
    except ValueError as error:
        return None, str(error)

    average = (score_1 + score_2 + score_3) / 3
    student = {
        "student_id": student_id,
        "full_name": full_name,
        "score_1": format_number(score_1),
        "score_2": format_number(score_2),
        "score_3": format_number(score_3),
        "average": format_number(average),
        "rank": classify_average(average),
    }
    STUDENTS.append(student)
    return {"students": STUDENTS, "message": "Đã thêm sinh viên vào danh sách."}, None
