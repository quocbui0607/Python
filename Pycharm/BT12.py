12.1
# x = input("Nhập tên:\n")
# y = int(input("Nhập tuổi:\n"))
# print("Năm {} 100 tuổi là: {}".format(x, (2019-y) + 100))

12.2
# x = int(input("Nhập số:\n"))
# if x % 2 == 0:
#     print("{} là số chẵn".format(x))
# else:
#     print("{} là số lẻ".format(x))

12.3
# import math
# x = float(input("Nhập diện tích:\n"))
# r = lambda x: math.sqrt(x/math.pi)
# print("Bán kính hình tròn: ", r(x))

12.4
# x = float(input("Nhập số tiền phải trả:\n"))
# y = int(input("Nhập thuế:\n1: 10%\n2: 20%\n=> "))
# while True:
#     if y == 1:
#         thue = x*0.1
#         break
#     elif y == 2:
#         thue = x*0.2
#         break
#     else:
#         y = int(input("Nhập thuế:\n1: 10%\n2: 20%\n=> "))
#         continue
# z = int(input("Nhập tip:\n1: 5%\n2: 10%\n=> "))
# while True:
#     if z == 1:
#         tip = (x + thue)*0.05
#         break
#     elif z == 2:
#         tip = tip = (x + thue)*0.1
#         break
#     else:
#         z = int(input("Nhập tip:\n1: 5%\n2:10%\n=> "))
#         continue
# print("Thuế phải trả: {:,}".format(thue))
# print("Tip: {:,}".format(tip))
# print("Tổng số tiền cần thanh toán: {:,}".format(x + thue + tip))

12.5
# from calendar import isleap
# x = int(input("Nhập ngày:\n"))
# y = int(input("Nhập tháng:\n"))
# z = int(input("Nhập năm:\n"))
# if y > 12 or y < 0:
#     print("Ngày tháng năm không hợp lệ")
# if y == 1 or y == 3 or y == 5 or y == 7 or y == 8 or y == 10 or y == 12:
#     if x > 31 or x < 0:
#         print("Ngày tháng năm không hợp lệ")
#     else:
#         print("Ngày tháng năm hợp lệ")
# elif y == 4 or y == 6 or y == 9 or y == 11:
#     if x > 30 or x < 0:
#         print("Ngày tháng năm không hợp lệ")
#     else:
#         print("Ngày tháng năm hợp lệ")
# else:
#     if isleap(z):
#         if x > 29 or x < 0:
#             print("Ngày tháng năm không hợp lệ")
#         else:
#             print("Ngày tháng năm hợp lệ")
#     else:
#         if x > 28 or x < 0:
#             print("Ngày tháng năm không hợp lệ")
#         else:
#             print("Ngày tháng năm hợp lệ")

12.6
# x = input("Nhập tên người chơi 1:\n")
# y = input("Nhập tên người chơi 2:\n")
# print("Game Start!!!")
# while True:
#     nguoichoi1 = input("Nhập Scissor hoặc Rock hoặc Paper:\n=> ")
#     nguoichoi2 = input("Nhập Scissor hoặc Rock hoặc Paper:\n=> ")
#     if nguoichoi1 == nguoichoi2:
#         print("Hòa")
#     elif nguoichoi1 == "Scissor" and nguoichoi2 == "Paper":
#         print("Người chơi 1 thắng")
#     elif nguoichoi1 == "Rock" and nguoichoi2 == "Scissor":
#         print("Người chơi 1 thắng")
#     elif nguoichoi1 == "Paper" and nguoichoi2 == "Rock":
#         print("Người chơi 1 thắng")
#     else:
#         print("Người chơi 2 thắng")
#     z = int(input("Hai bạn có muốn chơi tiếp hay không? 1: Có; 0: Không\n=> "))
#     while z != 0 and z != 1:
#         z = int(input("Hai bạn có muốn chơi tiếp hay không? 1: Có; 0: Không\n=> "))
#     if z == 1:
#         continue
#     elif z == 0:
#         break

12.7
print("*"*35 + "\n" + "Tính thuế thu nhập cá nhân".center(34) + "\n" + "*"*35 + "\n\n")
mst = input("Mã số thuế: ")
hoten = input("Họ tên đối tượng nộp thuế: ")
thunhap = float(input("Tổng thu nhập trong năm: "))
nguoiphuthuoc = float(input("Số người phụ thuộc: "))
giamtru = 108000000 + (3600000 * 12 * nguoiphuthuoc)
tienchiuthue = thunhap - giamtru
if tienchiuthue <= 60000000:
  thuephainop = tienchiuthue*0.05
elif tienchiuthue > 60000000 and tienchiuthue <= 120000000:
  thuephainop = 60000000*0.05 + (tienchiuthue - 60000000)*0.1
elif tienchiuthue > 120000000 and tienchiuthue <= 216000000:
  thuephainop = 60000000*0.05 + 60000000*0.1 + (tienchiuthue - 120000000)*0.15
elif tienchiuthue > 216000000 and tienchiuthue <= 384000000:
  thuephainop = 60000000*0.05 + 60000000*0.1 + 96000000*0.15 + (tienchiuthue - 216000000)*0.20
elif tienchiuthue > 384000000 and tienchiuthue <= 624000000:
  thuephainop = 60000000*0.05 + 60000000*0.1 + 96000000*0.15 + 168000000*0.2 + (tienchiuthue - 384000000)*0.25
elif tienchiuthue > 624000000 and tienchiuthue <= 960000000:
  thuephainop = 60000000*0.05 + 60000000*0.1 + 96000000*0.15 + 168000000*0.2 + 240000000*0.25 + (tienchiuthue - 624000000)*0.3
elif tienchiuthue > 960000000:
  thuephainop = 60000000*0.05 + 60000000*0.1 + 96000000*0.15 + 168000000*0.2 + 240000000*0.25 + 336000000*0.3 + (tienchiuthue - 960000000)*0.35
if tienchiuthue <= 0:
  tienchiuthue = 0
  thuephainop = 0
print("\n")
print("Kết quả:".center(34,"-"))
print("Số tiền giảm trừ: {:,} VNĐ".format(giamtru))
print("Số tiền chịu thuế: {:,} VNĐ".format(tienchiuthue))
print("Tiền thuế phải nộp: {:,} VNĐ".format(thuephainop))

12.8
# n = int(input("Nhập n:\n"))
# X = []
# giaithua = 1
# for i in range(1, n + 1):
#     X.append(i)
#     giaithua *= i
#     if i == n:
#         print("{}".format(i), end="")
#     else:
#         print("{} x ".format(i), end="")
# print(" =", giaithua)
# giaithua2 = 1
# for i in range(1, n + 1):
#     if n % 2 == 0:
#         if i == n:
#             giaithua2 *= X[i - 1]
#             print("{}".format(X[i-1]), end="")
#         elif X[i-1] % 2 == 0:
#             print("{} x ".format(X[i-1]), end="")
#             giaithua2 *= X[i - 1]
#     elif n % 2 == 1:
#         if i == n:
#             giaithua2 *= X[i - 1]
#             print("{}".format(X[i-1]), end="")
#         elif X[i-1] % 2 == 1:
#             print("{} x ".format(X[i-1]), end="")
#             giaithua2 *= X[i - 1]
# print(" =", giaithua2)

12.9
# print("*"*60)
# print("In bảng cửu chương".center(60," "))
# print("*"*60)
# x = int(input("\nNhập số bắt đầu: "))
# y = int(input("Nhập số kết thúc: "))
# list = []
# k = x
# print("\n" + "-"*60)
# while k >= x and k <= y:
#     list.append(k)
#     k += 1
# stt = 1
# while stt < 10:
#     for j in list:
#         print("{} x {} = {}".format(j, stt, j*stt), end="\t\t")
#     print("")
#     stt += 1

12.10
# import random
# n = int(input("Nhập n: "))
# list = []
# sum = 0
# for i in range(0, n + 1):
#     k = random.randrange(0, 100)
#     list.append(k)
# print("Các phần tử trong list:",list)
# for i in list:
#     for j in range(2, i):
#         if i % j == 0:
#             snt = False
#             break
#         else:
#             snt = True
#     if snt:
#         sum += i
# print("Tổng các số nguyên tố trong list: ", sum)

12.11
# a = [2, 7, 1, 4, 8]
# print("Các cặp số quan hệ chia hết:")
# for i in range(0, len(a)):
#   for j in range(0, len(a)):
#     if a[i] % a[j] == 0 and i != j:
#         continue
#       else:
#         print("{} & {}".format(a[i], a[j]))
# print("Các cặp số có quan hệ gấp 2:")
# for i in range(0, len(a)):
#   for j in range(0, len(a)):
#     if a[i]*2 == a[j]:
#       print("{} & {}".format(a[i], a[j]))
# print("Cặp số có tổng = 8:")
# b = {}
# for i in range(0, len(a)):
#   if a[i] not in b:
#     b[8 - a[i]] = a[i]
#   else:
#     print("{} & {}".format(b[a[i]], a[i]))

12.12
# a = [4, 5, 8, 9, 13]
# b = [2, 6, 13, 7, 18, 21, 5]
# print(a)
# print(b)
# c = list(set(a) & set(b))
# print(c)
# d = list((set(a) - set(b))) + list((set(b) - set(a)))
# print(d)

12.13
# dic1 = {3: 5, 4: 6, 9: 3, 5: 2}
# dic2 = {1: 2, 2: 3}
# dic3 = {11: 9, 12: 6, 33: 1}
# dic4 = {}
# dic4.update(dic1)
# dic4.update(dic2)
# dic4.update(dic3)
# print(dic4)
# print(max(dic4.values()))
# print(min(dic4.values()))

12.14
# n = int(input("Nhập n: "))
# dic = {}
# for i in range(1, n + 1):
#     dic[i] = i*i
# print(dic)

12.15
# def string_test(s):
#     d = {"UPPER": 0, "LOWER": 0}
#     for char in s:
#         if char.isupper():
#             d["UPPER"] += 1
#         elif char.islower():
#             d["LOWER"] += 1
#         else:
#             pass
#     print("Original String:", s)
#     print("Số lượng ký tự hoa:", d["UPPER"])
#     print("Số lượng ký tự hoa:", d["LOWER"])
# x = input("Nhập chuỗi: ")
# string_test(x)