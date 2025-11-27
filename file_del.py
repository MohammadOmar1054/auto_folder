import os 

path_working = os.getcwd()
print('Path we are working on : ', path_working)

for i in range(4): 
    file_name = str(input('Enter file name : '))
    del_fle = os.system("rmdir {}".format(file_name))