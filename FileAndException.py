import os

file_name = 'text.txt'

print(os.getcwd())
print(os.path.exists('C:\\Users\\Eric PC'))
print(os.path.exists('C:/Users/Eric PC'))
#os.mkdir('resource') 建立檔案
#os.chdir('resource') 切換檔案路徑

workspace_path = 'C:/Users/Eric PC/PythonProjects'
if os.path.isdir(workspace_path):
    print(os.listdir())

#file_mode = 'w'
#寫入
file_write = open(file_name,'w')
file_write.write('Hello!! My name is Eric.')
file_write.close()
#讀取
file_read = open(file_name,'r')
print(file_read.read())
file_read.close() 

with open(file_name,'w') as file:
    file.write('I am a engineer in ')

with open(file_name,'a') as file:
    file.write('Quality Assurance team.\n')
    file.writelines(["GG\n","EE\n"])
    file.writelines(os.listdir())

with open(file_name,'r',encoding='utf-8') as file:
    print(file.read())
    print(file.readline())
    print(file.readlines())     #檔案指標被移到最尾處，因此讀不到任何資料
    file.seek(0)        #將指標移至最前端
    print(file.readlines())
