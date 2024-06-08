"""
    Viết 1 hàm nhận 2 tham số đầu vào là 2 ma trận cùng kích thước,
    kết quả trả về là ma trận tích của chúng
    Ví dụ:
    Input:
        mat1 = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    mat2 = [
        [7, 8],
        [9, 10],
        [11, 12],
    ]


    Output:
        array = [
        [58,  64],
        [139, 154],
    ]

"""


def multiply_matrices(mat1, mat2):
    """
    b1: chuyen ma tran 2 thanh mat2_new=[[7,9,11],[8,10,12]]-->mat1 va mat2_new giong nhau-->zip
    b2: i quet hang mat1
            j quet hang mat2_new
            0, 0: zip(mat1[0],mat2_new[0])-->value1-->append [value1]
            0, 1: zip(mat1[0],mat2_new[1])-->value2-->append [value1 value2] -->[[value1 value2],]
            1, 0: zip(mat1[1],mat2_new[0])-->value3-->append [value3]
            1, 1: zip(mat1[1],mat2_new[1])-->value4-->append [value3 value4] -->[[value1 value2],[value3 value4]]




    :param mat1: ma tran 1
    :param mat2: ma tran 2
    :return: ma tran tich
    """

    mat2_new=[]
    for i in range(len(mat2[0])):
        row_mat2_temp=[]
        for j in range(len(mat2)):
            row_mat2_temp.append(mat2[j][i])
        mat2_new.append(row_mat2_temp)

    mat_sum=[]
    for i in range(len(mat1)):
        row_mat_sum = []
        for j in range(len(mat2_new)):
            sum_temp=0
            for a, b in zip(mat1[i],mat2_new[j]):
                sum_temp+=(a*b)
            row_mat_sum.append(sum_temp)
        mat_sum.append(row_mat_sum)

    return mat_sum





mat1 = [
        [1, 2, 3],
        [4, 5, 6],
    ]
mat2 = [
        [7, 8],
        [9, 10],
        [11, 12],
    ]

print(multiply_matrices(mat1,mat2))