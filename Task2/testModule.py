import math

def HHCN():
    chieu_dai=float(input("nhap chieu dai:"))
    chieu_rong=float(input("nhap chieu rong:"))
    chieu_cao=float(input("nhap chieu cao:"))
    dien_tich_xung_quanh=2*chieu_cao*(chieu_dai+chieu_rong)
    dien_tich_toan_phan=dien_tich_xung_quanh + 2*chieu_dai*chieu_rong
    print("dien tich xung quanh hhcn",dien_tich_xung_quanh)
    print("dien tich toan phan hhcn",dien_tich_toan_phan)