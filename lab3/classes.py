# # exercise 1

# class Manipulator:
#     def __init__(self):
#         self.input_string = ''
#     def getString(self):
#         self.input_string = input('Введите строку:')
#     def printString(self):
#         print(self.input_string.upper())
        

# manipulator = Manipulator()
# manipulator.getString()
# manipulator.printString()

# # exercise 2

# class Shape:
#     def area(self):
#         return 0
    
# class Square(Shape):
#     def __init__(self,length):
#         self.length = length
    
#     def area(self):
#         return self.length * self.length


# shape = Shape()
# print('начальная площадь была:'+ str(shape.area()))

# square = Square(5)


# print(f"площадь квадрата:{square.area()}")



# # exercise 3

# class Shape:
#     def area(self):
#         return 0

# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.length = int(length)
#         self.width = int(width)

#     def area(self):
#         return self.length * self.width
    
# shape = Shape()

# print('начальная площадь была:'+ str(shape.area()))

# user_input_length = input("введите длину четырехугольника:")
# user_input_width = input("введите ширину четырехугольника:")

# rectangle = Rectangle(user_input_length,user_input_width)

# print(f"площадь четырехугольника:{rectangle.area()}")


# # exercise 4
# import math

# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
        
#     def show(self):
#         print(f"точка с координатами {(self.x,self.y)}")
        
#     def move(self,new_x,new_y):
#         self.new_x = new_x
#         self.new_y = new_y
#         print("координаты точки были изменены")
    
#     def dist(self,another_point):
#         distance = math.sqrt((another_point.x - self.x)**2 + (another_point.y - self.y)**2)
#         print("расстояние между точками:"+str(distance))
    

# point1 = Point(2,3)
# point2 = Point(5,7)

# point1.show()
# point2.show()

# distance = point1.dist(point2)



# # exercise 5
# class Account:
    
#     def __init__(self,owner,balance = 0):
#         self.owner = owner
#         self.balance = balance
        
#     def deposit(self,amount):
#         if amount > 0:
#             self.balance += amount
#             print("Средства успешно внесены")
#         else:
#             print("Некорректная сумма для депозита")
#     def withdraw(self,amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Средства в размере {amount} успешно сняты")
#         else:
#             print("Недостаточно средств на счету для снятия")
            
#     def display_balance(self):
#         print(f"Текущий баланс счета {self.owner}:{self.balance}")
        
# account = Account("Dautbekov Magzhan",1000)

# account.display_balance()  
# account.deposit(500)       
# account.display_balance()  
# account.withdraw(2000)    
# account.withdraw(1000)     
# account.display_balance()  



# # exercise 6

# filterlambda = lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)) and x > 1

# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# prime_numbers = list(filter(filterlambda, numbers))

# print("Простые числа в списке:", prime_numbers)