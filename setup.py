import setuptools


with open('README.md','r') as file:
    long_description = file.read()


setuptools.setup(name='text_preprocess_package', #This should be unique
version = '0.0.1',
author = 'Pravin Borate',
author_email = '1pravin.borate@gmail.com',
description = 'This is text Preprocessing package',
Long_description = long_description,
long_description_content_type = 'text/markdown',
packages = setuptools.find_packages(),
classifiers = [
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires = '>=3.5'
)
