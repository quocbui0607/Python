5.1
def bai1(n):
    i = 1
    k = n
    sum = 0
    while n > 0:
        print("", n)
        sum += n
        n -= 1
    print("Start!!!")
    print("Sum =", sum)
    print("Bảng cưu chương của %i:" %k)
    while i <= 10:
        k*i
        print("\t%i * %2i = %2i" %(k, i, k*i))
        i += 1

5.2
def bai2(n, x):
    while n < 0:
        n = eval(input("Nhập n:"))
    S = (x**2 + 1)**n
    print("S = (x*x + 1)^2 =", S)

5.3
def bai3(n, x):
    while n < 0:
        n = eval(input("Nhập n:"))
    A = (x**2 + x + 1)**n +(x**2 - x + 1)**n
    print("A = {:,}".format(A))

5.4
def bai4(x):
    y = True
    while x < 0:
        x = int(input("Nhập x:"))
    if x <= 2:
         y = True
    else:
        for i in range(2, x):
            if x % i == 0:
                y = False
    if y:
        print("{} là số nguyên tố" .format(x))
    else:
        print("{} không là số nguyên tố" .format(x))

5.5
def bai5(n):
    while n < 0:
        n = int(input("Nhập n:"))
    A, B, C, D, E = 0, 0, 1, 1, 0
    print("A = ", end ="")
    for i in range(1, n + 1):
        if i % 2 != 0:
            A += i
            print("{} + ".format(i), end="")
    print("= {}".format(A))
    print("B = ", end="")
    for i in range(1, n + 1):
        if i % 2 == 0:
            B += i
            print("{} + ".format(i), end="")
    print("= {}".format(B))
    print("C = ", end="")
    for i in range(1, n + 1):
        C *= i
        print("{} * ".format(i), end="")
    print("= {}".format(C))
    print("D = ", end="")
    for i in range(1, n + 1):
        if i % 3 == 0:
            D *= i
            print("{} * ".format(i), end="")
    print("= {}".format(D))
    print("E = ", end="")
    def is_prime(k):
        for i in range(2, k):
            if k % i == 0:
                return False
        return True
    for i in range(2, n + 1):
        if is_prime(i):
            E += i
            print("{} + ".format(i), end="")
    print("= {}".format(E))

7.1
def bai7_1(list):
    print("Number of animals:", len(list))
    x = input("I want to find: ")
    if x in list:
        print("There is {} in list of animal".format(x))
    else:
        print("There is not {} in list of animal".format(x))

7.2
def bai7_2(x):
    danhsach = []
    danhsach.append(x)
    print("Tiếp tục nhập giá trị: 1: Có, 0: Không", end="  ")
    y = int(input(""))
    while y != 1 and y != 0:
        y = int(input("Vui lòng nhâp 1 hoặc 0:"))
    else:
        if y == 1:
            tieptuc = True
        else:
            tieptuc = False
    while tieptuc:
        x = int(input("Nhập giá trị: "))
        danhsach.append(x)
        print("Tiếp tục nhập giá trị: 1: Có, 0: Không", end="  ")
        y = int(input(""))
        while y != 1 and y != 0:
            y = int(input("Vui lòng nhâp 1 hoặc 0: "))
        if y == 1:
            tieptuc = True
            continue
        else:
            tieptuc = False
            break
    print("List:", danhsach)
    k = int(input("Nhập giá trị x cần tìm: "))
    tong = 0
    for num in danhsach:
        tong += num
    print("Tổng các giá trị trong list: ", tong)
    if k in danhsach:
        print("{} xuất hiện {} lần trong list".format(k, danhsach.count(k)))
    else:
        print("{} không xuất hiện trong danh sách".format(k))
    if max(danhsach) == k:
        print("{} lớn hơn tất cả các số trong list".format(k))
    else:
        print("{} không lớn hơn tất cả các số trong list".format(k))
    for num in danhsach:
        if num <= k:
            danhsach.remove(num)
    print("Các số lơn hơn %i trong list:" %k , danhsach)

7.3
def bai7_3(x):
    danhsach = []
    danhsach.append(x)
    print("Tiếp tục nhập giá trị: 1: Có, 0: Không", end="  ")
    y = int(input(""))
    while y != 1 and y != 0:
        y = int(input("Vui lòng nhâp 1 hoặc 0: "))
    else:
        if y == 1:
            tieptuc = True
        else:
            tieptuc = False
    while tieptuc:
        x = int(input("Nhập giá trị: "))
        danhsach.append(x)
        print("Tiếp tục nhập giá trị: 1: Có, 0: Không", end="  ")
        y = int(input(""))
        while y != 1 and y != 0:
            y = int(input("Vui lòng nhâp 1 hoặc 0:"))
        if y == 1:
            tieptuc = True
            continue
        else:
            tieptuc = False
            break
    print("List:", danhsach)
    snt = True
    dsphu = []
    for i in danhsach:
        for j in range(2, i):
            if i % j == 0:
                snt = False
                break
            else:
                snt = True
        if snt:
            dsphu.append(i)
    print("Các số nguyên tố trong list:", dsphu)
    tongam = 0
    tongduong = 0
    dsam = []
    dsphu.clear()
    for i in danhsach:
        if i < 0:
            dsam.append(i)
            tongam += i
        else:
            dsphu.append(i)
            tongduong += i
    if len(dsam) == 0:
        chia = 1
    else:
        chia = len(dsam)
    if len(dsphu) == 0:
        chia = 1
    else:
        chia = len(dsphu)
    print("Các phần tử âm trong list: {}\n Trung bình cộng các phần tử âm: {}".format(dsam,tongam/chia))
    print("Các phần tử dương trong list: {}\n Trung bình cộng các phần tử dương: {}".format(dsphu,tongduong/chia))
    print("Giá trị max trong list:", max(danhsach))
    print("Giá trị min trong list:", min(danhsach))
    danhsach.sort()
    print("List sắp tăng dần:", danhsach)

7.4
def bai7_4(tuple):
    print("Tuple:", tuple)
    x = int(input("Nhập số từ 0 đến 9: "))
    while x < 0 or x > 9:
        x = int(input("Vui lòng nhập số từ 0 đến 9: "))
    y = int(input("Nhập số từ -1 đến -9: "))
    while y > -1 or x < -9:
        y = int(input("Vui lòng nhập số từ -1 đến -9: "))
    s = input("Nhập chuỗi cần tìm: ")
    print("Tuple [%i] = %s" %(x, tuple[x]))
    print("Tuple [%i] = %s" %(y, tuple[y]))
    print("%s xuất hiện trong tuple %i lần" %(s, tuple.count(s)))

7.5
def bai7_5(a,b):
    c = a + b
    d = sorted(c)
    print("Tuple a:", a)
    print("Tuple b:", b)
    print("Tuple c:", c)
    print("Tuple d:", d)
    print("Tuple [3] =", d[3])
    print("3 phần tử cuối cùng của tuple d:", d[len(d)-3:])

7.6
def bai7_6(x):
    set1 = {x}
    k = int(input("Bạn có tiếp tục nhập cho set 1? 1: Có, 0: Không\t\t"))
    while k != 0 and k != 1:
        k = int(input("Bạn có tiếp tục nhập cho set 1? 1: Có, 0: Không\t\t"))
    if k == 1:
        tieptuc = True
    elif k != 0:
        k = int(input("Vui lòng nhập 1: Có hoặc 0: Không\t\t\t"))
    else:
        tieptuc = False
    while tieptuc:
        x = int(input("Nhập giá trị cho element trong set 1: "))
        set1.add(x)
        k = int(input("Bạn có tiếp tục nhập cho set 1? 1: Có, 0: Không\t\t"))
        while k != 0 and k != 1:
            k = int(input("Bạn có tiếp tục nhập cho set 1? 1: Có, 0: Không\t\t"))
        if k == 1:
            tieptuc = True
            continue
        elif k == 0:
            tieptuc = False
            break
    x = int(input("Nhập giá trị cho element trong set 2: "))
    set2 = {x}
    k = int(input("Bạn có tiếp tục nhập cho set 2? 1: Có, 0: Không\t\t"))
    while k != 0 and k != 1:
        k = int(input("Bạn có tiếp tục nhập cho set 2? 1: Có, 0: Không\t\t"))
    if k == 1:
        tieptuc = True
    elif k != 0:
        k = int(input("Vui lòng nhập 1: Có hoặc 0: Không\t\t\t"))
    else:
        tieptuc = False
    while tieptuc:
        x = int(input("Nhập giá trị cho element trong set 2: "))
        set2.add(x)
        k = int(input("Bạn có tiếp tục nhập cho set 2? 1: Có, 0: Không\t\t"))
        while k != 0 and k != 1:
            k = int(input("Bạn có tiếp tục nhập cho set 2? 1: Có, 0: Không\t\t"))
        if k == 1:
            tieptuc = True
            continue
        elif k == 0:
            tieptuc = False
            break
    print("Set 1:", set1)
    print("Set 2:", set2)
    print("Chiều dài set 1:", len(set1))
    print("Chiều dài set 2:", len(set2))
    print("Tổng set 1:", sum(set1))
    print("Tổng set 2:", sum(set2))
    print("Max set 1, Min set 1:", max(set1), min(set1))
    print("Max set 2, Min set 2:", max(set2), min(set2))
    print("Pop set 1:", set1.pop())
    print("Set 1 sau khi pop:", set1)
    print("Set 1 union set 2:", (set1|set2))
    print("Set 1 intersection set 2:", (set1&set2))
    print("Set 1 difference set 2:", (set1-set2))
    print("Set 1, set 2 symmetric difference:", (set1^set2))
    print("Set 1 tăng dần:", sorted(set1))
    print("Set 2 giảm dần:", sorted(set2, reverse = True))

7.7
def bai7_7(danhba):
    x = int(input("Bạn muốn làm gì?\n 1: Xem danh bạ\n 2: Tìm Kiếm\n 3: Thêm mới\n Vui lòng nhập từ 1 đến 3: "))
    while x != 1 and x != 2 and x != 3:
        x = int(input("Bạn muốn làm gì?\n 1: Xem danh bạ\n 2: Tìm Kiếm\n 3: Thêm mới"))
    if x == 1:
        print("Danh bạ điện thoại:\n")
        print("Tên\t\tSố điện thoại")
        for i in danhba:
            print("{}  --  {}".format(i,danhba[i]))
    elif x == 2:
        y = input("Nhập tên cần tìm:\n")
        print("{} có số điện thoại là: {}".format(y,danhba[y]))
    elif x == 3:
        key = input("Nhập tên:\n")
        value = input("Nhập số điện thoại:\n")
        danhba[key] = value
        print("Danh bạ điện thoại:\n")
        print("Tên\t\t Số điện thoại")
        for i in danhba:
            print("{}  --  {}".format(i,danhba[i]))
    k = int(input("Tiếp tục lựa chọn? 1.Có, 0: Không\t"))
    while k != 0 and k != 1:
        k = int(input("Vui lòng chọn: 1.Có, 0: Không\t"))
    if k == 1:
        tieptuc = True
    else:
        tieptuc = False
    while tieptuc:
        x = int(input("Bạn muốn làm gì?\n 1: Xem danh bạ\n 2: Tìm Kiếm\n 3: Thêm mới\n Vui lòng nhập từ 1 đến 3: "))
        while x != 1 and x != 2 and x != 3:
            x = int(input("Bạn muốn làm gì?\n 1: Xem danh bạ\n 2: Tìm Kiếm\n 3: Thêm mới"))
        if x == 1:
            print("Danh bạ điện thoại:\n")
            print("Tên\t\tSố điện thoại")
            for i in danhba:
                print("{}  --  {}".format(i,danhba[i]))
        elif x == 2:
            y = input("Nhập tên cần tìm:\n")
            print("{} có số điện thoại là: {}".format(y,danhba[y]))
        elif x == 3:
            key = input("Nhập tên:\n")
            value = input("Nhập số điện thoại:\n")
            danhba[key] = value
            print("Danh bạ điện thoại:\n")
            print("Tên\t\t Số điện thoại")
            for i in danhba:
                print("{}  --  {}".format(i, danhba[i]))

7.8
def bai7_8(tudien):
    x = int(input("Bạn muốn làm gì? 1: Xem từ điển; 2: Tra từ; 3: Thêm từ; 4: Xóa từ\t"))
    while x != 1 and x != 2 and x != 3 and x != 4:
        x = int(input("Vui lòng nhập số từ 1 đến 4:\t"))
    if x == 1:
        print("Dictionary:\nTừ Anh\tNghĩa Việt")
        for i in tudien:
            print("{}\t\t{}".format(i, tudien[i]))
    elif x == 2:
        y = input("Nhập từ cần tra:\t\t")
        if y in tudien:
            print("{} có nghĩa Việt là:\t{}".format(y,tudien[y]))
        else:
            print("Không tìm thấy trong từ điển")
    elif x == 3:
        key = input("Nhập từ Anh:\t")
        value = input("Nhập nghĩa Việt:\t")
        tudien[key] = value
        print("Dictionary:\nTừ Anh\tNghĩa Việt")
        for i in tudien:
            print("{}\t\t{}".format(i, tudien[i]))
    else:
        key = input("Nhập từ cần xóa:\t")
        x = int(input("Bạn có thật sự muốn xóa hay không? 1: Xóa; 0: Không\t\t"))
        if key in tudien:
            while x != 0 and x != 1:
                x = int(input("Vui lòng nhập 1: Xóa; 0: Không\t"))
            if x == 1:
                del tudien[key]
                print("Đã xóa từ trong từ điển")
                print("Dictionary:\nTừ Anh\tNghĩa Việt")
                for i in tudien:
                    print("{}\t\t{}".format(i, tudien[i]))
        else:
            print("Không có từ trong từ điển")
    k = int(input("Tiếp tục lựa chọn? 1: Có; 0: Không\t"))
    while k != 0 and k != 1:
        k = int(input("Vui lòng nhập 1: Có; 0: Không\t"))
    if k == 1:
        tieptuc = True
    else:
        tieptuc = False
    while tieptuc:
        x = int(input("Bạn muốn làm gì? 1: Xem từ điển; 2: Tra từ; 3: Thêm từ; 4: Xóa từ\t"))
        while x != 1 and x != 2 and x != 3 and x != 4:
            x = int(input("Vui lòng nhập số từ 1 đến 4:\t"))
        if x == 1:
            print("Dictionary:\nTừ Anh\tNghĩa Việt")
            for i in tudien:
                print("{}\t\t{}".format(i, tudien[i]))
        elif x == 2:
            y = input("Nhập từ cần tra:\t\t")
            if y in tudien:
                print("{} có nghĩa Việt là:\t{}".format(y, tudien[y]))
            else:
                print("Không tìm thấy trong từ điển")
        elif x == 3:
            key = input("Nhập từ Anh:\t")
            value = input("Nhập nghĩa Việt:\t")
            tudien[key] = value
            print("Dictionary:\nTừ Anh\tNghĩa Việt")
            for i in tudien:
                print("{}\t\t{}".format(i, tudien[i]))
        else:
            key = input("Nhập từ cần xóa:\t")
            x = int(input("Bạn có thật sự muốn xóa hay không? 1: Xóa; 0: Không\t\t"))
            if key in tudien:
                while x != 0 and x != 1:
                    x = int(input("Vui lòng nhập 1: Có; 0: Không\t"))
                if x == 1:
                    del tudien[key]
                    print("Đã xóa từ trong từ điển")
                    print("Dictionary:\nTừ Anh\tNghĩa Việt")
                    for i in tudien:
                        print("{}\t\t{}".format(i, tudien[i]))
            else:
                print("Không có từ trong từ điển")
        k = int(input("Tiếp tục lựa chọn? 1: Có; 0: Không\t"))
        while k != 0 and k != 1:
            k = int(input("Vui lòng nhập 1: Có; 0: Không\t"))
        if k == 1:
            tieptuc = True
            continue
        else:
            tieptuc = False
            break