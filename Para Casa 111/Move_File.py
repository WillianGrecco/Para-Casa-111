import os
import shutil

from_dir = "C:/Users/Gamer/Downloads"
to_dir = "C:/Users/Gamer/Documents/Arquivos_Documentos"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    os.path.splitext