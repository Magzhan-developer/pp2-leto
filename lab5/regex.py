import re

# exercise 1

string_1 = 'abba is my favourite group,abreviature is anderson bowen black actors'
result = re.match(r"ab*",string_1)
print(result)


# # exercise 2


# string_1 = 'abba is my favourite group,abreviature is anderson bowen black actors'
# result = re.match(r"ab{2,3}",string_1)
# print(result)



# exercise 3


# string_2 = 'i want to be a champion,that_can_be_first'
# result = re.findall(r"[a-z]+_[a-z]+",string_2)
# print(result)

# exercise 4

# string_2 = 'My Biggest dream is to be a champion,that_can_be_first'
# result = re.findall(r"[A-Z][a-z]+",string_2)
# print(result)


# exercise 5


# string = "akakkab sdffsf__ aooob"
# result = re.match(r"^a.*b$",string)
# print(result)



# exercise 6


# def replace_6(string):
#     pattern = r'[ ,.]'
#     print(re.sub(pattern, ':', string))

# string = "i have a question,here it is:Tell me,why i should do it."
# replace_6(string)



# result = re.sub(".",":",string)

# exercise 7


# def snake_to_camel(string):
#     components = string.split('_')
#     camel_case = components[0] + ''.join(x.title() for x in components[1:])
#     print(camel_case)

# string = "my_name_is_Magzhan"
# snake_to_camel(string)


# exercise 8


# def split_at_uppercase(string):
#     print(re.findall('[A-Z][a-z]*', string))

# string = "mazda is The Best Car ever"
# split_at_uppercase(string)


# exercise 9

# def insert_space(string):
#     result = re.sub(r'(?<=[a-z])([A-Z])', r' \1', string)
#     print(result)

# string = "HelloAgainWeAreMastersOfGame"
# insert_space(string)

# exercise 10

# def camel_to_snake(string):
#     snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', string)
#     print(snake_case.lower())

# string = "myProject"
# camel_to_snake(string)