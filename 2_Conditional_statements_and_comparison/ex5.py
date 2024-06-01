"""
    Yêu cầu người dùng nhập vào 3 số nguyên dương
    1. Kiểm tra xem đây có phải là số đo 3 cạnh của 1 tam giác không?
    2. Nếu có thì kiểm tra tiếp xem đây là tam giác cân, tam giác đều,
    tam giác vuông hay tam giác thường
    3. Kiểm tra tiếp xem tam giác có góc tù hay không?
    4. Tính diện tích của tam giác
"""
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
# 1. Kiểm tra xem đây có phải là số đo 3 cạnh của 1 tam giác không?
if a + b > c or a + c > b or b + c > a:
    print("a , b , c la so do 3 canh cua 1 tam giac")
    """
    2. Nếu có thì kiểm tra tiếp xem đây là tam giác đều, tam giác cân,
    tam giác vuông hay tam giác thường
    """
    if a == b == c:
        print("tam giac la tam giac deu")
    elif a == b or a == c or b == c:
        print("tam giac la tam giac can")
    elif (a ** 2 + b ** 2) == c ** 2 or (a ** 2 + c ** 2) == b ** 2 or (c ** 2 + b ** 2) == a ** 2:
        print("tam giac la tam giac vuong")
    else:
        print("tam giac la tam giac thuong")
        """
        3. Kiểm tra tiếp xem tam giác có góc tù hay không?
        """
        if (a ** 2 + b ** 2) < c ** 2 or (a ** 2 + c ** 2) < b ** 2 or (c ** 2 + b ** 2) < a ** 2:
            print("tam giac co goc tu")
    '''
     4. Tính diện tích của tam giác (cong thuc Heron)
    '''      
    p=(a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**0.5
    print("dien tich cua tam giac= ",s)

else:
    print("a , b , c KHONG la so do 3 canh cua 1 tam giac")
