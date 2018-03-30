#slice can get several values from list
#slice has 2 indexes mainly
#a[start:end] # items start through end-1
#a[start:]    # items start through the rest of the array
#a[:end]      # items from the beginning through end-1
#a[:]         # a copy of the whole array

animals = ['cat', 'rat', 'bat', 'dog', 'fox']

#a[start:end:step] # start through not past end, by step
#by default step is 1
slice = animals[0:3]
print(slice)

#a[-1]    # last item in the array
#a[-2:]   # last two items in the array
#a[:-2]   # everything except the last two items
#what does 'stop' means
#stop: the ending index of the slice, it does not include the element at this index, 

#len()  will return length of list too, like string
"""
Note to self:
if you ask for a[:-2] and
a only contains one element, 
you get an empty list instead of
an error. Sometimes you would prefer 
the error, so you have to be aware that
this may happen.
"""