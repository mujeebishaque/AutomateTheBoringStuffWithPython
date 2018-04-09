import os
total_size = 0
directory = r"D:\Family Photos\WinRar 64x\1 - Automate the Boring Stuff with Python Programming\11 Files"
for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        total_size += os.path.getsize(os.path.join(directory, filename))

print(total_size/(1024*1024), " MB")
