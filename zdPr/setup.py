from setuptools import setup,find_packages
import os

data_dir=(r'zdpr\data\external')
data_files=[(d,[os.path.join(d,f) for f in files])
    for d,folders,files in os.walk(data_dir)]

setup(
    name='zdpr',
    version='0.1.0',
    description='Detection of voltage pulses presented as a csv file.\
	    Issuing a file with pulse position marks',
    author='Vadim Stetsenko',
    license='MIT',
    include_package_data=True,
    packages=find_packages(),
    install_requires=['Click',],  
    entry_points={
       'console_scripts':['com_file=zdpr.com_line:file',
                          'com_view=zdpr.com_line:view',
                          'com_test=zdpr.com_line:test',]},
    data_files = data_files
)
