# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 10:33:40 2022

@author: Liang Yu

This code is used for setting the spec_cal parameters.
by YuLiang 
yuliang@shao.ac.cn
"""

from setuptools import setup, find_packages

setup(
    name="spec-cal",
    version="0.0.3",
    description='spec_cal',
    long_description=('spec_cal.'),
    author="Yu Liang",
    author_email="yuliang@shao.ac.cn",
    url="https://github.com/git-yuliang/ifs_spec_cal/",
    license="MIT Licence",
    packages=find_packages(where="src"),
    install_requires=['pandas>=1.3.3',
                      'numpy>=1.21.6',
                      'h5py>=2.8.0',
                      'einops>=0.3.2',
                      'matplotlib>=3.2.2',
                      'astropy>=4.2.1',
                      'scipy>=1.1.0',
                      'extinction>=0.4.0'],
    #package_dir={'': 'src'},
    #include_package_data=True,
    package = {'spec_cal'},
    package_dir={'spec_cal': 'src/spec_cal'},
    package_data={'spec_cal': [ 'refdata/1d_sp/Hamuy1992/*.dat',
                                'refdata/1d_sp/oke1990/*.dat',
                                'refdata/1d_sp/Massey1998/*.dat',
                                'refdata/1d_sp/ctiocal/*.dat',
                                'refdata/1d_sp/gemini/*.dat',
                                'refdata/starlists/Hamuy1992/*.xlsx',
                                'refdata/starlists/oke1990/*.xlsx',
                                'refdata/starlists/Massey1998/*.xlsx',
                                'refdata/starlists/ctiocal/*.xlsx',
                                'refdata/starlists/gemini/*.xlsx',
                                ]},
    include_package_data=True,
    python_requires='>=3.7',
)

