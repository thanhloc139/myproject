"""
    Viết hàm nhận 1 tham số đầu vào là 1 số tự nhiên n
    In ra kết quả là tích các thừa số nguyên tố của số đó
    Ví dụ, với n = 100
    Kết quả in ra màn hình là:
        100 = 2 x 2 x 5 x 5
"""


def get_string(n):
    """
    prime_n cac so nguyen to tu 2 den n
    n chia so nguyen to thu 1, neu chia het thi thuc hien tiep voi so nguyen to do
    neu chia khong het, thi try voi so nguyen to thu 2 v.v


    :param n: 1 số tự nhiên n
    :return: tích các thừa số nguyên tố của số n
    """
    prime_n = []
    for i in range(2, n+1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            prime_n.append(i)

    count = 0
    while count <= len(prime_n):
        if n in prime_n:
            print(n)
            break
        elif n % prime_n[count] == 0:
            print(prime_n[count])
            n = n // prime_n[count]
        else:
            count += 1


print(get_string(3))
