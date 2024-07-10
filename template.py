import os
from pathlib import Path
import logging
 
#instead of printing the statements it is advisable to log the info in the terminal using the logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name='finment' 
sub_dir1='backend'
sub_dir2='frontend'
sub_dir3='model'

list_of_files=[
   #here, we can add the filename accordingly if we want to add something in the future
    ".github/workflows/.gitkeep",
    f"{project_name}",
    f"src/{project_name}/{sub_dir1}/dockerfile",
    f"src/{project_name}/{sub_dir1}/main.py",
    # f"src/{project_name}/{sub_dir1}/fasttext.bin",   
    f"src/{project_name}/{sub_dir2}/Dockerfile",
    f"src/{project_name}/{sub_dir2}/streamlit_app.py",
    f"src/{project_name}/{sub_dir3}/preprocessing.py",
    f"src/{project_name}/docker-compose.yml",
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")