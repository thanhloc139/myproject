"""
    Cho 1 mảng gồm các số tùy ý
    Kiểm tra xem mảng đó có phải mảng đơn điệu hay không.
    Định nghĩa mảng đơn điệu: mảng đơn điệu là mảng
    không tăng hoặc không giảm
"""
array = [1, 3, 3, 4, 6, 7, 7]
# array = [5, 3, 2, 2, 1]
# array = [2, 3, 2, 1]

increase_array=sorted(array)
decrease_array=sorted(array,reverse=True)

if increase_array==array or decrease_array==array:
    print("this is not monotonic array ")
else:
    print("this is monotonic array")