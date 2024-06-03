# b = "Hello, World!"
# print(b[:5]) #с начала до пятой позиции

# b = "Hello, World!"
# print(b[2:]) # со второго до конца

# b = "Hello, World!"
# print(b[-5:-2]) #=> orl

# a = "Hello, World!"
# print(a.upper())

# a = "Hello, World!"
# print(a.lower())

# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"

# a = "Hello, World!"
# print(a.replace("H", "J"))


# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']

# age = 36
# txt = f"My name is John, I am {age}"
# print(txt) #=>f-строка 

# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt) #=>Отобразите цену с 2 знаками после запятой

# txt = f"The price is {20 * 59} dollars"
# print(txt) #=>Заполнитель может содержать код Python, например, математические операции


# txt = "We are the so-called \"Vikings\" from the north." 


# exercise 1
x = "Hello World"
print(len(x))


# exercise 2
txt = "Hello World"
print(txt[0])


# exercise 3
txt = "Hello World"
txt = txt[2:5]


# exercise 4
txt = " Hello World "
txt = txt.strip()


# exercise 5
txt = "Hello World"
txt = txt.upper()


# exercise 6
txt = "Hello World"
txt = txt.lower()


# exercise 7
txt = "Hello World"
txt = txt.replace("H","J")

# exercise 8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
