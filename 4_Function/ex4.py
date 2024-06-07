"""
    A.
    Viết hàm is_member() nhận 2 tham số đầu vào:
    1. 1 giá trị (số, chuỗi ký tự, bool, ...)
    2. 1 List chứa các giá trị bất kì
    Hàm kiểm tra xem giá trị có xuất hiện trong List hay không
    (Không dùng toán tử in)

    B.
    Viết hàm overlapping() nhận 2 tham số đầu vào là 2 List
    Hàm trả về danh sách các phần tử nằm ở cả 2 List
    Gợi ý: Sử dụng hàm is_member()
"""


def is_member(value, list_of_values):
    for i in range(len(list_of_values)):
        if value == list_of_values[i]:
            return "true"
    else:
        return "false"


def overlapping(list_a, list_b):
    list_temp = []
    for i in range(len(list_a)):
        if is_member(list_a[i], list_b) == "true":
            list_temp.append(list_a[i])
    return list_temp


print(is_member("monday", ["rose", 5, True, "monday", "tuesday", -5.5]))
print(is_member("Monday", ["rose", 5, True, "monday", "tuesday", -5.5]))

print(overlapping(["rose", 5, True, "monday",-5.5],["rose", 5, True, "monday", "tuesday", -5.5]))
