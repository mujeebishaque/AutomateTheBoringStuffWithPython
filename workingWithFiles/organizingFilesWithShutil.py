# shell utils module

import shutil

shutil.copy('source', 'destination')

# copy entire directory with all its files and folders
shutil.copytree('source', 'destination')

# move to different folder
shutil.move('source', 'destination')
# by move, it moves not copies. 

# you can rename a file by moving it to same dir by different name
# hence, it will get 'different' name