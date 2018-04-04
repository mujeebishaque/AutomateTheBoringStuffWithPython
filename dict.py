# syntax
dict = {'dude':'black', 'key': 'value'}
# syntax for ints as key

another_dict = {12:'some_value', 0: 'zero', 2: 'two'}
# print(another_dict[0])
# Dicts are un-ordered means

first = {'name': 'doodoo', 'gender': 'male'}
# second = {'gender':'male', 'name':'doodoo'}
# print(first == second) => returns true
# check keys existence using in and not in
# if 'name' in first:
    # print("Yes. True")
# gets returned list of keys and values separately
store_keys = list(first.keys()) 
store_values = list(first.values())
store_items = list(first.items())
# store_items gets returned tuples.

# get() method returns default value if key doesn't exist
# setdefault() method can set a value if key doesn't exist
# prettyprint or pprint can print elegant dict values.