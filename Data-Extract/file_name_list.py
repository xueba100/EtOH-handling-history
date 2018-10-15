import os
path=input('Give me a director path here.\neg.H:/DataSet/EEG/alcoholics/co2a0000364/')
list_name = []
for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if os.path.splitext(file_path)[1]=='.txt':
        list_name.append(file_path)
print('Finished. Check list_name for file names.')
