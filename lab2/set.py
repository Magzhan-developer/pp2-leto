# Набор — это коллекция, которая не упорядочена, не изменяется* и не индексируется.

# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# Заметка: Наборы не упорядочены, поэтому вы не можете быть уверены в том, в каких Порядок появления элементов.

# thisset = {"apple", "banana", "cherry", "apple"}

# print(thisset) # =>наборы не могут содержать одинаоквые элементы,в этом случае терминал выдаст набор в которым только одно яблоко


# thisset = {"apple", "banana", "cherry"}

# print(len(thisset))


# set1 = {"abc", 34, True, 40, "male"}  # => <class 'set'>


# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

# =======================================

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)

# =======================================

# thisset = {"apple", "banana", "cherry"}

# print("banana" in thisset)

# =======================================

# thisset = {"apple", "banana", "cherry"}

# print("banana" not in thisset)

# =======================================


# thisset = {"apple", "banana", "cherry"}

# thisset.add("orange")

# print(thisset)

# =======================================

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)

# =======================================

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]

# thisset.update(mylist)

# print(thisset)

# =======================================

# thisset = {"apple", "banana", "cherry"}

# thisset.remove("banana") # Заметка: Если удаляемый элемент не существует, возникнет ошибка.remove()

# print(thisset)

# =======================================

# thisset = {"apple", "banana", "cherry"}

# thisset.discard("banana") # Заметка: Если удаляемый элемент не существует, ошибка НЕ возникнет.discard()

# print(thisset)

# =======================================

# thisset = {"apple", "banana", "cherry"}

# x = thisset.pop() # метод pop() удаляет случайный элемент

# print(x)

# print(thisset)

# =======================================

# thisset = {"apple", "banana", "cherry"}

# thisset.clear() # .clear() - очищает подмножество 

# print(thisset)

# =======================================

# thisset = {"apple", "banana", "cherry"}

# del thisset # удаляет набор полностью

# print(thisset)

# =======================================

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)

# =======================================

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2) #обьединяет сеты
# print(set3)
# =======================================

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1 | set2 # этот оператор обьединяет сеты
# print(set3)


# =======================================

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# myset = set1.union(set2, set3, set4)
# print(myset)

# =======================================


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# myset = set1 | set2 | set3 |set4
# print(myset)

# =======================================

# x = {"a", "b", "c"}
# y = (1, 2, 3)

# z = x.union(y) #  Оператор позволяет соединять наборы только с множествами, но не с другими типами данных
# print(z)

# =======================================

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.intersection(set2) #Метод вернет новый набор, содержащий только те элементы, которые присутствуют в обоих наборах
# print(set3)

# =======================================


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 & set2  # можно использовать оператор аналог intersection() [Оператор позволяет соединять наборы только с множествами, но не с другими типами данных, такими как вы может с помощью метода.&intersection()]
# print(set3)

# =======================================

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.intersection_update(set2) # Сохраните элементы, которые существуют как в , так и в :set1set2

# print(set1) # =>{'apple'}

# =======================================


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.difference(set2) #Метод будет Возвращает новый набор, который будет содержать только элементы из первого набора, отсутствующие в другом наборе.

# print(set3)

# =======================================

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 - set2  # аналог difference()
# print(set3)

# =======================================


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.difference_update(set2)  # Используйте этот метод, чтобы сохранить элементы, отсутствующие в обоих наборах: 

# print(set1)
# =======================================


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.symmetric_difference(set2) #Метод сохранит только те элементы, которые НЕ присутствуют в обоих наборах

# print(set3)
# =======================================

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 ^ set2
# print(set3)

# =======================================

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.symmetric_difference_update(set2) #Используйте этот метод, чтобы сохранить элементы, отсутствующие в обоих наборах

# print(set1)


# exercise 1

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

# exercise 2

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

# exercise 3

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)


# exercise 4

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

# exercise 5

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

