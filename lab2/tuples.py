# Кортежи используются для хранения нескольких элементов в одной переменной.

# Tuple — один из 4 встроенных типов данных в Python, используемых для хранения коллекций data, остальные 3 - List, Set и Dictionary, все с разными качествами и использованием.

# Кортеж — это упорядоченная и неизменяемая коллекция.

# Кортежи пишутся с круглыми скобками.



# thistuple = ("apple", "banana", "cherry")
# print(thistuple)


# Элементы кортежа упорядочены, не изменяются и допускают повторяющиеся значения.

# Элементы кортежа индексируются, первый элемент имеет индекс, второй элемент имеет индекс и т.д.[0][1]



# Кортежи допускают дублирование значений:

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)


# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))

# ===========================================

# thistuple = ("apple",) # =>надо добавить запятую в конце иначе Python не распознает это как кортеж
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))



# tuple1 = ("abc", 34, True, 40, "male")  # <class 'tuple'>


# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

        # кортеж напрямую нельзя изменить,но можно преобразовать в лист и потом изменить необходимую часть
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)


# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)


# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)


# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)


# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists


# Когда мы создаем кортеж, мы обычно присваиваем ему значения. Это называется «упаковкой» кортежа

# ==================

# Но в Python нам также разрешено извлекать значения обратно в переменные. Это называется "распаковкой":
# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# ==================


# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

# =========================

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

# =========================


# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)

# =========================

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

# =========================



# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)

# =========================


# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

# =========================

# exercise 1
fruits = ("apple", "banana", "cherry")
print(fruits[0]) 

# exercise 2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

# exercise 3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

# exercise 4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])


