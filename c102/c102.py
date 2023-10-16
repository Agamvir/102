import os
import shutil
#print(dir(os))
path = os.getcwd()
print('The path of the file is', path)
#os.mkdir('Directory')
download = os.listdir('/Users/agam/Downloads')
#print(download)
exist = os.path.exists('/Users/agam/Downloads/abc')
print(exist)
name, ext = os.path.splitext('/Users/agam/Downloads/get-pip.py')
print('The name of the file is', name)
print('The extension of the file is', ext)

source='/Users/agam/Downloads'
destination='/Users/agam/Desktop'
files= os.listdir(source)
for i in files:
    name, ext = os.path.splitext(i)
    if ext == '':
        continue
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1= source + '/' + i
        path2= destination + '/' + 'image_files'
        path3= destination + '/' + 'image_files' + '/' + i
        if os.path.exists(path2):
            print('moving')
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print('moving')
            shutil.move(path1, path3)