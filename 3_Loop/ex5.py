"""
    Đếm số chẵn, lẻ, âm, dương trong dãy sau
"""
numbers = [2, -3, 1, 5, -6, 3, 2, -4, 0, 5, 1, -3, -1, 2, 6, 3, -5, 0, 1, -4, 2, 3, -1, 0, 3, 2, -4, 2, 3]

even_num = 0
odd_num = 0
positive_num = 0
negative_num = 0

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        # Đếm số chẵn
        even_num += 1
    else:
        # Đếm số le
        odd_num += 1

    if numbers[i] == 0:
        continue
    elif numbers[i] > 0:
        # Đếm số duong
        positive_num += 1
    else:
        # Đếm số am
        negative_num += 1

print("number of even: ", even_num)
print("number of odd: ", odd_num)
print("number of positive: ", positive_num)
print("number of negative: ", negative_num)
