def chia_het_cho_5(num):
    # Chuyển sang nhị phân
    so_thap_phan = int(num, 2)
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
    
chuoi_so_nhi_phan = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ")
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
so_chia_het_cho5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]

if (len(so_chia_het_cho5) > 0):
    ketqua = ','.join(so_chia_het_cho5)
    print("Các số nhị phân chia hết cho 5 là: ", ketqua)
else:
    print("Không có số nhị phân nào chia hết cho 5 trong chuỗi đã nhập")