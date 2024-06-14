def trapezoid_area(a,b,h):
    area = (a + b) * h / 2
    return area


h = int(input())
b = int(input())
a = int(input())
print(trapezoid_area(a,b,h))