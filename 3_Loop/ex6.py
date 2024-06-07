"""
    Yêu cầu người dùng nhập vào 1 số dạng nhị phân (e.g. 1001)
    In ra giá trị dạng thập phân tương ứng của số đó
"""
n = input("Enter a binary number: ")
decimal_num = 0
for i in range(len(n) - 1, -1, -1):
    print(n[i], len(n) - 1 - i)
    decimal_num += int(n[i])* 2 ** (len(n) - 1 - i)
print(decimal_num)
