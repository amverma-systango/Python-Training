import os


# printing current directory
print(os.getcwd())


# changing the directory 
os.chdir('../')
print(os.getcwd())


# listing all the dirs repesnt in current dir

print(os.listdir())


# making a dir
# os.mkdir('experimentalDirCreated2')
print(os.listdir())


#renaming a directory
# os.rename('experimentalDirCreated2','experimentalDirCreatedRenamed')
print(os.listdir())



# removing a directory
os.rmdir('experimentalDirCreatedRenamed')
print(os.listdir())


    