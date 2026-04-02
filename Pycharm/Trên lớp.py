#Trên.lớp
# n = int(input("Input number:"))
# sum = 0
# i = 1
# k = n
# for k in range(0,n):
#     print("", n)
#     sum += n
#     n -= 1
# print("Start!!!")
# print("Sum =", sum)
# print("Bảng cưu chương của %i:" %k)
# for i in range(1,k+1):
#     k*i
#     print("\t%i * %2i = %2i" %(k,i,k*i))

#******PHẦN PHỤ KHÁC******

# tieptuc = True
# while tieptuc:
#     chon=int(input("Bạn muốn làm gì?\n1. Hình Tam Giác\n2. Hình chữ nhật\n3. Tính trung bình"))
#     if chon == 1:
#         n = int(input("Input number:"))
#         for i in range(1,n+1):
#             print("*"*i)
#     if chon == 2:
#         cd = int(input("Chiều dài:"))
#         cr = int(input("Chiều rộng:"))
#         for i in range(cr):
#             print("* "*cd)
#     if chon == 3:
#         n = int(input("Bạn muốn nhập bao nhiêu số:"))
#         tong = 0
#         for i in range (1, n + 1):
#             so = int(input("Mời bạn nhập số thứ %i: " %i))
#             tong += so/n
#         print("Giá trị trung bình:", tong)
#     else:
#         print("Vui lòng nhập số từ 1 đến 3:")
#         continue
#     hoi = int(input("Bạn muốn tiếp tục không?\n1. Yes\n2. No"))
#     if hoi == 1:
#         continue
#     else:
#         break

chuoi = "trung Tam Tin Hoc"
# print(chuoi.capitalize())
# print(chuoi.upper())
# print(chuoi.lower())

# print(len(chuoi))

# print(chuoi.center(30, "-"))
# print(chuoi.ljust(30, "-"))
# print(chuoi.rjust(30, "-"))

# print(chuoi.count("t"))
# print(chuoi.find("z"))


# du_lieu = input("Nhập: ")
# if du_lieu.isdigit():
#     print("Là số")
# else:
#     print("Không là số")


# list_so = [4,7,2,8,0]
# print(len(list_so))




ho_ten = "Nguyễn Thị Bé Ba"
# Họ: Nguyễn
# Tên: Ba
# Tên lót: Thị Bé

# tach_chuoi = ho_ten.split()  # list

# Họ
# print("Họ:", tach_chuoi[0])

# Tên
# chieu_dai_list = len(tach_chuoi)
# print("Tên:", tach_chuoi[chieu_dai_list - 1])

# Tên lót
# Cách 1
# ten_lot = ""
# for i in range(1, chieu_dai_list - 1):
#     ten_lot = ten_lot + tach_chuoi[i] + " "
# else:
#     print("Tên lót:", ten_lot)

# Cách 2
# ten_lot = ho_ten.replace(tach_chuoi[0], "").replace(tach_chuoi[chieu_dai_list - 1], "").strip()
# print("Tên lót:", ten_lot)

# Cách 3
# ten_lot = " ".join(tach_chuoi[1: chieu_dai_list - 1])
# print("Tên lót:", ten_lot)




chuoi = "trung tâm tin học"  # => Trung Tâm Tin Học
print(chuoi)

tach_chuoi = chuoi.split()   # => list

chuoi_xu_ly = ""
for tu in tach_chuoi:
    chuoi_xu_ly += tu.capitalize() + " "
else:
    print(chuoi_xu_ly)


print(chuoi.title())


