import html

from calculator import CALCULATOR_OPERATIONS
from student_manager import STUDENTS


EXERCISES = [
    ("01", "Câu 1", "Nhập 2 số, tính tổng, hiệu, tích, thương.", "/cau1"),
    ("02", "Câu 2", "Nhập chiều dài, chiều rộng, tính diện tích và chu vi hình chữ nhật.", "/cau2"),
    ("03", "Câu 3", "Nhập bán kính r, tính diện tích và chu vi hình tròn.", "/cau3"),
    ("04", "Câu 4", "Nhập số tự nhiên n, kiểm tra n là số chẵn hay lẻ.", "/cau4"),
    ("05", "Câu 5", "Nhập số tự nhiên n, kiểm tra n có phải số nguyên tố.", "/cau5"),
    ("06", "Câu 6", "Xuất các dãy số <= n và tính tổng của chúng.", "/cau6"),
    ("07", "Câu 7", "Giúp bé làm toán và kiểm tra đáp án đúng hay sai.", "/cau7"),
    ("08", "Câu 8", "Nhập mảng số nguyên và thực hiện các thao tác trên mảng.", "/cau8"),
    ("09", "Câu 9", "Nhập chuỗi s và xử lý độ dài, từ, cắt chuỗi.", "/cau9"),
    ("10", "Câu 10", "Quản lý điểm sinh viên, tính điểm trung bình và xếp loại.", "/cau10"),
]


def esc(value):
    return html.escape(str(value))


def render_layout(title, subtitle, content):
    nav_links = "\n".join(
        f'<a href="{url}">{label}</a>'
        for _, label, _, url in EXERCISES
    )
    return f"""<!doctype html>
<html lang="vi">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{esc(title)}</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <div class="page-shell">
        <aside class="sidebar">
            <a class="brand" href="/">
                <span class="brand-mark">PY</span>
                <span>
                    <strong>Python Web</strong>
                    <small>Bài tập desktop</small>
                </span>
            </a>
            <nav class="side-nav" aria-label="Danh sách bài tập">
                <a href="/">Trang chọn bài</a>
                {nav_links}
            </nav>
        </aside>
        <main>
            <header>
                <span class="eyebrow">Ứng dụng tính toán</span>
                <h1>{esc(title)}</h1>
                <p>{esc(subtitle)}</p>
            </header>
            {content}
        </main>
    </div>
</body>
</html>"""


def render_home():
    cards = "\n".join(
        f"""
        <a class="menu-item" href="{url}">
            <span class="menu-number">{number}</span>
            <span class="menu-copy">
                <strong>{label}</strong>
                <span>{description}</span>
            </span>
            <span class="menu-arrow">Vào bài</span>
        </a>
        """
        for number, label, description, url in EXERCISES
    )
    content = f'<section class="menu-panel">{cards}</section>'
    return render_layout("Bài tập Python Web", "Chọn mục liên quan để tiếp tục.", content)


def render_back_link():
    return """
        <nav class="top-actions" aria-label="Điều hướng bài tập">
            <a href="/">Quay về menu</a>
        </nav>
    """


def render_text_input(label, name, value="", input_type="number", required=True, step="any"):
    required_attr = "required" if required else ""
    step_attr = f' step="{step}"' if input_type == "number" and step else ""
    return f"""
        <label>
            {esc(label)}
            <input type="{input_type}"{step_attr} name="{esc(name)}" value="{esc(value)}" {required_attr}>
        </label>
    """


def render_select(label, name, options, selected):
    option_html = "\n".join(
        f'<option value="{esc(value)}" {"selected" if value == selected else ""}>{esc(text)}</option>'
        for value, text in options
    )
    return f"""
        <label>
            {esc(label)}
            <select name="{esc(name)}">
                {option_html}
            </select>
        </label>
    """


def render_tool_page(title, subtitle, form_html):
    return render_layout(
        title,
        subtitle,
        f'<section class="tool-panel">{render_back_link()}{form_html}</section>',
    )


def render_calculator_page(mode="buttons", form=None, result=None, error=None):
    form = form or {}
    active_operation = form.get("operation", "sum")
    buttons_active = "active" if mode == "buttons" else ""
    radio_active = "active" if mode == "radio" else ""
    action = "/cau1/radio" if mode == "radio" else "/cau1"
    controls = render_radio_controls(active_operation) if mode == "radio" else render_button_controls()

    form_html = f"""
        <nav class="mode-tabs" aria-label="Cách thực hiện">
            <a class="{buttons_active}" href="/cau1">Dùng button</a>
            <a class="{radio_active}" href="/cau1/radio">Dùng radio button</a>
        </nav>
        <form method="post" action="{action}">
            <div class="field-grid">
                {render_text_input("Số thứ nhất", "first_number", form.get("first_number", ""))}
                {render_text_input("Số thứ hai", "second_number", form.get("second_number", ""))}
            </div>
            {controls}
            {render_result(result, error)}
        </form>
    """
    return render_tool_page(
        "Câu 1: Tổng, hiệu, tích, thương",
        "Nhập 2 số và chọn phép tính cần thực hiện.",
        form_html,
    )


def render_rectangle_page(form=None, result=None, error=None):
    form = form or {}
    form_html = f"""
        <form method="post" action="/cau2">
            <div class="field-grid">
                {render_text_input("Chiều dài", "length", form.get("length", ""))}
                {render_text_input("Chiều rộng", "width", form.get("width", ""))}
            </div>
            <button class="primary-button" type="submit">Tính diện tích và chu vi</button>
            {render_rectangle_result(result, error)}
        </form>
    """
    return render_tool_page(
        "Câu 2: Hình chữ nhật",
        "Nhập chiều dài, chiều rộng để tính diện tích và chu vi.",
        form_html,
    )


def render_circle_page(form=None, result=None, error=None):
    form = form or {}
    form_html = f"""
        <form method="post" action="/cau3">
            {render_text_input("Bán kính r", "radius", form.get("radius", ""))}
            <button class="primary-button" type="submit">Tính diện tích và chu vi</button>
            {render_circle_result(result, error)}
        </form>
    """
    return render_tool_page(
        "Câu 3: Hình tròn",
        "Nhập bán kính r để tính diện tích và chu vi hình tròn.",
        form_html,
    )


def render_even_odd_page(form=None, result=None, error=None):
    form = form or {}
    form_html = f"""
        <form method="post" action="/cau4">
            {render_text_input("Số tự nhiên n", "number", form.get("number", ""), step="1")}
            <button class="primary-button" type="submit">Kiểm tra chẵn lẻ</button>
            {render_even_odd_result(result, error)}
        </form>
    """
    return render_tool_page(
        "Câu 4: Kiểm tra chẵn lẻ",
        "Nhập số tự nhiên n để xác định n là số chẵn hay số lẻ.",
        form_html,
    )


def render_prime_check_page(form=None, result=None, error=None):
    form = form or {}
    form_html = f"""
        <form method="post" action="/cau5">
            {render_text_input("Số tự nhiên n", "number", form.get("number", ""), step="1")}
            <button class="primary-button" type="submit">Kiểm tra nguyên tố</button>
            {render_prime_result(result, error)}
        </form>
    """
    return render_tool_page(
        "Câu 5: Kiểm tra số nguyên tố",
        "Nhập số tự nhiên n để kiểm tra n có phải số nguyên tố hay không.",
        form_html,
    )


def render_number_list_page(form=None, result=None, error=None):
    form = form or {}
    options = [
        ("all", "Các số tự nhiên <= n"),
        ("even", "Các số chẵn <= n"),
        ("odd", "Các số lẻ <= n"),
        ("prime", "Các số nguyên tố <= n"),
        ("first_primes", "N số nguyên tố đầu tiên"),
    ]
    form_html = f"""
        <form method="post" action="/cau6">
            <div class="field-grid">
                {render_text_input("Số tự nhiên n", "number", form.get("number", ""), step="1")}
                {render_select("Yêu cầu xuất", "mode", options, form.get("mode", "all"))}
            </div>
            <button class="primary-button" type="submit">Xuất kết quả</button>
            {render_list_result(result, error)}
        </form>
    """
    return render_tool_page(
        "Câu 6: Dãy số tự nhiên",
        "Nhập n, chọn yêu cầu và xem danh sách kèm tổng.",
        form_html,
    )


def render_kid_math_page(form=None, result=None, error=None):
    form = form or {}
    options = [(key, symbol) for key, (_, _, symbol) in CALCULATOR_OPERATIONS.items()]
    form_html = f"""
        <form method="post" action="/cau7">
            <div class="field-grid">
                {render_text_input("Số tự nhiên thứ 1", "first_number", form.get("first_number", ""), step="1")}
                {render_text_input("Số tự nhiên thứ 2", "second_number", form.get("second_number", ""), step="1")}
                {render_select("Phép toán", "operation", options, form.get("operation", "sum"))}
                {render_text_input("Đáp số của bé", "answer", form.get("answer", ""))}
            </div>
            <button class="primary-button" type="submit">Kiểm tra đáp án</button>
            {render_kid_math_result(result, error)}
        </form>
    """
    return render_tool_page(
        "Câu 7: Giúp bé làm toán",
        "Nhập 2 số, chọn phép toán, nhập đáp số và kiểm tra đúng sai.",
        form_html,
    )


def render_array_page(form=None, result=None, error=None):
    form = form or {}
    options = [
        ("all", "Xuất mảng và tổng"),
        ("even", "Xuất phần tử chẵn và tổng"),
        ("odd", "Xuất phần tử lẻ và tổng"),
        ("prime", "Xuất phần tử nguyên tố và tổng"),
        ("add", "Thêm 1 phần tử mới"),
        ("delete", "Xóa phần tử thứ k"),
        ("search", "Tìm vị trí của x"),
    ]
    form_html = f"""
        <form method="post" action="/cau8">
            <div class="field-grid">
                {render_text_input("Số phần tử N", "size", form.get("size", ""), required=False, step="1")}
                {render_select("Yêu cầu xử lý", "mode", options, form.get("mode", "all"))}
            </div>
            <label>
                Các phần tử của mảng
                <textarea name="values" rows="4" required>{esc(form.get("values", ""))}</textarea>
            </label>
            <div class="field-grid">
                {render_text_input("Phần tử mới", "new_value", form.get("new_value", ""), required=False, step="1")}
                {render_text_input("Vị trí k cần xóa", "index", form.get("index", ""), required=False, step="1")}
                {render_text_input("Số x cần tìm", "target", form.get("target", ""), required=False, step="1")}
            </div>
            <button class="primary-button" type="submit">Xử lý mảng</button>
            {render_array_result(result, error)}
        </form>
    """
    return render_tool_page(
        "Câu 8: Mảng số nguyên",
        "Nhập N và các phần tử của mảng, sau đó chọn thao tác cần thực hiện.",
        form_html,
    )


def render_string_page(form=None, result=None, error=None):
    form = form or {}
    options = [
        ("length", "Độ dài của s"),
        ("trim", "Xóa khoảng trắng thừa"),
        ("words", "Đếm số từ và tách mỗi từ trên 1 dòng"),
        ("left_right", "Lấy k ký tự bên trái và bên phải"),
        ("substring", "Lấy n ký tự kể từ vị trí k"),
    ]
    form_html = f"""
        <form method="post" action="/cau9">
            <label>
                Chuỗi s
                <textarea name="text" rows="5" required>{esc(form.get("text", ""))}</textarea>
            </label>
            <div class="field-grid">
                {render_select("Yêu cầu xử lý", "mode", options, form.get("mode", "length"))}
                {render_text_input("Số tự nhiên k", "count", form.get("count", ""), required=False, step="1")}
                {render_text_input("Vị trí k", "start", form.get("start", ""), required=False, step="1")}
                {render_text_input("Số ký tự n", "substring_count", form.get("substring_count", ""), required=False, step="1")}
            </div>
            <button class="primary-button" type="submit">Xử lý chuỗi</button>
            {render_string_result(result, error)}
        </form>
    """
    return render_tool_page(
        "Câu 9: Xử lý chuỗi",
        "Nhập chuỗi s và chọn yêu cầu xử lý.",
        form_html,
    )


def render_student_page(form=None, result=None, error=None):
    form = form or {}
    students = (result or {}).get("students", STUDENTS)
    form_html = f"""
        <form method="post" action="/cau10">
            <div class="field-grid">
                {render_text_input("Mã sinh viên", "student_id", form.get("student_id", ""), input_type="text")}
                {render_text_input("Họ tên", "full_name", form.get("full_name", ""), input_type="text")}
                {render_text_input("Điểm 1", "score_1", form.get("score_1", ""))}
                {render_text_input("Điểm 2", "score_2", form.get("score_2", ""))}
                {render_text_input("Điểm 3", "score_3", form.get("score_3", ""))}
            </div>
            <div class="button-grid two-cols">
                <button class="primary-button" type="submit" name="action" value="add">Thêm sinh viên</button>
                <button class="secondary-button" type="submit" name="action" value="clear" formnovalidate>Xóa danh sách</button>
            </div>
            {render_student_result(result, error, students)}
        </form>
    """
    return render_tool_page(
        "Câu 10: Quản lý điểm sinh viên",
        "Nhập thông tin sinh viên, tính điểm trung bình và xếp loại.",
        form_html,
    )


def render_button_controls():
    buttons = "\n".join(
        f"""
        <button class="operation-button" type="submit" name="operation" value="{key}">
            {display}
        </button>
        """
        for key, (_, display, _) in CALCULATOR_OPERATIONS.items()
    )
    return f'<div class="button-grid">{buttons}</div>'


def render_radio_controls(active_operation):
    radios = "\n".join(
        f"""
        <label class="radio-option">
            <input type="radio" name="operation" value="{key}" {"checked" if key == active_operation else ""}>
            <span>{display}</span>
        </label>
        """
        for key, (_, display, _) in CALCULATOR_OPERATIONS.items()
    )
    return f"""
        <div class="radio-grid">{radios}</div>
        <button class="primary-button" type="submit">Tính kết quả</button>
    """


def render_result(result, error):
    if error:
        return render_error(error)
    if result:
        return f"""
            <div class="message success">
                <span>Kết quả phép {esc(result["label"]).lower()}</span>
                <strong>{esc(result["expression"])}</strong>
            </div>
        """
    return ""


def render_rectangle_result(result, error):
    if error:
        return render_error(error)
    if result:
        return render_metrics(
            f'Kết quả với chiều dài {esc(result["length"])} và chiều rộng {esc(result["width"])}',
            [("Diện tích", result["area"]), ("Chu vi", result["perimeter"])],
        )
    return ""


def render_circle_result(result, error):
    if error:
        return render_error(error)
    if result:
        return render_metrics(
            f'Kết quả với bán kính {esc(result["radius"])}',
            [("Diện tích", result["area"]), ("Chu vi", result["circumference"])],
        )
    return ""


def render_even_odd_result(result, error):
    if error:
        return render_error(error)
    if result:
        return render_message("success", "Kết quả", f'Số {esc(result["number"])} là số {esc(result["kind"])}.')
    return ""


def render_prime_result(result, error):
    if error:
        return render_error(error)
    if result:
        text = "là số nguyên tố" if result["is_prime"] else "không phải số nguyên tố"
        return render_message("success", "Kết quả", f'Số {esc(result["number"])} {text}.')
    return ""


def render_list_result(result, error):
    if error:
        return render_error(error)
    if not result:
        return ""
    values = ", ".join(map(str, result["values"])) if result["values"] else "Không có giá trị nào."
    return f"""
        <div class="message success result-list">
            <span>{esc(result["label"])}</span>
            <strong>{esc(values)}</strong>
            <small>Tổng: {esc(result["total"])}</small>
        </div>
    """


def render_kid_math_result(result, error):
    if error:
        return render_error(error)
    if not result:
        return ""
    status = "Đúng rồi" if result["correct"] else "Sai rồi"
    detail = (
        f'Đáp án của bé: {esc(result["answer"])}. '
        f'Đáp án đúng: {esc(result["correct_answer"])}.'
    )
    return render_message("success", status, detail)


def render_array_result(result, error):
    if error:
        return render_error(error)
    if not result:
        return ""
    values = ", ".join(map(str, result["values"])) if result["values"] else "Không có phần tử nào."
    extra = f'<small>{esc(result["extra"])}</small>' if result["extra"] else ""
    return f"""
        <div class="message success result-list">
            <span>{esc(result["label"])}</span>
            <strong>{esc(values)}</strong>
            <small>Tổng: {esc(result["total"])}</small>
            {extra}
        </div>
    """


def render_string_result(result, error):
    if error:
        return render_error(error)
    if not result:
        return ""
    lines = "\n".join(f"<li>{esc(line)}</li>" for line in result["lines"])
    return f"""
        <div class="message success result-list">
            <span>{esc(result["label"])}</span>
            <ul class="result-lines">{lines}</ul>
        </div>
    """


def render_student_result(result, error, students):
    if error:
        return render_error(error) + render_student_table(students)
    message = ""
    if result and result.get("message"):
        message = render_message("success", "Thông báo", result["message"])
    return message + render_student_table(students)


def render_student_table(students):
    if not students:
        return '<div class="message muted-box">Chưa có sinh viên nào trong danh sách.</div>'
    rows = "\n".join(
        f"""
        <tr>
            <td>{esc(student["student_id"])}</td>
            <td>{esc(student["full_name"])}</td>
            <td>{esc(student["score_1"])}</td>
            <td>{esc(student["score_2"])}</td>
            <td>{esc(student["score_3"])}</td>
            <td>{esc(student["average"])}</td>
            <td>{esc(student["rank"])}</td>
        </tr>
        """
        for student in students
    )
    return f"""
        <div class="table-wrap">
            <table>
                <thead>
                    <tr>
                        <th>Mã SV</th>
                        <th>Họ tên</th>
                        <th>Điểm 1</th>
                        <th>Điểm 2</th>
                        <th>Điểm 3</th>
                        <th>ĐTB</th>
                        <th>Xếp loại</th>
                    </tr>
                </thead>
                <tbody>{rows}</tbody>
            </table>
        </div>
    """


def render_metrics(title, metrics):
    metric_html = "\n".join(
        f"<strong>{esc(label)}: {esc(value)}</strong>"
        for label, value in metrics
    )
    return f"""
        <div class="message success result-list">
            <span>{title}</span>
            <div class="metric-grid">{metric_html}</div>
        </div>
    """


def render_message(kind, title, content):
    return f"""
        <div class="message {esc(kind)}">
            <span>{esc(title)}</span>
            <strong>{esc(content)}</strong>
        </div>
    """


def render_error(error):
    return f'<div class="message error">{esc(error)}</div>'
