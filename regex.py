import re

message = "some message having 123-555-999 nummbers. Call 111-333-111"
# regex basics till line 20
# we pass raw string to compile()
# call re.compile() function to create regex object
phoneregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
# d for digit
match_object = phoneregex.search(message)
# search()  creates a match object as the name depicts
print(match_object.group())
# group method to get matched string
# it returns the digits above which is so cool
# now this method of search() returns the first occurance, we need more.

print(phoneregex.findall('Here goes my number 555-999-111 and 999-000-777'))
# returns all the occurances found in a string in a list
