"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 list bao gồm các số bất kì
    2. 1 số tự nhiên k
    Đếm xem số k xuất hiện trong list bao nhiêu lần
"""

numbers = [20, 10, -4, 5, 10, 36, -16, 3, 5, 10, 16, -5, 5]
k = 10


def count_number(lista, k):
    count = 0
    for i in range(len(lista)):
        if k == numbers[i]:
            count += 1
    return count


print(count_number(numbers, k))
