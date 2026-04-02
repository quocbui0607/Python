list_so = [4, 8, 3, 5, -6, 11, 25, 1, 7, -9]

# Tính tổng các phần tử trong list
from functools import reduce
from operator import add
tinh_tong = reduce(add, list_so)
print("Tổng:", tinh_tong)


# List các số lớn hơn x
x = int(input("Nhập x: "))
list_so_lon_hon_x = list(filter(lambda item: item > x, list_so))
print("Danh sách số lớn hơn x:", list_so_lon_hon_x)


# List các phần tử âm
list_phan_tu_am = list(filter(lambda item: item < 0, list_so))
print("Danh sách phần tử âm:", list_phan_tu_am)


# List các phần tử dương
list_phan_tu_duong = list(filter(lambda item: item > 0, list_so))
print("Danh sách phần tử dương:", list_phan_tu_duong)


# Số nguyên tố
def la_so_nguyen_to(so):
    if so < 2:
        return False
    else:
        for i in range(2, so):
            if so % i == 0:
                return False
                break
        else:
            return True

# list_so_nguyen_to_1 = list(filter(la_so_nguyen_to, list_so))
list_so_nguyen_to_2 = list(filter(lambda item: la_so_nguyen_to(item), list_so))
print("Danh sách số nguyên tố:", list_so_nguyen_to_2)
