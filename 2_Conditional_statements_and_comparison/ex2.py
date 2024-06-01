"""
    Yêu cầu người dùng nhập vào 3 số a, b, c
    Tìm nghiệm của phương trình bậc 2
    ax^2 + bx + c = 0
"""
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
    print("x=", (-c) / b)
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("vo nghiem")
    elif delta == 0:
        print('x=', -(b / (2 * a)))
    else:
        print('x1= ', (-b + delta ** 0.5) / (2 * a))
        print('x2= ', (-b - delta ** 0.5) / (2 * a))
