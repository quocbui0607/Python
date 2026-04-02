8.1
# def can(x):
#     a = {0: "Canh", 1: "Tân", 2: "Nhâm", 3: "Quý", 4: "Giáp", 5: "Ất", 6: "Bính", 7: "Đinh", 8: "Mậu", 9: "Kỷ"}
#     if x % 10 in a:
#         can = a[x % 10]
#     return can
# def chi(x):
#     b = {0: "Thân", 1: "Dậu", 2: "Tuất", 3: "Hợi", 4: "Tý", 5: "Sửu", 6: "Dần", 7:"Mão", 8: "Thìn", 9: "Tỵ", 10: "Ngọ", 11: "Mùi"}
#     if x % 12 in b:
#         chi = b[x % 12]
#     return chi
# k = int(input("Nhập năm:\n"))
# can = can(k)
# chi = chi(k)
# print("Năm {} âm lịch là năm {} {}".format(k, can, chi))

8.2
# x = float(input("Nhập cân nặng (kg):\n"))
# y = float(input("Nhập chiều cao (m):\n"))
# def BMI(kg, m):
#     try:
#         bmi = round(kg/pow(m, 2), 2)
#     except ZeroDivisionError as e:
#         print("Error:", e)
#     else:
#         print(" Chỉ số BMI của bạn:",bmi)
#         if bmi < 18.5:
#             print("Kết quả: Gầy")
#         elif bmi >= 18.5 and bmi <= 24.99:
#             print("Kết quả: Bình thường")
#         elif bmi >= 25:
#             print("Kết quả: Thừa cân")
#         return
# BMI(x, y)

8.3
# x = int(input("Nhập x: "))
# n = int(input("Nhập n: "))
# while n <= 0:
#     n = int(input("Nhập n lớn hơn 0: "))

# def Tính_S( x, n):
#     #5.1
#     S = pow((x**2 + 1), n)
#     return S
# print("S =", Tính_S(x, n))

# def Tính_A(x, n):
#     #5.2
#     A = pow((x**2 + x +1), n) + pow((x**2 - x +1), n)
#     return A
# print("A =", Tính_A(x, n))

# def KiểmTraSNT(x):
#     if x == 2:
#         return True
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#             break
#     return True
# if KiểmTraSNT(x):
#     print("%i là số nguyên tố" %x)
# else:
#     print("%i không là số nguyên tố" %x)

8.4
# #7.2
# danhsach = []
# def themvaolist(lst):
#     x = int(input("Nhập giá trị: "))
#     lst.append(x)
#     print("Tiếp tục nhập giá trị: 1: Có, 0: Không", end="  ")
#     y = int(input(""))
#     while y != 1 and y != 0:
#         y = int(input("Vui lòng nhâp 1 hoặc 0: "))
#     else:
#         if y == 1:
#             tieptuc = True
#         else:
#             tieptuc = False
#     while tieptuc:
#         x = int(input("Nhập giá trị: "))
#         lst.append(x)
#         print("Tiếp tục nhập giá trị: 1: Có, 0: Không", end="  ")
#         y = int(input(""))
#         while y != 1 and y != 0:
#             y = int(input("Vui lòng nhâp 1 hoặc 0: "))
#         if y == 1:
#             tieptuc = True
#             continue
#         else:
#             tieptuc = False
#             break
#     return lst
# themvaolist(danhsach)
# print("List sau khi thêm:", danhsach)
# def tonglist(lst):
#     tong = 0
#     for num in lst:
#         tong += num
#     return tong
# print("Tổng các giá trị trong list: ", tonglist(danhsach))

# #7.4
# tuple = ('red', 'green', 'yellow', 'blue', 'black', 'white', 'pink', 'orange', 'red', 'blue')
# x = input("Nhập chuỗi cần tìm: ")
# def tim_dem_slxh(a , x):
#     if x in a:
#         k = a.count(x)
#     else:
#         k = 0
#     return k
# print("Số lần xuất hiện của {} là: {}".format(x, tim_dem_slxh(tuple,x)))

# #7.6
# danhba = {'Johnny': '0989741258', 'Katherine': '0903852147', 'Misu': '0913753951', 'Jack': '0933753654'}
# def in_dict(a):
#     print("Danh bạ điện thoại:")
#     print("Tên\t\tSố điện thoại")
#     for i in a:
#         print("{}  --  {}".format(i, a[i]))
#     return
# in_dict(danhba)
# x = input("\nNhập tên cần tìm: ")
# def tim_dict(a, x):
#     if x in a:
#         print("{} : {}".format(x, a[x]))
#     else:
#         print("Không tìm thấy key search!!!")
#     return
# tim_dict(danhba, x)
# x = input("\nNhập tên: ")
# y = input("Nhập số điện thoại: ")
# def them_dict(a, key, value):
#     a[key] = value
#     in_dict(a)
#     return a
# them_dict(danhba, x, y)

8.5
# import math
# s = lambda r: math.pi * math.pow(r, 2)
# k = lambda r: math.pi * r * 2
# cv = lambda a, b: (a + b)*2
# dt = lambda a, b: a*b
# r = int(input("Nhập bán kính: "))
# a = int(input("Nhập chiều dài: "))
# b = int(input("Nhập chiều rộng: "))
# print("Chu vi hình tròn:", round(k(r),2))
# print("Diện tích hình tròn:", round(s(r),2))
# print("Chu vi hình chữ nhật:", cv(a, b))
# print("Diện tích hình chữ nhật:", dt(a, b))

8.6
# from functools import reduce
# from operator import add 
# import math
# x = int(input("Nhập giá trị: "))
# danhsach = []
# danhsach.append(x)
# print("Tiếp tục nhập giá trị: 1: Có, 0: Không", end="  ")
# y = int(input(""))
# while y != 1 and y != 0:
#     y = int(input("Vui lòng nhâp 1 hoặc 0:"))
# else:
#     if y == 1:
#         tieptuc = True
#     else:
#         tieptuc = False
# while tieptuc:
#     x = int(input("Nhập giá trị: "))
#     danhsach.append(x)
#     print("Tiếp tục nhập giá trị: 1: Có, 0: Không", end="  ")
#     y = int(input(""))
#     while y != 1 and y != 0:
#         y = int(input("Vui lòng nhâp 1 hoặc 0:"))
#     if y == 1:
#         tieptuc = True
#         continue
#     else:
#         tieptuc = False
#         break
# print("List:", danhsach)
# # tong = reduce(lambda i1, i2: i1 + i2, danhsach) #Cách 1
# tong = reduce(add, danhsach)                      #Cách 2
# print("Tổng = ", tong)
# k = int(input("Nhập giá trị x cần tìm lớn hơn: "))
# greater = list(filter(lambda i: i > k, danhsach))
# print("Danh sách các số lớn hơn {}: {}".format(k, greater))
# nums = list(filter(lambda x: x > 1, danhsach))
# print("Nums trước:", nums)
# for j in danhsach:
#   for i in range(2, j + 1):
#     nums = list(filter(lambda x: x % i or x == i, nums))
# print("Danh sách các số nguyên tố: ", nums)
# duong = list(filter(lambda i: i > 0, danhsach))
# print("Các phần tử dương trong list:", duong)
# am = list(filter(lambda i: i < 0, danhsach))
# print("Các phần tử am trong list:", am)