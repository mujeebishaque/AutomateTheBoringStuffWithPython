"""for i in range(10):
    print(i)
    if i is 9:
        print( i + 1)

simple_list = list(range(0, 100, 1))
for i in simple_list:
    print(i)    
"""

merch = ['pens', 'playboy stuff', 'notes', 'books']
# returns items, no control cuz no index
# for index in merch:
    # print(index)


for i in range(len(merch)):
    print("Index : " + str(i) + " Item : " + merch[i])