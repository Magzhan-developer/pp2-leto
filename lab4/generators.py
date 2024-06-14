# exercise 1

# def squares_up_to_n(n):
#     for i in range(1,n+1):
#         yield i * i
        
# user_input = int(input("введите число:"))

# for x in squares_up_to_n(user_input):
#     print(x)
    
    
    
# exercise 2
    
# def even_numbers_with_commas(n):
#     for i in range(n + 1):
#         if i % 2 == 0:
#             yield i
            
# user_input = int(input())

# even_numbers_str = ",".join(map(str,even_numbers_with_commas(user_input)))
# print(even_numbers_str)


# exercise 3

# def divisible_by_3_and_4(n):
#     for x in range(n):
#         if x % 12 == 0:
#             yield x 
            
# user_input = int(input("введите число:"))
# numbers_divisible_by_12 = ",".join(map(str,divisible_by_3_and_4(user_input)))
# print(numbers_divisible_by_12)


# exercise 4

# def square_generator(a,b):
#     for number in range(a, b+1):
#         yield number**2
        
# a = int(input("введите первое число:"))
# b = int(input("введите второе число:"))

# square_numbers = square_generator(a,b)

# print(', '.join(map(str,square_numbers)))


# exercise 5

def from_n_to_0(n):
    for x in range(n,-1,-1):
        yield x

user_input = int(input("введите число:"))

decreasing_numbers = ','.join(map(str,from_n_to_0(user_input)))

print(decreasing_numbers)