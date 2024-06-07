"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên n khác 0
    Tính n! theo 2 cách:
    - Sử dụng vòng lặp for
    - Sử dụng vòng lặp while
"""
n = int(input("Enter a number: "))
result = 1
# Sử dụng vòng lặp for
for i in range(1, n + 1):
    result *= i
print("The factorial of", n, "is", result)

# Sử dụng vòng lặp while
result = 1
i = 1
while i <= n:
    result *= i
    i += 1
print("The factorial of", n, "is", result)
