"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 list bao gồm các từ bất kì
    2. 1 số tự nhiên k
    In ra các từ trong list có độ dài lớn hơn k ký tự
"""

word_list = ["apple", "banana", "cherry", "date", "monkey", "blackpink"]
k = 5

def check_word(lista,k):
    for i in range(len(word_list)):
        if len(lista[i])>k:
            print(lista[i])


check_word(word_list,k)
