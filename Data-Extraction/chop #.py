# Chenge file name by chopping '# '
import os
dirpath = input('Give me a directory path here.\neg.H:/DataSet/EEG/alcoholics/co2a0000364/')
for file in os.listdir(dirpath):
    file_path = os.path.join(dirpath, file)
    tmp = os.path.splitext(file_path)
    print(tmp)
    if tmp[1]=='.txt'or'.csv':
        if tmp[0][-20]== '#':
            print('tmp[0]:',tmp[0])
            file_new = tmp[0][-18:]+tmp[1]
            file_path_new = os.path.join(dirpath, file_new)
            os.rename(file_path, file_path_new)
