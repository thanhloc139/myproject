"""
    Viết 1 hàm nhận 2 tham số đầu vào là 2 ma trận,
    kết quả trả về là ma trận tổng của chúng. Nếu phép
    cộng không thực hiện được thì trả về giá trị 0
    Ví dụ:
    Input:
        mat1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    mat2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
    ]
    Output:
        array = [4, 5, 1, 2, 3]

"""


def add_matrices(mat1, mat2):
    """
    quét từng phan tử, i quét theo hàng, j quét theo cột, [i][j] hang i cot j
    :param mat1: ma trận 1
    :param mat2: ma trận 2
    :return: ma trận tổng
    """
    if len(mat1)==len(mat2) and len(mat1[0])==len(mat2[0]):
        mat_sum = []
        for i in range(len(mat1)):
            temp=[]
            for j in range(len(mat1[0])):
                temp.append(mat1[i][j] + mat2[i][j])
            mat_sum.append(temp)

        return mat_sum
    else:
        return 0

mat1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
mat2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
    ]

# mat2 = [
#         [9, 8, 7, 2],
#         [6, 5, 4, 2],
#         [3, 2, 1, 2],
#     ]

print(add_matrices(mat1,mat2))