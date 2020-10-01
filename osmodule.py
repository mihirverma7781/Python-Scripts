import os
import shutil

# # os.getcwd --> return current working directory
# print(os.getcwd())
# # os.mkdir('movies')
# if os.path.exists('movies'):
#     print('already exist')
# else:
#     os.mkdir('movies')

# open('file.txt' ,'a').close()

# os.chdir(r'E:\bollywood\m')
# print(os.listdir(r'E:\bollywood'))

# for item in os.listdir(r'E:\hollywood'):
#     print(os.path.join(r'E:\bollywood',item))

# os.walk() gives whole directory to ditectory info

fileiter = os.walk(r'E:\hollywood')
for current_path,folder,files in fileiter:
    print(f'current path --> {current_path}')
    print(f'current folder --> {folder}')
    print(f'current file --> {files}')