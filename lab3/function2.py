movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# # exercise 1

# def film_imdb_true(movies,movie_name):
#     for x in movies:
#         if x["name"] == f"{movie_name}" and x["imdb"] > 5.5:
#             print(True)
#         else:
#             print(False)
#             break
        

# user_film_name = input("введите ваш фильм:")

# film_imdb_true(movies,user_film_name)

# # exercise 2

# def imdb_rating(dict):
#     list_of_rated_films = []
#     for x in dict:
#         if x["imdb"] > 5.5:
#             list_of_rated_films.append(x["name"])
            
#     print(list_of_rated_films)
    
# imdb_rating(movies)


# # exercise 3

# def films_by_category(dictionaire,category_name):
#     massive = []
#     for x in dictionaire:
#         if x["category"] == category_name:
#             massive.append(x["name"])
    
#     print(massive)

# category = input("выберите категорию:")
# films_by_category(movies,category)


# # exercise 4

# def average_imdb(dictionaire,list_of_films):
#     count = 0
#     movies = list_of_films.split(",")
#     for x in movies:
#         for y in dictionaire:
#             if y["name"] == x:
#                 count += y["imdb"]
                
#     print(f"The average imdb:{round(count/len(movies),2)}")
    
    

# user_input = input("введите список фильмов:")
# average_imdb(movies,user_input)


# # exercise 5

# def average_imdb_by_category(dictionaire,category_name):
#     count = 0
#     total_sum = 0
#     for x in dictionaire:
#         if x["category"] == category_name:
#             total_sum += x["imdb"]
#             count += 1
    
#     print(f"The average imdb by this category:{total_sum/count}")
    
    
    
    
# category_name = input("Введите категорию фильма:")
# average_imdb_by_category(movies,category_name)