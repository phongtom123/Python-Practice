from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from array_exercise import build_array_result
from calculator import build_result
from circle import build_circle_result
from even_odd import build_even_odd_result
from kid_math import build_kid_math_result
from number_series import build_number_list_result
from prime import build_prime_check_result
from rectangle import build_rectangle_result
from string_exercise import build_string_result
from student_manager import build_student_result
from views import (
    render_array_page,
    render_calculator_page,
    render_circle_page,
    render_even_odd_page,
    render_home,
    render_kid_math_page,
    render_number_list_page,
    render_prime_check_page,
    render_rectangle_page,
    render_string_page,
    render_student_page,
)


HOST = "127.0.0.1"
PORT = 8000
BASE_DIR = Path(__file__).resolve().parent


def parse_form(body):
    data = parse_qs(body, keep_blank_values=True)
    return {key: values[0] for key, values in data.items()}


class CalculatorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path

        if path == "/":
            self.send_html(render_home())
            return

        if path in ("/cau1", "/cau1/radio", "/radio"):
            mode = "radio" if path in ("/cau1/radio", "/radio") else "buttons"
            self.send_html(render_calculator_page(mode=mode))
            return

        if path == "/cau2":
            self.send_html(render_rectangle_page())
            return

        if path == "/cau3":
            self.send_html(render_circle_page())
            return

        if path == "/cau4":
            self.send_html(render_even_odd_page())
            return

        if path == "/cau5":
            self.send_html(render_prime_check_page())
            return

        if path == "/cau6":
            self.send_html(render_number_list_page())
            return

        if path == "/cau7":
            self.send_html(render_kid_math_page())
            return

        if path == "/cau8":
            self.send_html(render_array_page())
            return

        if path == "/cau9":
            self.send_html(render_string_page())
            return

        if path == "/cau10":
            self.send_html(render_student_page())
            return

        if path == "/static/style.css":
            self.send_static_css()
            return

        self.send_error(404, "Không tìm thấy trang")

    def do_POST(self):
        path = urlparse(self.path).path

        if path in ("/cau1", "/cau1/radio", "/radio"):
            length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(length).decode("utf-8")
            form = parse_form(body)
            result, error = build_result(form)
            mode = "radio" if path in ("/cau1/radio", "/radio") else "buttons"
            self.send_html(render_calculator_page(mode=mode, form=form, result=result, error=error))
            return

        if path == "/cau2":
            length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(length).decode("utf-8")
            form = parse_form(body)
            result, error = build_rectangle_result(form)
            self.send_html(render_rectangle_page(form=form, result=result, error=error))
            return

        if path == "/cau3":
            form = self.read_form()
            result, error = build_circle_result(form)
            self.send_html(render_circle_page(form=form, result=result, error=error))
            return

        if path == "/cau4":
            form = self.read_form()
            result, error = build_even_odd_result(form)
            self.send_html(render_even_odd_page(form=form, result=result, error=error))
            return

        if path == "/cau5":
            form = self.read_form()
            result, error = build_prime_check_result(form)
            self.send_html(render_prime_check_page(form=form, result=result, error=error))
            return

        if path == "/cau6":
            form = self.read_form()
            result, error = build_number_list_result(form)
            self.send_html(render_number_list_page(form=form, result=result, error=error))
            return

        if path == "/cau7":
            form = self.read_form()
            result, error = build_kid_math_result(form)
            self.send_html(render_kid_math_page(form=form, result=result, error=error))
            return

        if path == "/cau8":
            form = self.read_form()
            result, error = build_array_result(form)
            self.send_html(render_array_page(form=form, result=result, error=error))
            return

        if path == "/cau9":
            form = self.read_form()
            result, error = build_string_result(form)
            self.send_html(render_string_page(form=form, result=result, error=error))
            return

        if path == "/cau10":
            form = self.read_form()
            result, error = build_student_result(form)
            self.send_html(render_student_page(form=form, result=result, error=error))
            return

        if path == "/":
            self.send_error(405, "Vui lòng chọn bài tập trước")
            return

        else:
            self.send_error(404, "Không tìm thấy trang")
            return

    def read_form(self):
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length).decode("utf-8")
        return parse_form(body)

    def send_html(self, content):
        encoded = content.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def send_static_css(self):
        css_path = BASE_DIR / "static" / "style.css"
        encoded = css_path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/css; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)


def main():
    server = ThreadingHTTPServer((HOST, PORT), CalculatorHandler)
    print(f"Mở trình duyệt tại http://{HOST}:{PORT}")
    print("Nhấn Ctrl+C để dừng chương trình.")
    server.serve_forever()


if __name__ == "__main__":
    main()
