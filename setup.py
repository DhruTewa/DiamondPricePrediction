# -------------- setup.py is a python script that defines the packaging of the project ---------------
# It contains the metadata of the project like name, version, author, author_email, install_requires, packages
# It is used to install the project in the system
# It is used to create a distributable package of the project
# It is used to upload the project on PyPI (Python Package Index)


from setuptools import find_packages,setup   # this is required to give the details of the packages 
from typing import List # this is required to give the type of the variable

HYPEN_E_DOT = ' -e .'

def get_requirements(file_path:str)->List[str]: # this function will take the file path as input and return the list of the packages
    requirements=[]
    with open(file_path,'r') as file_obj:
        requirements= file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements] # this will remove the \n from the list with the blank space
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)    # this will remove the -e . from the list
        return requirements
        

setup(
    name= 'DimondPricePrediction',
    version= '0.0.1',
    author= 'DhruvTewari',
    author_email= 'dhrutewa@gmail.com',
    install_requires= get_requirements('requirements.txt'), # these are the packages that are required to run this project
    packages= find_packages() # this will find all the packages in the project
)