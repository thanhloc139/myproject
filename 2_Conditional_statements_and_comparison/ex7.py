"""
    Yêu cầu người dùng nhập vào 2 số, trong đó:
    - Số thứ nhất là bán kính của 1 hình tròn
    - Số thứ hai là diện tích của 1 hình vuông
    Hãy tính và so sánh xem, trong 2 hình trên,
    hình nào có chu vi lớn hơn
"""
from math import pi
r1=float(input('nhap ban kinh hinh tron 1: '))
a2=float(input('nhap dien tich hinh tron 2: '))

r2=(a2/pi)**0.5 # tinh ban kinh hinh tron 2

c1=2*pi*r1 # tinh chu vi hinh tron 1
c2=2*pi*r2 # tinh chu vi hinh tron 2

if c1>c2:
    print("chu vi hinh tron 1 lon hon chu vi hinh tron 2")
elif c1==c2:
    print("chu vi hinh tron 1 bang chu vi hinh tron 2")
else:
    print("chu vi hinh tron 1 nho hon chu vi hinh tron 2")
