# Module được sử dụng để phân loại code thành các phần nhỏ hơn liên quan với nhau
# Trong một module, chúng ta có thể định nghĩa hàm (function), lớp (class), biến (variable).
# Package trong Python bao gồm một hoặc nhiều module. Package giống như một thư mục (directory). Một package có thể chứa các package khác.
# cac cach goi module
# 1 dung lenh import
# 2 dung lenh form import
# 3 su dung as neu moi doi ten module

# ex1 dung module math
import math
import testModule

print("so pi =",math.pi)
print("can bac hai cua 25 la:", math.sqrt(25))
print(" Sin va cos 1 goc bag:",math.sin(60),math.cos(60))
print("-**********-")
print("HHCH", testModule.HHCN())