dict_1 = {"one": 1, "two": 2, "three": 3, "four": 4}
# print(type(dict_1))
# print(dict_1["one"])
for i in dict_1:
    print("{} : {}".format(i, dict_1[i]))
# print("three" in dict_1)


# dict_1 = {"one": 1, "two": 2, "three": 3, "four": 4}
# print(dict_1)
# print(type(dict_1))
#
# cd = str(dict_1)
# print(cd)
# print(type(cd))


# Về nhà làm
# list_key = [1, 2, 3, 4, 5]
# list_value = ["one", "two", "three", "four", "five"]
# dict_2 = dict.fromkeys(list_key, [4, 5, 6])
# print(dict_2)


# dict_1 = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
# # a = list(dict_1.items())
# # print(a[0][0])
#
# for item in dict_1:
#     print(item, "-", dict_1.get(item))
#
# print()
#
# for key, value in dict_1.items():
#     print(key, "-", value)


Danh_ba = {
            "01235468655": "Nguyễn Văn An",
            "0909090909": "Phạm Thị Lan",
            "01234567891": "Trần Minh Ngọc",
            "0906213456": "Lê Nguyễn Hồng Đào"
}


while True:
    # ĐIỀU KIỆN 1: CHỌN CHỨC NĂNG
    chuc_nang = int(input("\nBạn muốn làm gì?\n1. In danh bạ\n2. Thêm danh bạ\n"
                          "3. Cập nhật danh bạ\n4. Xóa danh bạ\n=> "))

    if chuc_nang == 1:
        # In danh bạ
        print("SĐT".ljust(15), "HỌ TÊN".ljust(30))
        print("- " * 20)
        for sdt, ho_ten in Danh_ba.items():
            print(sdt.ljust(15), ho_ten.ljust(30))

    elif chuc_nang == 2:
        # Cách 1
        # sdt = input("Nhập vào số điện thoại: ")
        # if sdt in Danh_ba:
        #     print("Số điện thoại đã tồn tại. Không thêm được")
        # else:
        #     ho_ten = input("Nhập họ tên: ")
        #     Danh_ba[sdt] = ho_ten
        #
        #     # In danh bạ
        #     print("SĐT".ljust(15), "HỌ TÊN".ljust(30))
        #     print("- " * 20)
        #     for sdt, ho_ten in Danh_ba.items():
        #         print(sdt.ljust(15), ho_ten.ljust(30))

        # Cách 2
        sdt = input("Nhập vào số điện thoại: ")
        if sdt in Danh_ba:
            print("Số điện thoại đã tồn tại. Không thêm được")
        else:
            ho_ten = input("Nhập họ tên: ")
            Danh_ba_moi = {sdt: ho_ten}
            Danh_ba.update(Danh_ba_moi)

            # In danh bạ
            print("SĐT".ljust(15), "HỌ TÊN".ljust(30))
            print("- " * 20)
            for sdt, ho_ten in Danh_ba.items():
                print(sdt.ljust(15), ho_ten.ljust(30))

    elif chuc_nang == 3:
        sdt = input("Nhập vào số điện thoại: ")
        if sdt in Danh_ba:
            ho_ten = input("Nhập họ tên cập nhật: ")
            Danh_ba[sdt] = ho_ten

            # In danh bạ
            print("SĐT".ljust(15), "HỌ TÊN".ljust(30))
            print("- " * 20)
            for sdt, ho_ten in Danh_ba.items():
                print(sdt.ljust(15), ho_ten.ljust(30))

        else:
            print("Số điện thoại không tồn tại. Không cập nhật được.")

    elif chuc_nang == 4:
        sdt = input("Nhập vào số điện thoại: ")
        if sdt in Danh_ba:
            del Danh_ba[sdt]
            print("Số điện thoại '" + sdt + "' đã được xóa thành công.")

            # In danh bạ
            print("SĐT".ljust(15), "HỌ TÊN".ljust(30))
            print("- " * 20)
            for sdt, ho_ten in Danh_ba.items():
                print(sdt.ljust(15), ho_ten.ljust(30))

        else:
            print("Số điện thoại không tồn tại. Không xóa được.")

    else:
        print("Chỉ được chọn 1, 2, 3 hoặc 4")

    # ĐIỀU KIỆN 2: TRẢ LỜI TIẾP TỤC ?
    tra_loi = input("\nBạn có muốn tiếp tục nữa không? (y/n)\n=> ")
    if tra_loi == "y" or tra_loi == "Y":
        continue
    else:
        break
