# exercise 1
# import datetime

# current_time = datetime.datetime.now()
# new_date = current_time - datetime.timedelta(days = 5)

# print(f"сейчас : {current_time}")
# print(f"5 дней назад : {new_date}")



# exercise 2

# import datetime

# today = datetime.datetime.now()
# yesterday = today - datetime.timedelta(days=1)
# tomorrow = today + datetime.timedelta(days=1)

# print("сегодняшняя дата :",today.strftime("%Y-%m-%d"))
# print("вчерашняя дата :",yesterday.strftime("%Y-%m-%d"))
# print("завтрашняя дата :",tomorrow.strftime("%Y-%m-%d"))



# exercise 3

# import datetime

# current_time = datetime.datetime.now()

# print(current_time)
# print(current_time.replace(microsecond=0))



# # exercise 4

# from datetime import datetime
# import random
# first_date = datetime.now()
# random_hours = random.randint(0,23)
# random_minutes = random.randint(0,59)
# random_seconds = random.randint(0,59)

# second_date = datetime(2024,6,18,random_hours,random_minutes,random_seconds)

# print("первая дата:",first_date.replace(microsecond=0))
# print("вторая дата:",second_date)
# print("обычная разница:",abs(first_date - second_date))
# if abs((first_date - second_date).days) > 0:
#     print ("разница в секундах:",(first_date - second_date).seconds + abs((first_date - second_date).days) * 86400,"s")