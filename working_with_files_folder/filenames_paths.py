# path = r'D:\mujeeb'
# add/nest path like
# nested_path = '\\'.join(['folder', 'folder2', 'another_folder'])

'''# cross-platform and better version
import os

path = os.path.join('root_folder', 'sub_folder', 'again_sub', 'extras')
print(path)

print(os.sep)
print(os.getcwd())
os.chdir()
os.path.abspath() -> gets abs path
os.path.isabs() ->returns True
os.path.relpath(2 paras, first path, second to check)
'''


# if you have a file_path and you
# want to get folder_path
# os.path.dirname()
import os
# os.path.basename() -> get's the last name with extension
certain_file = "c:\\programfiles\\"
if os.path.exists(certain_file):
    pass
if os.path.isfile(certain_file) or os.path.isdir(certain_file): pass

get_size = os.path.getsize(certain_file)
dir_tree = os.listdir()