"""
    Yêu cầu người dùng nhập vào lượng nước tiêu thụ của 1 hộ gia đình
    Viết chương trình tính hóa đơn tiền nước cho gia đình đó,
    với quy tắc sau:
    Lượng nước (lít)                    Giá mỗi 1000 lít
    0-8000                                  5$
    8001-22000                              6$
    22001-30000                             7$
    30001+                                  10$
"""
n=int(input("nhap so luong nuoc tieu thu (lit): "))
if n<=8000:
    # 0-8000                                  5$
    print("gia= ",(n//1000)*5," $")
elif n<=22000:
    # 8001-22000                              6$
    print("gia= ", (8 * 5)+(((n-8000)//1000)*6), " $")
elif n<=30000:
    # 22001-30000                             7$
    print("gia= ", (8*5)+(14*6)+((n-22000)//1000)*7, " $")
else:
    # 30001+                                  10$
    print("gia= ", (8 * 5) + (14 * 6) + (8 * 7) + ((n - 30000) // 1000) * 10, " $")
