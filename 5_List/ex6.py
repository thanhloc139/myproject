"""
    Cho 1 danh sách gồm các số
    Viết các chương trình để tìm ra:
    1. Số lớn nhất
    2. Số lớn thứ nhì
    3. k số lớn nhất

"""

numbers = [20, 36, 10, -4, 5, 15, 36, -16]

increase_sorted = sorted(numbers, reverse=True)
print(increase_sorted)
# 1. Số lớn nhất
print("maximum is ", increase_sorted[0])
k_max = 1
for i in range(1, len(increase_sorted)):
    if increase_sorted[0] != increase_sorted[i]:
        # 2. Số lớn thứ nhì
        second_max = increase_sorted[i]
        print(second_max, "is seconde maximum")
        break
    else:
        # 3. k số lớn nhất
        k_max += 1
print("there are", k_max, "of maximum")
