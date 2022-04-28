6.1
# import math
# try:
#     a, b, c, d = eval(input("Nhập a, b, c, d: "))
#     if a < 0 or b < 0 or c < 0 or d < 0:
#         raise ValueError("Nhập a,b,c,d > 0")
# except ValueError as e:
#     print("Error:", e)
# else:
#     print("Max = ", max(a, b, c, d))
#     print("Min = ", min(a, b, c, d))

6.2
# try:
#     x = int(input("Nhập x: "))
#     abs_x = x
#     if abs_x < 0:
#         abs_x = -abs_x
#     print("|%i| =" % x, abs_x)
# except ValueError as er:
#     print("Error:", er)

6.3
# try:
#     x = int(input("Nhập x: "))
#     if x < 0:
#         raise ValueError("Nhập x > 0")
#     n = int(input("Nhập n: "))
#     if n < 0:
#         raise ValueError("Nhập n > 0")
# except ValueError as e:
#     print("Error: ", e)
# else:
#     A = pow(x**2 + 1, n)
#     print("A = ", A)

6.4
# try:
#     x = int(input("Nhập x: "))
#     if x < 0:
#         raise ValueError("Nhập x > 0")
#     n = int(input("Nhập n: "))
#     if n < 0:
#         raise ValueError("Nhập n > 0")
# except ValueError as e:
#     print("Error:", e)
# else:
#     A = pow(pow(x,2) + x + 1, n) + pow(pow(x,2) - x + 1, n)
#     print("A = ", A)

6.5
# import math
# print("Giải phương trình bậc 2: ax^2 + bx + c = 0")
# a = float(input("Nhập a:"))
# b = float(input("Nhập b:"))
# c = float(input("Nhập c:"))
# if a == 0:
# 	print("Phương trình bậc I: bx + c = 0")
# 	if b == 0 and c != 0:
# 		print("Phương trình vô nghiệm")
# 	elif b == 0 and c == 0:
# 		print("Phương trình vô số nghiệm")
# 	else:
# 		print("Phương trình có nghiệm x = -c/b = ", -c/b)
# else:
#     delta = pow(b,2) - 4*a*c
#     if delta < 0:
#         print("Phương trình vô nghiệm")
#     elif delta == 0:
#         x = -b/(2*a)
#         print("Phương trình có nghiệm kép: x1 = x2 = -b/2a = ", x)
#     else:
#         x1 = (-b + math.sqrt(delta))/(2*a)
#         x2 = (-b - math.sqrt(delta))/(2*a)
#         print("Phương trình có nghiệm x1 = ", x1)
#         print("Phương trình có nghiệm x2 = ", x2)

6.6
# s = input("Chuỗi s: ")
# s_sub = input("Chuỗi s_sub: ")
# s_find = input("Chuỗi s_find: ")
# s_replace = input("Chuỗi s_replace: ")
# s1 = s
# print("Chuỗi s:", s)
# s1 = s.strip()
# print("Chuỗi s sau khi loại bỏ khoảng trắng:", s1)
# s1 = s.strip().capitalize()
# print("Chuỗi viết hoa ký tự đầu:", s1)
# s1 = s.count(s_sub)
# print("Số lần s_sub xuất hiện trong s:", s1)
# s1 = s.strip().capitalize().replace(s_find,s_replace)
# print("Chuỗi s sau khi tìm kiếm và thay thế:", s1)

6.7
# import datetime
# import calendar
# try:
#     ngay = int(input("Nhập ngày: "))
#     if ngay < 0:
#         raise ValueError("Ngày phải > 0")
#     thang = int(input("Nhập tháng: "))
#     if thang < 0:
#         raise ValueError("Tháng phải > 0")
#     nam = int(input("Nhập năm: "))
#     if nam < 0:
#         raise ValueError("Năm phải > 0")
# except ValueError as e:
#     print("Error: ", e)
# else:
#     x = datetime.datetime(nam, thang, ngay)
#     print("Ngày tháng năm vừa nhập: " , x.strftime('%d-%m-%Y'))
#
#     if calendar.isleap(nam):
#         print("Năm %i là năm nhuận" % nam)
#     else:
#         print("Năm %i không là năm nhuận" % nam)
#
#     k = calendar.weekday(nam,thang,ngay)
#     if k==0: print("{} là Thứ Hai".format(x.strftime('%d-%m-%Y')))
#     elif k==1: print("{} là Thứ Ba".format(x.strftime('%d-%m-%Y')))
#     elif k==2: print("{} là Thứ Tư".format(x.strftime('%d-%m-%Y')))
#     elif k==3: print("{} là Thứ Năm".format(x.strftime('%d-%m-%Y')))
#     elif k==4: print("{} là Thứ Sáu".format(x.strftime('%d-%m-%Y')))
#     elif k==5: print("{} là Thứ Bảy".format(x.strftime('%d-%m-%Y')))
#     elif k==6: print("{} là Thứ Chủ Nhật".format(x.strftime('%d-%m-%Y')))
#
#     if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
#         print("Số ngày trong tháng %i là:" %thang, 31)
#     if thang == 4 or thang == 6 or thang == 9 or thang == 11:
#         print("Số ngày trong tháng %i là:" % thang, 30)
#     if thang == 2 and calendar.isleap(nam):
#         print("Số ngày trong tháng %i là:" % thang, 29)
#     elif thang == 2 and not(calendar.isleap(nam)):
#         print("Số ngày trong tháng %i là:" % thang, 28)