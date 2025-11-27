import os 
import time

class folder_create:
    print("File we are working on : ", os.getcwd())
    def __init__(self, folder_name): 
        self.folder_name = folder_name
        
    def fldr_create(self): 
        no_ti = int(input("Enter the times you want to create folder : "))
        for i in range(no_ti): 
            if os.path.exists(self.folder_name):
                print(f"Folder '{self.folder_name}' already exists!")
                
            else :
                try:
                    os.mkdir(self.folder_name)
                    print('creating file.......')
                    print(f"Folder '{self.folder_name}' created successfully.")
                except:
                    print(f"An unexpected error occurred while creating {self.folder_name}:")

            ask_more = str(input('Do you wish to create more (y/n) : ')) 
            if ask_more=="y":
                self.foler_name = str(input('Enter the new folder name : '))
                
            else: 
                break 
class file_create: 
    def __init__(self , file_name: str, which_folder: str):
        self.file_name = file_name
        self.which_folder = which_folder
    def folder_nav(self ):
        folder_create()
        
        # os.getcwd()
    def fl_create(file_name):
        os.system(f"type nul > {file_name}")
         
        
if __name__ ==  "__main__":          
    nm_fl= str(input("Enter the name of the folder: "))
    folder = folder_create(nm_fl)
    folder.fldr_create()
    
    fl_nm = str(input('Enter the name of the file : '))
    mem_all = str(input('Where do you want to create this file (folder) : '))
    no = os.getcwd()
    print(no)
    file = file_create(fl_nm, mem_all)
    file.fl_create()
    
    