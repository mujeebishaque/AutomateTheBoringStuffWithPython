"""
def write_to_file(text):
    try:
        file = open('random_file.txt', 'a')
        file.write(text)
    except IOError:
        print("ERROR: Can't Open File.")
    finally:
        file.close()
        print(file.closed)
write_to_file("\nLast line and that;s all.")
"""
"""
file_name = "random_file.txt"
with open(file_name, "r") as file:
    reader = file.read()
print(file.closed)
print(reader)
# """
# store = ""
file_name = "some_random_file.txt"
# for i in range(65, 90+1):
#     store += chr(i)

with open (file_name, "r") as file:
    writer = file.read()
print(writer)

# for i in range(0, 10):
#     print(i)

# for ch in range(97, 123):
#     print(chr(ch))