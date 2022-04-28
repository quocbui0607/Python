# import math
#
#
# def tinh_danh_gia_bmi(can_nang, chieu_cao):
#     # Tính BMI
#     bmi = can_nang / math.pow(chieu_cao, 2)
#     # Đánh giá BMI
#     if bmi < 18.5:
#         chuoi_kq = 'Gầy'
#     elif bmi < 25:
#         chuoi_kq = 'Bình thường'
#     else:
#         chuoi_kq = 'Thừa cân'
#
#     return bmi, chuoi_kq  # tuple
#
#
# # Nhập
# can_nang = eval(input('Nhập cân nặng (kg):\n'))
# chieu_cao = eval(input('Nhập chiều cao (m):\n'))
#
#
# # Xuất
# a, b = tinh_danh_gia_bmi(can_nang, chieu_cao)
# print('Chỉ số BMI của bạn: %s' %a)
# print('Kết quả: Bạn', b)
