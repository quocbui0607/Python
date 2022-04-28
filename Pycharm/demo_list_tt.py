import calendar


# danhSachPhim = ["Cuốn theo chiều gió",
#                 "Chiến tranh và hòa bình",
#                 "Titanic",
#                 "The bad, the good and the ugly",
#                 "Star war",
#                 "Iron man"]
#
#
# while True:
#     # ĐIỀU KIỆN 1: CHỌN CHỨC NĂNG
#     chuc_nang = int(input("\nBạn muốn làm gì?\n1. In danh sách phim\n2. Thêm phim mới\n"
#                           "3. Cập nhật phim\n4. Xóa phim\n=> "))
#
#     if chuc_nang == 1:
#         # In danh sách phim
#         tieu_de = "DANH SÁCH CÁC PHIM (" + str(len(danhSachPhim)) + ")"
#         print(tieu_de.center(40))
#         for phim in danhSachPhim:
#             stt = danhSachPhim.index(phim) + 1
#             print(str(stt) + ". " + phim)
#
#     elif chuc_nang == 2:
#         while True:
#             # Nhập tên phim
#             ten_phim = input("Nhập tên phim mới (dừng lại => bấm phím s): ")
#             if ten_phim == "s" or ten_phim == "S":
#                 # In danh sách phim nếu như không nhập nữa
#                 tieu_de = "DANH SÁCH CÁC PHIM (" + str(len(danhSachPhim)) + ")"
#                 print(tieu_de.center(40))
#                 for phim in danhSachPhim:
#                     stt = danhSachPhim.index(phim) + 1
#                     print(str(stt) + ". " + phim)
#
#                 # Dừng vòng lặp
#                 break
#             else:
#                 # Thêm phim vào list
#                 danhSachPhim.append(ten_phim)
#
#     elif chuc_nang == 3:
#         print()
#         # In danh sách phim
#         tieu_de = "DANH SÁCH CÁC PHIM (" + str(len(danhSachPhim)) + ")"
#         print(tieu_de.center(40))
#         for phim in danhSachPhim:
#             stt = danhSachPhim.index(phim) + 1
#             print(str(stt) + ". " + phim)
#
#         # Cập nhật
#         stt = int(input("\nBạn muốn cập nhật phim nào? Vui lòng nhập STT: "))
#         ten_phim = input("Nhập tên phim mới: ")
#         danhSachPhim[stt - 1] = ten_phim
#
#         print()
#         # In danh sách phim
#         tieu_de = "DANH SÁCH CÁC PHIM (" + str(len(danhSachPhim)) + ")"
#         print(tieu_de.center(40))
#         for phim in danhSachPhim:
#             stt = danhSachPhim.index(phim) + 1
#             print(str(stt) + ". " + phim)
#
#     elif chuc_nang == 4:
#         print()
#         # In danh sách phim
#         tieu_de = "DANH SÁCH CÁC PHIM (" + str(len(danhSachPhim)) + ")"
#         print(tieu_de.center(40))
#         for phim in danhSachPhim:
#             stt = danhSachPhim.index(phim) + 1
#             print(str(stt) + ". " + phim)
#
#         # Xóa phim
#         stt = int(input("\nBạn muốn xóa phim nào? Vui lòng nhập STT: "))
#         print("Phim '" + danhSachPhim.pop(stt - 1) + "' đã được xóa thành công!")
#
#         print()
#         # In danh sách phim
#         tieu_de = "DANH SÁCH CÁC PHIM (" + str(len(danhSachPhim)) + ")"
#         print(tieu_de.center(40))
#         for phim in danhSachPhim:
#             stt = danhSachPhim.index(phim) + 1
#             print(str(stt) + ". " + phim)
#
#     else:
#         print("Chỉ được chọn 1, 2, 3 hoặc 4")
#
#     # ĐIỀU KIỆN 2: TRẢ LỜI TIẾP TỤC ?
#     tra_loi = input("\nBạn có muốn tiếp tục nữa không? (y/n)\n=> ")
#     if tra_loi == "y" or tra_loi == "Y":
#         continue
#     else:
#         break



"""
thang = ?
nam = ?

1. Tháng <thang> năm <nam> có <bao nhiêu> ngày?
2. Năm <nam> có phải là năm nhuận không?
3. Thứ của ngày cuối cùng trong tháng <thang>/<nam> là <thứ mấy>?
"""

# Nhập liệu
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))


# 1
so_ngay = calendar.monthrange(nam, thang)[1]
print("Tháng %i năm %i có %i ngày." % (thang, nam, so_ngay))

# 2
if calendar.isleap(nam):
    print("Năm %i là năm nhuần." % nam)
else:
    print("Năm %i không là năm nhuần." % nam)

# 3
thu = calendar.weekday(nam, thang, so_ngay)
list_thu = ["Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy", "Chủ nhật"]
print("Thứ của ngày cuối cùng trong tháng %i năm %i là %s" % (thang, nam, list_thu[thu]))

