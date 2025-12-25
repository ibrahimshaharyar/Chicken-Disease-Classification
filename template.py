import os
from pathlib import Path
import logging

#creating logging so we can study each step when the code executes
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "CNN_based_disease_classifier"

#list of files/folders that will be needed
list_of_files= [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    
    filepath = Path(filepath) #using Paths because it creates a file object of the strings we have given in the list
    
    filedir, filename = os.path.split(filepath) # example -> config/config.yaml is filedr=config and filename=config.yaml
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True) #making the file directory and exist_ok=True means that if it alr exists then
                                            #dont make another file dir
        logging.info(f"Creating directory -> {filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
#if the filepath does not exist or the bytes of the filepath is 0 then we create an empty file in this path    
        with open(filepath, "w") as f:  
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} already exists")
        
        

    
