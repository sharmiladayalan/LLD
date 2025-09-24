from abc import ABC ,abstractmethod
import typing


#Component

class FileSystem(ABC):
    @abstractmethod
    def display(self,indent=0):
        pass
    @abstractmethod
    def delete(self):
        pass
    @abstractmethod
    def rename(self,new_name):
        pass
   
#Leaf

class File(FileSystem):
    def __init__(self,name):
        self.name=name
    def display(self, indent=0):
        print(' ' * indent + f'File:  {self.name}')
    def delete(self):
        print(f'Deleting File: {self.name}')
    def rename(self,new_name):
        print(f'Renaming File: {self.name} -> {new_name}')
        self.name=new_name
   
        
        
#Composite

class Folder(FileSystem):
    def __init__(self,name):
        self.name=name
        self.children: typing.List[FileSystem]=[]
        
    def add(self,item: FileSystem):
        self.children.append(item)
        
    def display(self,indent=0):
        print(' ' * indent+f'Folder: {self.name}')
        for child in self.children:
            child.display(indent+2)
        
    def delete(self):
        print(f'Deleting Folder: {self.name}')
        for child in self.children:
            child.delete()
        self.children.clear()   #clearing array
        
    def rename(self,new_name):
        print(f'Renaming Folder: {self.name} -> {new_name}')
        self.name=new_name
        
      
            
root=Folder('root')
file_1=File('File1.txt')
file_2=File('File2.txt')
file_3=File('File3.txt')
sub_folder=Folder('sub_folder')

sub_folder.add(file_3)

root.add(file_1)
root.add(file_2)
root.add(sub_folder)

root.display()
file_1.display()
file_2.display()

sub_folder.display()

# root.delete()
# print('----------')
# root.delete()

root.rename('root_updated')
file_1.rename('File1_updated')
sub_folder.rename('sub_folder_updated')

root.display()
file_1.display()
file_2.display()

sub_folder.display()





