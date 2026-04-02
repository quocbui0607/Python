
def tinh_diem_tb(hk1, hk2):
    
	assert(hk1 >= 0 and hk2 >= 0), "Điểm hk1 và hk2 phải lớn hơn hoặc bằng 0"
    
	diem_tb = (hk1 + hk2 * 2) / 3
    
	return diem_tb




print(tinh_diem_tb(-2, 6.5))






def tinh_tong(a, b):
    
	assert(a + b == 6), "Không hợp lệ"
    
	return print(a+b)




tinh_tong(2, 4)
