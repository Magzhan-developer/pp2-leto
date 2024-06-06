# Словари используются для хранения значений данных в парах ключ:значение.

# Словарь - это коллекция, которая упорядочена*, изменяема и не Разрешить дубликаты.



# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,   #Повторяющиеся значения будут перезаписывать существующие:
#   "year": 2020
# }
# print(thisdict)


# thisdict = {  #<class 'dict'>
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

# x = thisdict.get("model") # --- thisdict["model"]


# x = thisdict.keys() # -- список ключей 





# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change -- dict_keys(['brand', 'model', 'year'])

# car["color"] = "white"

# print(x) #after the change -- dict_keys(['brand', 'model', 'year', 'color'])






# x = thisdict.values() # вернет значения




# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change




# x = thisdict.items()  # Метод вернет каждый элемент в словаре в виде кортежей в списке #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])




# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018




# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")  #Метод удаляет элемент с указанным именем ключа
# print(thisdict)




# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()  #Метод удаляет последний Вставленный элемент
# print(thisdict)




# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]  #Ключевое слово удаляет элемент с указанным значением Имя ключа
# print(thisdict)




# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# } 
# del thisdict  #удаляет полностью
# print(thisdict) #this will cause an error because "thisdict" no longer exists.



# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()  #метод очищает словарь полностью
# print(thisdict)




# for x in thisdict.values():  #Вы также можете использовать метод для Возвращаемые значения словаря
#   print(x)



# for x, y in thisdict.items():
#   print(x, y)  
                        # brand Ford
                        # model Mustang
                        # year 1964
                        
                        

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()  #копирует словарь  #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# print(mydict)





# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)  # тоже копирует   #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# print(mydict)




# myfamily = {                    # словарь внутри словаря = вложенный словарь 
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }



# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# for x, obj in myfamily.items():
#     print(x)
    
#     for y in obj:
#         print(y + ':', obj[y])



# print =>  
                                    # child1
                                    # name: Emil
                                    # year: 2004
                                    # child2
                                    # name: Tobias
                                    # year: 2007
                                    # child3
                                    # name: Linus
                                    # year: 2011
                                    
                                    
# exercise 1 

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

# exercise 2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

# exercise 3
 
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

 
# exercise 4

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model") 
 
# exercise 5 

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

