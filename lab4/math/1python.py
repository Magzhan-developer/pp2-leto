import math
def v_radiany(n):
    radian_znachenie = n / 180 * math.pi
    return radian_znachenie
    
n = int(input())
print(v_radiany(n))