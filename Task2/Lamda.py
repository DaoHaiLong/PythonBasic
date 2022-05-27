# lamda function dc goi la cac ham an danh. Ham lambda khong co kha nang tai su dung
#  cau truc ham: lamda arguments: expression
# la mot expression khong phai khoi lenh
# giup cho bieu thuc cua minh tro nen ngan gon hon (nhung bieu thu vua va nho)
#  nhuc diem: viec debug va bao tri se kho khan hon

#  ex1: 400
number= lambda x : x*20
print(number(20)) 

# ex2: lambda with list
arr=[1,2,3,4,5,6,7,8,9,10,11,20]
#  filter object tra ra danh sach voi dk la true
sort_evennumber=filter(lambda x:(x%2==0),arr)
print(list(sort_evennumber))

# ex3
def myfunc(n):
      return lambda a : a * n

# return a=3*11=33
mytripler = myfunc(3)
print(mytripler(11)) 

x ="GeeksforGeeks"
 
# lambda gets pass to print
(lambda x : print(x))(x)

lists=[lambda x:pow(x, 2),lambda x:pow(x, 3),lambda x:pow(x, 4),lambda x:pow(x, 5)]
# x=3
# print(lists[1](3))
# x=2
for pows in lists:
      print(pows(2))
key = 'Google'
print({'Google': lambda: 'Goooooooog',
'YouTube': lambda: 'Youuuuuuuuu',
 'Kteam': lambda: 'Free Education'}[key]())