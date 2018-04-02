words = ['some', 'words', 'here', 'what', 'not']

# print(words.index('some')) =? index method. returns index

# .append method append shit like
words.append("somevalue")
words.insert(1, "insert this value at <-that index")
words.remove("not")

# remove method uses `value` to delete first occurance found
# you can use `del` keyword to delete using index
 
#  sort the list using sort()
words.sort()
# it would start sorting with what in mind/logic?
# alphabetical order from [o] index
# what if alphabet is capital A rather than a.
# capital A would come first. Z, z, A, b => A and Z come first.
# reverse_sort please?
words.sort(reverse=True)

# NOTE : can't store mixed data-type list
# Just sort normally .... ASCII-belitcal

words.sort(key=str.lower)
