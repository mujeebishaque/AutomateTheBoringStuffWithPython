# Note-to-self
# you can use pyperclip to copy and paste text to clipboard

value = "string"

value_upper = value.upper()
value_lower = value.lower()

isupper = isupper(value)
islower = islower(value)

# isalpha, isalnum, isdecimal, isspace, istitle



answer = value.startswith("s")
answer2 = value.endswih("g")

join_string = ','.join(['cats', 'cats', 'cancer', 'camel'])
join_str_mod = ' '.join(['cats', 'cats'])

# split method does opposite to join

string = "Hey, whats up, my name is Abraham"
split_list = string.split()

another_str = "Greg, how are you?"
add_leftpad = another_str.ljust(20)
add_rightpad = another_str.rjust(30)

# text would be in center
center_string = another_str.center(20)
# for headings
title = another_str.center(20, '=')
# strip space and ljust, rjust etc
# to remove whitespace from left side = lstrip()
# to remove whitespace from right side = rstrip()

let = "let this be a string, from which we want to remove some chars"
#  i would want to remove certain chars from it.
new_let = let.strip('tSwR')

# replace certain char with char or string.

ex = "Jello and Hello"
ex.replace('J', 'H')

ex.replace('l', 'LL')
# p_result: JeLLLLo and heLLLLo



