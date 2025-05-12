def tinh_tong_chan(lst):
    tong = 0
    for i in lst:
        if (i % 2 == 0): tong += i
    return tong

numbers_list = list(map(int, input("Nhap danh sach cac so, cach nhau bang dau phai: ").split(',')))
tong_chan = tinh_tong_chan(numbers_list)
print("Tong cac so chan trong list: ", tong_chan)