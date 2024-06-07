"""
    In ra các số có ít hơn 4 chữ số và chia hết cho cả 5 và 7
"""
for i in range(10000):
    if i % 5 == 0 and i % 7 == 0:
        print(i)
