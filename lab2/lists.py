
                # Create a list
# thislist = ["apple", "banana", "cherry"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# print(len(thislist)) # =>len - для определения длины


# list1 = ["abc", 34, True, 40, "male"]


# С точки зрения Python, списки определяются как объекты с типом данных 'list'


# mylist = ["apple", "banana", "cherry"]
# print(type(mylist)) # list 



# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)


# Список - это коллекция, которая упорядочена и изменяема. Допускает дублирование элементов.
# Кортеж — это упорядоченная и неизменяемая коллекция. Допускает дублирование элементов.
# Набор - это коллекция, которая не упорядочена, неизменяемый* и неиндексируемый. Отсутствие дублирующихся элементов.
# Словарь - это коллекция, которая упорядочена** и изменчивый. Отсутствие дублирующихся элементов.

# exercise 1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# exercise 2

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

# exercise 3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

# exercise 4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

# exercise 5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

# exercise 6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

# exercise 7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:6])

# exercise 8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))