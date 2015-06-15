# -*- coding: utf-8 -*-
"""
Created on Mon Jun 08 21:20:55 2015

@author: CLEV2
"""
import os

def walk_path(path):
    path_dict = {'name': path}
    if os.path.isdir(path):
        path_dict['children'] = []
        for child_path in os.listdir(path):
            path_dict['children'].append(walk_path(child_path))
    return path_dict

structure = walk_path('sample_dir')

