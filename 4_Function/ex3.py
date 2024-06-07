"""
    Viết 1 hàm nhận vào 2 tham số đầu vào
    1. Cân nặng của 1 người (đơn vị: kg)
    2. Chiều cao của người đó (đơn vị: mét)
    Hàm trả về 3 thông tin sau:
    1. Chỉ số cân đối cơ thể BMI = cân nặng/chiều cao^2
    2. Thể trạng của người đó
    3. Nguy cơ phát triển bệnh
    2. và 3. được kết luận dựa vào bảng sau:
    BMI             Status (Thể trạng)  Disease risk (Nguy cơ phát triển bệnh)
    < 18.5          Underweight         Low
    18.5-24.9       Normal              Medium
    25.0-29.9       Overweight          High
    30.0-34.9       Obese               High
    > 35.0          Extremely Obese     Very High
"""


def estimate_infor(height, weight):
    BMI = weight / (height ** 2)
    if BMI < 18.5:
        status = "underweight"
        risk = "low"
    elif BMI < 24.9:
        status = "normal"
        risk = "medium"
    elif BMI < 29.9:
        status = "overweight"
        risk = "high"
    elif BMI < 34.9:
        status = "obese"
        risk = "high"
    else:
        status = "extremely obese"
        risk = "very high"

    return BMI, status, risk


height = float(input("Enter the height: "))
weight = float(input("Enter the weight: "))
bmi, status, risk = estimate_infor(height, weight)
print("BMI:", bmi)
print("Status:", status)
print("Disease risk:", risk)
