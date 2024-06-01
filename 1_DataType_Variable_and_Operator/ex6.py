"""
    Đội Manchester United tham gia giải ngoài hạng anh.
    Yêu cầu người dùng nhập vào lần lượt 3 số tự nhiên
    tương ứng với số trận thắng, hòa, thua của đội.
    Quy tắc tính điểm như sau:
    - Mỗi trận thắng đội sẽ được 3 điểm
    - Mỗi trận hòa đội sẽ được 1 điểm
    - Mỗi trận thua đội sẽ không được điểm nào
    Tính số điểm đội có được
"""

win = int(input('so tran thang: '))
draw = int(input('so tran hoa: '))
lose = int(input('so tran thua: '))

print('score=', win * 3 + draw * 1)
