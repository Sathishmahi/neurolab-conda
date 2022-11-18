import os
import logging
import pathlib

logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s:%(levelname)s]:%(message)s")

while True:
    project_name=input('enter the project name ')
    if project_name!="":
        break
logging.info(f'project created {project_name}')

list_of_files=[
    ".github/.workflows/.gitkeep",
    f'src/{project_name}/__init__.py',
    f'tests/__init__.py',
    f'tests/unit/__init__.py',
    f'tests/integration/__init__.py',
    'init_setup.sh',
    'requirements.txt',
    'requirements_dev.txt',
    'setup.py',
    'setup.cfg',
    'tox.ini'

]
for file_path in list_of_files:
    file_dir,file_name=os.path.split(file_path)
    if file_dir !='':
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f'dir created {file_dir}')
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,'w') as f:
            logging.info(f'file created {file_path}')
            pass
    else:
        logging.info(f'file already created')
    
