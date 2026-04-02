4.1
# print("Nhập a,b,c,d:")
# a = eval(input())
# b = eval(input())
# c = eval(input())
# d = eval(input())
# max = -999999
# if max < a:
#     max = a
# if max < b:
#     max = b
# if max < c:
#     max = c
# if max < d:
#     max = d
# min = 999999
# if min > a:
#     min = a
# if min > b:
#     min = b
# if min > c:
#     min = c
# if min > d:
#     min = d
# print("Max =", max)
# print("Min =", min)

4.2
# try:
#     x = int(input("Nhập x: "))
#     abs_x = x
#     if abs_x < 0:
#         abs_x = -abs_x
#     print("|%i| =" % x, abs_x)
# except ValueError as er:
#     print("Error:", er)

4.3
# class Loinhaplieu(ValueError):
#     def __init__(self, thong_bao):
#         self.thong_bao = thong_bao
# try:
#     xe = int(input("Loại xe (chỉ nhập 4 chỗ hoặc 7 chỗ): "))
#     if xe < 0:
#         raise Loinhaplieu('xe must be > 0')
#     km = int(input("Số km di chuyển: "))
#     if km < 0:
#         raise Loinhaplieu('km must be > 0')
#     tg = int(input("Thời gian chờ (làm tròn theo phút): "))
#     if tg < 0:
#         raise Loinhaplieu('tg must be > 0')
# except Loinhaplieu as er:
#     print("Error:", er.thong_bao)
# if tg > 5:
#     x = (tg - 5) * 750
# print("Tiền chờ =", x)
# if xe == 4:
#     c1 = 11000
#     c2 = 15300
#     c3 = 12100
#     if km <= 0.8:
#         print("Tiền di chuyển =", c1)
#         print("Tiền cước = %i + %i =" % (c1, x), c1 + x)
#     elif km > 0.8 and km <= 30.0:
#         y = c1 + (km - 0.8) * c2
#         print("Tiền di chuyển =", y)
#         print("Tiền cước = %i + %i =" % (y, x), y + x)
#     elif km > 30:
#         y = c1 + (30 - 0.8) * c2 + (km - 30) * c3
#         print("Tiền di chuyển =", y)
#         print("Tiền cước = %i + %i =" % (y, x), y + x)
# else:
#     if xe == 7:
#         c1 = 12000
#         c2 = 16100
#         c3 = 13800
#     if km <= 0.8:
#         print("Tiền di chuyển =", c1)
#         print("Tiền cước = %i + %i =" % (c1, x), c1 + x)
#     elif km > 0.8 and km <= 30.0:
#         y = c1 + (km - 0.8) * c2
#         print("Tiền di chuyển =", y)
#         print("Tiền cước = %i + %i =" % (y, x), y + x)
#     elif km > 30:
#         y = c1 + (30 - 0.8) * c2 + (km - 30) * c3
#         print("Tiền di chuyển =", y)
#         print("Tiền cước = %i + %i =" % (y, x), y + x)

4.4
# try:
#     x = eval(input("Số kW tiêu thụ: "))
#     if x < 0:
#         raise ValueError("Kw phải lớn hơn 0")
# except ValueError as a:
#     print("Error:", a)
# else:
#     if x <= 50:
#         y = x * 1484
#         print("Tiền điện phải trả:",y)
#     elif x > 50 and x <= 100:
#         y = 50 * 1484 + (x-50) * 1533
#         print("Tiền điện phải trả:", y)
#     elif x > 100 and x <= 200:
#         y = 50 * 1484 + 50 * 1533 + (x-100) * 1786
#         print("Tiền điện phải trả:", y)
#     elif x > 200 and x <= 300:
#         y = 50 * 1484 + 50 * 1533 + 100 * 1786 + (x-200) * 2242
#         print("Tiền điện phải trả:", y)
#     elif x > 300 and x <= 400:
#         y = 50 * 1484 + 50 * 1533 + 100 * 1786 + 100 * 2242 + (x-300) * 2503
#         print("Tiền điện phải trả:", y)
#     elif x > 400:
#         y = 50 * 1484 + 50 * 1533 + 100 * 1786 + 100 * 2242 + 100 * 2503 + (x-400) * 2587
#         print("Tiền điện phải trả:", y)

4.5
# try:
#     phong = eval(input("Nhập loại phòng: "))
#     if phong <= 0:
#         raise ValueError("Phòng phải lớn hơn 0")
#     dem = eval(input("Nhập số đêm: "))
#     if dem <= 0:
#         raise ValueError("Đêm phải lớn hơn 0")
# except ValueError as a:
#     print("Error:", a)
# else:
#     if phong == 1:
#         y = 1260000
#     elif phong == 2:
#             y = 1550000
#     elif phong == 3:
#             y = 1830000
#     elif phong == 4:
#             y = 1830000
#     elif phong == 5:
#             y = 2120000
#     elif phong == 6:
#             y = 2120000
#     elif phong == 7:
#             y = 2540000
#     elif phong == 8:
#             y = 4800000
#     if dem == 2 or dem == 3:
#          y = y * 0.75 * dem
#     elif dem >= 4:
#         y = y * 0.7 * dem
#     print("Thành tiền =",y)