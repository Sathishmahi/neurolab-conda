import setuptools

with open("README.md",'r',encoding="utf-8") as f:
    long_description=f.read()
__version__="0.0.0"
REPO_NAME="neurolab-conda"
AUTHOR_USER_NAME="Sathishmahi"
AUTHOR_EMAIL="sathishmahi433@gmail.com"
SOURCE_REPO=REPO_NAME
setuptools.setup(

    name=SOURCE_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    long_description=long_description,
    long_description_content=f'text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_url={
        "Bug Tracker":f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues'
    },

package_data={"","src"},
packages=setuptools.find_packages(where='src')
)
