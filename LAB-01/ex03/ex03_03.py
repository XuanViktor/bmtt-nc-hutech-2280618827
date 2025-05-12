def tao_tuple_tu_list(lst):
    return tuple(lst)

numbers_list = list(map(int, input("Nhap danh sach cac so, cach nhau bang dau phai: ").split(',')))
my_tuple = tao_tuple_tu_list(numbers_list)
print("List: ", numbers_list)
print("Tuple tu List: ", my_tuple)
