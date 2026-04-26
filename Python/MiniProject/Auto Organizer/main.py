import os
import shutil

# Create Directory
# os.mkdir('Test')

files = os.listdir(path='.')

for file in files:
    file = file.split('.', 1)
    for i in file[1]:
        print(i)

# shutil.move('E:\Code\practice\Python\MiniProject\Auto Organizer\main.py', 'E:\Code\practice\Python\MiniProject\Auto Organizer\core')

