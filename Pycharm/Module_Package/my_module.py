def tinh_diem_tb(hk1, hk2):
    dtb = (hk1 + hk2 * 2) / 3
    return dtb


def tinh_bmi(can_nang, chieu_cao):
    bmi = can_nang / math.pow(chieu_cao, 2)
    return bmi


tinh_binh_phuong = lambda item: item ** 2

tong = lambda item1, item2: item1 + item2

hieu = lambda item1, item2: item1 - item2

pi = 3.14

loi_chao = "Chào các bạn."



def tinh_tong():
    return 4 + 5 + 6