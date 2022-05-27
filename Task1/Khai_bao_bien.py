
def khaibao():
    print("Day la bien noi bo")
    # int
    a=10
    # float
    b=10.5
    # string
    name='dao hai long'
    # list
    vlaue_list=[6,12,20,7,4]
    # complex
    complexnumber=3+10j
    # tuple
    thistuple = ("apple", "banana", "cherry","tomato")
    # dictionary
    dicts={
        "name": "New",
        "age":22,
        "branch": "new"
    }
    # boolean 
    number=10>9    
 
    print(a ,'\n')
    print(b ,'\n')
    print(name ,'\n')
    print(vlaue_list ,'\n')
    print(complexnumber,'\n')
    print(thistuple[3],'\n')
    print(dicts,'\n')
    print(number,'\n')
    
    print('type',type(a) ,'\n')
    print('type',type(b),'\n')
    print('type',type(name) ,'\n')
    print('type',type(vlaue_list) ,'\n')
    print('type', type(complexnumber))
    print('type',type(thistuple))
    print('type',type(dicts))
    print('type',type(number))
    
def ep_kieu_du_lieu():
    value=15
    int_number= int(value)
    float_number= float(value)
    string=str(value)
    hex_data=hex(value)
    
    print(int_number,'int')
    print(float_number,'float')
    print(string,'string')
    print(hex_data,'hex','he 16')
    
if __name__ == '__main__':
    khaibao()
    ep_kieu_du_lieu()
    

