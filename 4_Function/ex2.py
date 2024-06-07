"""
    Viết hàm nhận 3 số đầu vào, và trả về số lớn nất trong 3 số
    (Không dùng hàm max())
"""


def get_max(a, b, c):
    max_number = a
    if max_number < b:
        max_number = b
    if max_number < c:
        max_number = c
    return max_number


max_test = get_max(7.2, 4, 2)
print(max_test)
