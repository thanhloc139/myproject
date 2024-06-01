"""
    Nhập vào điểm của 1 học sinh (0-100)
    Quy đổi điểm từ thang điểm 100 sang thang điểm chữ theo quy tắc:
        Điểm                             Quy đổi
        > 90                                A
        > 80 và <=90                        B
        > 60 và <= 80                       C
        <= 60                               D
"""
n=int(input("nhap diem hoc sinh (0-100): "))
if n>90:
    # > 90                                A
    print("A")
elif n>80:
    # > 80 và <=90                        B
    print("B")
elif n>60:
    # > 60 và <= 80                       C
    print("C")
else:
    #  <= 60                               D
    print("D")