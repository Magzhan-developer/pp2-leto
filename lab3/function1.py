# # exercise 1 
# def to_grams(dictionary):
#   for x, y in dictionary.items():
#       print(x + ":",round(y / 28.3495231, 2),"ounces")  
    
 
 
# ingredients = {
#     "carrots":200, 
#     "onions":150,
#     "celery":120,
#     "chicken":500,
#     "salt":50,
#     "pepper":40,
#     "bay leaf":30,
#     "noodles":70,
#     "spinach":60
#  }   

# to_grams(ingredients)

# # exercise 2 

# def to_celcium(faraengheit):
#     print((5 / 9) * (faraengheit - 32))
    
# to_celcium(120)



# # # exercise 3 

# def solve(numheads, numlegs):
#     for num_rabbits in range(numheads + 1):
#         num_chickens = numheads - num_rabbits
#         total_legs = 4 * num_rabbits + 2 * num_chickens
#         if total_legs == numlegs:
#             return num_chickens, num_rabbits
#     return "No solution"
    


# print(solve(35,94))


# exercise 4

# import math

# def string_to_array(stroka):
#     massiv = stroka.split()
#     integer_massiv = [int(x) for x in massiv]
#     return integer_massiv

# def find_prime_numbers(array):
#     for x in array:
#         if x < 2:
#             continue
#         elif x == 2 or x == 3 or x == 5 or x == 7:
#            print(x)
#         else:
#             root = int(math.sqrt(x)) + 1
#             i = 2
#             while i <= root and x % i != 0:
#                 i += 1
#                 if i == root and x % i != 0:
#                     print(x)

               
# string_of_numbers = "22 3 10 171 89 19"
# find_prime_numbers(string_to_array(string_of_numbers))


# exercise 5

# def podborka(string, prefix=""):
#     if len(string) == 0:
#         print(prefix)
#     else:
#         for i in range(len(string)):
#             podborka(string[:i] + string[i+1:], prefix + string[i])


# user_input = input("Введите строку: ")
# podborka(user_input)


# exercise 6

# def to_massiv(stroka):
#     return stroka.split()

# def to_reverse_string():
#     massiv = to_massiv(user_input)
#     massiv.reverse()
#     return " ".join(massiv)

# user_input = input(str("введите свою строку:"))
# print(to_reverse_string())


# exercise 7


# def has_33(nums):
#     count = 0
#     for x in range(len(nums)):
#         if x != 0 or x != len(nums) - 1:    
#             if nums[x] == 3 and nums[x - 1] == 3 or nums[x] ==  3 and nums[ x+1 ] == 3:
#                 count += 1
#         elif x == 0 or x == len(nums) - 1:
#             if nums[x] == 3 and nums[x + 1] == 3:
#                 count += 1
#         elif x == len(nums) - 1:
#             if nums[x] == 3 and nums[x - 1] == 3:
#                 count += 1
#     if count > 0:
#         print(True)
#     else:
#         print(False)

# # has_33([1, 3, 3])
# has_33([1, 3, 1, 3])
# # has_33([3, 1, 3])


# # exercise 8
# def spy_game(nums):
#     count = 0
#     for x in range(len(nums) - 2):
#         if nums[x] == 0 and nums[x+1] == 0 and nums[x+2] == 7:
#             count += 1

#     if count > 0:
#         print(True)
#     else:print(False)
# # spy_game([1,2,4,0,0,7,5])
# # spy_game([1,0,2,4,0,5,7])
# spy_game([1,7,2,0,4,5,0])


# # exercise 9
# import math
# def volume_sphere(radius):
#     volume = (4/3) * math.pi * radius ** 3
#     print(volume)


# rad = float(input("введите радиус:"))
# volume_sphere(rad)

# # exercise 10

# def unique_elements(array):
#     massive = []
#     for x in array:
#         if x not in massive:
#             massive.append(x)
    
    
#     print(massive)   
    
# array = [12,2,33,44,12,5,23,44,33,12]
# unique_elements(array)


# # exercise 11

# def check_to_palindrome(number):
#     stringify = str(number)
#     massive_1 = []
#     massive_2 = []
#     length = len(stringify)
#     if length % 2 == 1:
#          for i in range(int(length/2)):
#              massive_1.append(stringify[i])
             
#          for j in range(int(length/2) + 1,length):
#              massive_2.append(stringify[j])
        
#     elif length % 2 == 0:
#         for i in range(int(length/2)):
#              massive_1.append(stringify[i])
#         for j in range(int(length/2),length):
#              massive_2.append(stringify[j])
        
#     massive_2.reverse()
    
#     if massive_2 == massive_1:
#         print('Это число является палиндромом')
#     else:
#         print('Ваше число не палиндром')
    

# # number_1 = 12334345
# number_2 = 1229221
# # number_3 = 1890981

# check_to_palindrome(number_2)



# # exercise 12

# def stars(number):
#     print(number * "*")

# def histogram(array):
#     for x in array:
#         stars(x)
        
# list = [4,9,7,10]
# histogram(list)

# # exercise 13
# import random

# def random_number_for_game():
#     return random.randint(1,20)

# myNumber = random_number_for_game()

# print("Hello! What is your name?")
# user_name = input()
# print("Well, KBTU, I am thinking of a number between 1 and 20.")
# print("Take a guess.")
# print(f"my number is:{myNumber}")

# score_counter = 0
# user_number = 0
# while user_number != myNumber:
#     user_number = int(input())
#     print("Your guess is too low.","\n","Take a guess.")
#     score_counter += 1

# print(f"Good job, {user_name}!" + " " + f"You guessed my number in {score_counter} guesses!")
    