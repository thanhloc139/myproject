"""
    Yêu cầu người dùng nhập vào 2 số bất kỳ.
    Viết chương trình để đổi giá trị 2 số đó với nhau theo 2 cách
"""
a = input("Enter the first value: ")
b = input("Enter the second value: ")
print("Original values: a =", a, ", b=", b)

# cach 1
print("a=", b,"b=",a)

# cach 2
temp=a
a=b
b=temp
print("a=", a,"b=",b)
