import os
import cchardet

path = input('dir_path eg.H:/DataSet/EEG/alcoholics/co2a0000364')
pathway = path + '/'
file_name = os.listdir(path)#需要修改的文件在哪个文件夹里，绿色部分就写哪里
L = []

for temp in file_name: #对于文件夹里的文件
    L = os.path.splitext(temp) #分离扩展名：os.path.splitext(r"c:\python\hello.py") --> ("c:\\python\\hello", ".py")
    if L[-1]=='.txt':#对于txt格式的文件
            file = open(pathway + temp,'rb')
            lines = file.read()
            print (temp,'\n',cchardet.detect(lines),'\n\n')
print('Finished this dir_path.')
