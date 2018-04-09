import os
# permanent deletion of SINGLE file only
os.unlink('directory_path') 

# remove dir by os.rmdir()
# deletes only empty folders

import shutil

shutil.rmtree('pass_path')

# import send2trash -> for soft deletion
