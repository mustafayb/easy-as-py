#!/usr/bin/python 

import os

path_components = os.getcwd()

path_components = path_components.split('/')

path_components.remove('')

print (path_components)

print (path_components)

def get_path_components():
        return os.getcwd().split('/')

print (get_path_components())
