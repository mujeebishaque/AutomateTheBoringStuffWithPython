class User:
    name, age = 'Zeus', 12
x = y = z = 0
if x <= y and y<=z:
    pass
#Good Code. Chained comparison operator
if x <= y <= z:
    pass
# Ternary operator replacement
a = True
value = 1 if a else 0
# use the in keyword
city = 'Nairobi'
found = city in {'Nairobi', 'Kampala', 'Lagos'}
cities = ['Nairobi', 'Kampala', 'Lagos']
for city in cities:
  print(city)
# Multiple Assignments
x = y = z = 'some string'
# Formatting strings
def user_info(user):
    return 'Name : {user.name}, Age : {user.age}' . format(user=user)
user = User()
print(user_info(user))
# enumerate list
ls = list(range(10))
for index, value in enumerate(ls):
  print(index, value)