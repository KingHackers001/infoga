#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : Infoga - Email OSINT
# @url    : http://github.com/KingHackers001
# @author : KING001

from setuptools import setup 

setup(
    name='infoga',

    version='0.1.5',
    description='Email OSINT',
    url='https://github.com/KingHackers001'
    
    author = 'KING001',
    license='GPLv3',

    install_requires = ['colorama','requests','urllib3'],
    console =['infoga.py'],
)
