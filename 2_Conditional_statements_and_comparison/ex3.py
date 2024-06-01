"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên tương ứng
    với số đơn vị điện sử dụng của 1 hộ gia đình
    Viết chương trình tính hóa đơn tiền điện cho gia đình đó,
    với quy tắc sau:
    Số đơn vị điện                     Giá
    100 đơn vị đầu                  Miễn phí
    100 đơn vị tiếp theo            5$/đơn vị
    Các đơn vị sau đó               10$/đơn vị
"""

n = int(input('nhap so don vi dien: '))
if n <= 100:
    # 100 đơn vị đầu                  Miễn phí
    print('free')
elif n <= 200:
    # 100 đơn vị tiếp theo            5$/đơn vị
    print("gia= ", (n - 100) * 5, "$")
else:
    # Các đơn vị sau đó               10$/đơn vị
    print("gia= ", 100 * 5 + (n - 200) * 10, "$")

