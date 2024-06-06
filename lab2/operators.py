# % => Modulus x % y
# ** => Exponentiation x ** y	
# // => Floor division x // y
# :=	print(x := 3)	x = 3
#                     print(x)


# is => Returns True if both variables are the same object	x is y	
# is not => Returns True if both variables are not the same object	x is not y


# in => Returns True if a sequence with the specified value is present in the object	x in y	
# not in => Returns True if a sequence with the specified value is not present in the object	x not in y

# exercise 1
print(10 * 5)

# exercise 2
print(10 / 2)

# exercise 3
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")
  
# exercise 4
if 5 != 10:
    print("5 and 10 is not equal")
    
# exercise 5
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")