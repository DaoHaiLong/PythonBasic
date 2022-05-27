
String="xin chao moi nguoi"
def methods():
    a=int(input("nhap so thu 1:"))
    b=int(input("nhap so thu 2:"))
    if a==b:
        print(" so thu nhat bang so thu 2")
    elif a>b:
        print("so thu 1 lon hon so thu 2 ")
    else:
        print("so thu 1 nho hon so thu 2")
        
def lapkytu():
    count=0
    kytu=str(input("vui long nhap ky tu can tim:"))
    for item in String:
        if item==kytu:
            count +=1
            print(count,'ky tu tim duoc trong chuoi')  
        else:
            print("ko co ki tu nao trong chuoi",count)
            break
def forChuoi():
    chuoi=['chao','moi','nguoi']
    for item in chuoi:
        print('xin',item)
        
def whileloop():
    couts=0
    while couts<=100:
        couts +=1
        if couts==50:
            continue
        print(couts,'.''Xin Chao Moi Nguoi')
    else:
      print("bye")
        
   
if __name__ == '__main__':
    print(" Vui long chon phuong thuc\n")
    print("1: Method if else:")
    print("2: Kiem tra ky tu ")
    print("3: while loop ")
    print("4: for loop mang")
    option=int((input("moi nhap:")))
    if option==1:
        methods()
    elif option==2:
        lapkytu()
    elif option==3:
        whileloop()
    elif option==4:
        forChuoi()
    else:
        exit()
        
            
            
        
