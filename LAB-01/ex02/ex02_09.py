def kiem_tra_so_nt(n):
    if (n < 2): return False
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True

if __name__=="__main__":
    number = int(input("Nhập số nguyên tố: "))
    if kiem_tra_so_nt(number):
        print(number, "là số nguyên tố")
    else:
        print(number, "không là số nguyên tố")
        