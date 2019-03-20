""" 
### Reference: https://github.com/Terrabits/rohdeschwarz/blob/master/setup.py
### Reference: https://python-packaging.readthedocs.io/en/latest/minimal.html
### 
### python setup.py --help-commands
### python setup.py sdist    #Creates tar.gz| bdist for zip
### python setup.py install  #Installs package
### pip install .            #Installs package in directory
### pip install -e .         #Install editable package
###
##########################################################
### Upload to PyPi
### python setup.py register #Reserve name in pypi
### python setup.py sdist    #Creates tar.gz
### twine upload GUIBlox-2019.03.15.tar.gz 
### twine upload dist/* --repository-url=https://test.pypi.org/legacy/
"""
import os
from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(name='guiblox',
    version='2019.03.05',
    description='GUI Widgets in Frames',
    long_description=long_description,
    long_description_content_type='text/markdown', 
    classifiers=[
      'Development Status :: 3 - Alpha',      #3:Alpha 4:Beta 5:Production/Stable
      'License :: Other/Proprietary License',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3.7',
      'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)',
    ],
    keywords='Rohde Schwarz FSW SMW SCPI test equipment VSA VGA',
    url='https://github.com/mclim9/guiblox',
    author='Martin C Lim',
    author_email='martin.lim@rsa.rohde-schwarz.com',
    license='R&S Terms and Conditions for Royalty-Free Products',
    packages=find_packages(exclude=['test','proto']),
    install_requires=[      ],
    test_suite = 'test',
    include_package_data=True,
    zip_safe=False)

#if __name__ == "__main__":
#    os.system("python setup.py sdist")