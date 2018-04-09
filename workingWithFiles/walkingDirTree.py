import os

for folderName, subfolders, filenames in os.walk('E:\\'):
    print(folderName)
    print(str(subfolders))
    print(str(filenames))
    