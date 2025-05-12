def dao_nguoc_chuoi(lst):
    return lst[::-1]

numbers_list = list(map(int, input("Nhap danh sach cac so, cach nhau bang dau phai: ").split(',')))
print("Dao nguoc chuoi: ", dao_nguoc_chuoi(numbers_list))