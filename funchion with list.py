num = [1, 2, 3, 44, 45, 46, 47, 48, 25, 67, 89, 100, 98, 97]
num1 = [31, 32, 38, 33, 344, 345, 346, 347, 348, 325, 367, 389, 1300, 398, 397]


# even_number_list = []
# for number in num:
#     if number % 2 == 0:
#         even_number_list.append(number)
# print(even_number_list)
def even_number_finder(number_list):
    even_number_list = []
    for number in number_list:
        if number % 2 == 0:
            even_number_list.append(number)
    return even_number_list

even_list1 = even_number_finder(num)
even_list2 = even_number_finder(num1)
print(even_list1)
print(even_list2)


