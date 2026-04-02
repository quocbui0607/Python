# a = 24
# b = int(input("Nhập b: "))
# thuong = a / b
# print("%i : %i = %.1f" %(a, b, a/b))


try:
    a = 24
    b = int(input("Nhập b: "))
    thuong = a / b
    print("%i : %i = %.1f" %(a, b, a/b))
except ZeroDivisionError as loi_1:
    print("Lỗi 1:", loi_1)
except ValueError as loi_2:
    print("Lỗi 2:", loi_2)
except Exception as loi:    # Luôn khai báo cuối cùng
    print("Nhãn lỗi:", type(loi).__name__)
    print("Mô tả:", loi)


