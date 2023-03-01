
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# st = 'Create a list of the first letters of every word in this string'
# st =st.split()
# print(st)
# a = []
# for i in st:
#     a.append(i[0])
#
# print(a)

# from string import ascii_uppercase
#
#
# print(x := [i for i in ascii_uppercase[:int(input())]])

#
# phrase = 'Take only the words that start with t in this sentence'
# print([i for i in phrase.split() if i[0] == 't' or i[0] == 'T'])

# i_love_none = [None] * 50
# print(i_love_none)

# a = (1,)
# b = ('R',)
# c = ('A',)
# d = (2,)
# result = (a*3+ b*5+ c*8+ d*5)
# print(result)

# a = 8
# b = 11
# a = tuple(range(a, b))
# print(a)

# n = int(input())
# a = tuple([i for i in range(n, n*n+1) if i%2 != 0])
# print(a)

# my_tuple = (32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45, 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34, 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68, 56, 26, 39, 34, 50, 10, 12, 3, 27)
# print(my_tuple[44])
# print(my_tuple[-10])


# my_tuple = (32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45, 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34, 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68, 56, 26, 39, 34, 50, 10, 12, 3, 27)
#
# slice_5_10 = my_tuple[5:11]
# slice_from_20 = my_tuple[20:]
# slice_to_35 =my_tuple[0:35]
#
# print(slice_5_10)
# print(slice_from_20)
# print(slice_to_35)

# a = int(input())
# dict_1 = {}
# for i in range(a):
#     b = input()
#     if b in dict_1:
#         dict_1[b] +=1
#         print(f'{b}{dict_1[b]}', sep='')
#     else:
#         dict_1.setdefault(b, 0)
#         print('OK')

user = {
    "id": 4170,
    "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
    "password": "SyUpfo1ljm",
    "first_name": "Teresa",
    "last_name": "Wehner",
    "username": "teresa.wehner",
    "email": "teresa.wehner@email.com",
    "gender": "Non-binary",
    "phone_number": "+674 424.561.2776",
    "social_insurance_number": "637316241",
    "date_of_birth": "1993-08-17"
}
user.pop(password)



