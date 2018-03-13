print("How many cats do you have?")

cats_count = input()

try:
    if int(numberOfCats) >= 4:
        print("thats rather a lot" + "\n")
    else:
        print("Not enough")
except ValueError:
    print("Please Enter Number/Integers")
