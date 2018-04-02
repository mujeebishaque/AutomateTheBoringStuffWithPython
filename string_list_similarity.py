# both can do indexing
# both can use len and range funtions
# both have slicing

name = "KingZeus"

if "King" in name:
    print("Yes, it sure is")

if "x" not in name:
    print("Nope, Nope, nope... Zara larrson said Nope. xD")

#  LIST is MUTABLE DATATYPE
#  String is immutable

# List is reference type,no copy, it will change original.
# string is not
def some_function(para):
    para.append("function_called")

pass_list = [12, 34, 56, 78]
some_function(pass_list)
print(pass_list)
# print(pass_list)
# what if you want complete copy of list?
# use module and its function deepcopy.

# import copy
# new_copy_list = copy.deepcopy(pass_list)
# new_copy_list[1] = "Heyaa bre haaa bre haaa"
# print(new_copy_list)
# print(pass_list)

# line continuation, like you can't continue stuff on other line, it executes that instruction separately that's why escape 
# char and + sign to tell python to look for line continuation?
print("This is a multi-line" + \
"print statement. Whatchu gonna do about it?")