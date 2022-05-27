# khai bao string

from re import U


String =' Chung ta la ai  '
StringNew='conTact'

# is dung de so sanh vi tri tren bo nho
class String_method:
    
    # 1 su dung kieu pho thong
    def catchuoi():
        print(String)
        # lay cac ky tu tu chuoi
        print('ky tu dau tien:',String[1])
        print('ky tu cuoi cung:',String[-1])
        # tra ra ky tu thu 3 den ky tu 7
        print('ky tu trong khoang:', String[2:7])
        
    def noichuoi():
        print(String + StringNew)
        print('heloo'' ''moi nguoi')
        
    def lapkytu():
        count=0
        for item in String:
            if item=='o':
                count +=1
        print(count,'ky tu tim duoc trong chuoi')
        
    def kiemtrakytu():
        print('c' in String)
    
    def cacdinhdangchuoi():
        # Sử dụng ba dấu nháy
        print('''what are you doing''')   
        # truong hop nhay don
        print('He said, "What\'s there?"')
        
    def kytuthoat():
        print('xin chao' '\t' 'moi nguoi')
        print('xin chao' '\r' 'moi nguoi')
        print('xin chao' '\v' 'moi nguoi')


# 2 su dung cac ham thay the
    # Hàm strip() loại bỏ bất kỳ khoảng trắng(hoac ki tu char) từ đầu hoặc cuối cùng, 
    def loaiboSpace():
        print("Loai bo space o bat ky dau hay cuoi chuoi:")
        arr_new=String.strip()
        print(arr_new)
        
    # Ham lstrip loai bo khoang trg o dau chuoi
    def loaibofirstSpaceSequence():
        print("loai bo space o dau chuoi:")
        Str="  Hello"
        arr_new=Str.lstrip()
        print(arr_new)
    
    # Ham rstrip loai bo khoang trg o cuoi chuoi
    def loaiboEndSpaceSequence():
        print("loai bo space o cuoi chuoi:")
        Str="Hello heloo  "
        arr_new=Str.rstrip()
        print(arr_new)
       
    # Hàm lower() trả về chuỗi chữ thường  
    def Vietthuong():
        print("Viet thuong:")
        arr_new=StringNew.lower()
        print(arr_new)
        
    # Ham upper() tra ve chuoi viet hoa (viet hoa tat ca chu cai)
    def VietHoa():
        print("Viet hoa tat ca: ")
        arr_new= String.upper()
        print(arr_new)
        
    # Ham viet hoa chu cai dau tien (capitalize)
    def VietHoaChuCaiDauTien():
        print("Viet hoa chu dau: ")
        arr_new=StringNew.capitalize()
        print(arr_new)
        
    #  ham replace() thay the chuoi bang mot chuoi khac
    #  cau truc (replace('ki tu can thay','ky tu thay the'))
    def Replace():
        print("Thay the chuoi:")
        arr_new=String.replace('a','oi')
        print(arr_new)
    
    # ham cout kiem tra so ki tu lap lai
    def kiemtrakytu(a):
        print("Co",String.count(a),"ki tu", a)
    
    # Ham tim kiem chuoi trong  mang chuoi.Tra ve address cua ky tu bat dau chuoi tim dc.
    # khong co se tra ve -1
    def timkiem(a):
        print(" Vi tri ki tu dau tien tim dc la:")
        arr_new=String.find(a,1)
        print(arr_new)
    
    # Ham tim kiem chuoi trong  mang chuoi.Tra ve address cua ky tu cuoi cung tim dc
    def timkiemfinal(a):
        print(" Vi tri cua ki tu cuoi cung tim dc la:")
        arr_new=String.rfind(a,1)
        print(arr_new)
        
    #  Ham join dung de noi cac thanh phan cua cac chuoi, list voi nhau
    def Noichuoi():
        arr='*'
        print("Noi 2 Chuoi lai voi nhau ta co:",arr.join(String))
    
    # swapcase chuyen ky tu ve dg nghich dao cua no
    def inverse():
        print(" chuyen doi kt ve dg nghich dao cua no:",StringNew.swapcase())
    
    # ham split() tach chuoi thanh mot list the ky tu dc chon
    # ham splitline() tach chuoi thanh dg list theo " \n". Neu doi so la 0(false) se bo "\n" va nguoc lai.
    def tachchuoisangList(a):
        print("chuoi moi sau khi tach la:",StringNew.split(a))
        arr="Dang\nThai\nSon"
        print("Dau ra voi doi so la 0:",arr.splitlines(0))
        print("Dau ra voi doi so la 1:",arr.splitlines(1))
        
        
if __name__ == '__main__':
    print(" Vui long chon option:\n "
          "1. Xu ly string thong thuong\n"
          "2. Xu ly string theo ham da co:")
    option=int(input("Vui long nhap lua chon cua ban:"))
    if option==1:
    
        String_method.catchuoi()
        
        String_method.noichuoi()
        
        String_method.lapkytu()
        
        # tra ve theo kieu boolean
        String_method.kiemtrakytu()
        
        String_method.cacdinhdangchuoi()
        
        String_method.kytuthoat()
    elif option==2:
        String_method.loaiboSpace()
        String_method.loaibofirstSpaceSequence()
        String_method.loaiboEndSpaceSequence()
        String_method.Vietthuong()
        String_method.VietHoa()
        String_method.VietHoaChuCaiDauTien()
        String_method.Replace()
        String_method.kiemtrakytu('u')
        String_method.timkiem('u')
        String_method.timkiemfinal('u')
        String_method.Noichuoi()
        String_method.inverse()
        String_method.tachchuoisangList('n')
    
        