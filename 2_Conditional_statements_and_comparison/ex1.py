"""
    Nhập vào 2 số:
    - 1 số đại diện cho 1 năm
    - 1 số đại diện cho 1 tháng trong năm đó
    In ra màn hình số ngày của tháng đó
    Chú ý: Năm nhuận là năm thỏa mãn 1 trong 2 điều kiện sau:
    - Năm đó chia hết cho 4 nhưng không chia hết cho 100
    - Năm đó chia hết cho 400
"""
year = int(input("Enter year number: "))
month = int(input("Enter month number: "))

if month==2:
    if (year%4==0 and year%100!=0) or (year%400==0):
        # Năm nhuận
        print("month has 29 days")
    else:
        print("month has 28 days")
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("month has 31 days")
else:
    print("month has 30 days")
