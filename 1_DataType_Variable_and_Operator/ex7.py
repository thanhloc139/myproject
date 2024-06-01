"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên bất kì
    Lấy ra chữ số hàng đơn vị theo 2 cách khác nhau
    rồi in ra màn hình
"""

n=input('enter the number= ')
# cach 1
print('don vi= ',n[len(n)-1])

# cach 2
n=int(n)
print('don vi= ', n%10)