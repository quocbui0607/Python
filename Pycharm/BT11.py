import csv
def write_file(filename, content):
    f = open(filename, "w+")
    f.write(content)
    f.close
def read_file(filename):
    f = open(filename, "r+")
    content = f.read()
    print(content)
def write_end_of_file(filename, content):
    f = open(filename, "a")
    f.write("\n")
    f.write(content)
    f.close()
def read_csv(filename):
    f = open(filename, "r")
    for item in csv.reader(f):
        print(item)
    f.close
def write_file_csv(filename):
    f = open(filename, "a", newline='')
    while True:
        ten = input("Nhập tên:\n")
        sdt = input("Nhập số điện thoại:\n")
        csv.writer(f, delimiter='\t').writerow([ten, sdt])
        x = int(input("Tiếp tục? 1: Có - 0: Không\n=> "))
        if x == 1:
            continue
        else:
            break
    f.close
def read_file_csv(filename):
    f = open(filename, "r")
    print("name\tfone")
    for item in csv.reader(f, delimiter='\t'):
        print('\t'.join(item))
    f.close

11.1
# f = open(input("Nhập tên tập tin:\n"), "r")
# print("Nội dung tập tin:")
# content = f.read()
# print(content)

11.2
# # CÁCH 1
# chars = 0
# words = 0
# lines = 0
# for line in f.readlines():
#     print(line)
#     chars += len(line)
#     words += len(line.split())
#     lines += 1
# # CÁCH 2
# # chars = 0
# # words = 1
# # lines = 1
# # for item in content:
# #     chars += 1
# #     if item == " " or item == "\n":
# #         words += 1
# #     if item == "\n":
# #         lines += 1
# print("Report: Lines/ Words/ Chars".center(37, "-"))
# print("Lines: {}, Words: {} , Chars: {}".format(lines, words, chars))
# f.close

11.3
# x = input("Nhập tên tập tin:\n")
# a = input("Nhập nội dung:\n")
# write_file(x, a)
# print("Đã ghi nội dung vào tập tin {}".format(x))
# read_file(x)

11.4
# x = input("Nhập tên tập tin:\n")
# a = input("Nhập nội dung:\n")
# write_file(x, a)
# while True:
#     k = int(input("Bạn có muốn tiếp tục ghi nội dung vào file? 1: Có; 0: Không\n"))
#     if k == 1:
#         a = input("Nhập nội dung:\n")
#         write_end_of_file(x, a)
#         continue
#     elif k == 0:
#         break
# print("Đã ghi nội dung vào tập tin {}".format(x))
# read_file(x)

11.5
# x = input("Nhập tên tập tin:\n")
# read_csv(x)

11.6
# x = input("Nhập tên tập tin:\n")
# write_file_csv(x)
# read_file_csv(x)