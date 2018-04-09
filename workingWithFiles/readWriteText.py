
directory = "c:\\files\\other_dir\\"

file = open(directory, 'r') # r, w, a => modes
file.readlines()
# file.read()reads till UOF
# file.write() should have w mode
# shelve module stores values in binary file
# shelve.open() retrieves a dictionary like shelf value


