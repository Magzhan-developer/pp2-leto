import math 
def area_right_triangle(n,a):
    
    area = (pow(a,2) * n) / (4 * math.tan(math.pi / n))
    return area
    
    
n = int(input())
a = int(input())

print(area_right_triangle(n,a))