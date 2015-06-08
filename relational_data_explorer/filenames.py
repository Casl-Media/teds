# -*- coding: utf-8 -*-
"""
Created on Tue May 12 01:11:08 2015

@author: CLEV2
"""

from os import walk
#import re

walk_dir = "sample_dir"
max_subs = 10
i = 1
j = 1
k = 0

colnum = 0
graph_data = []
last_dir = []
#last_dir.append(walk_dir)
last_subdir = {}
last_dir_wsub = []
dir_index = []
for root, subdirs, filenames in walk(walk_dir):
    this_dir = root.rsplit('\\',1)
    
    for base, listofdirs in last_subdir.iteritems():
        if this_dir[-1] in listofdirs:
            print this_dir[-1] + " has a base index of "+ base
            #base index + 1
            
    
    """
    print root
    print subdirs
    print filenames"""
    last_dir.append(root)
    
    if subdirs:
        
        for sub in subdirs:
           dir_index.append([this_dir[-1], colnum]) 
        last_dir_wsub.append(root)
        last_subdir[this_dir[-1]] = subdirs
        colnum += 1
        
       
    
    #while len(root) > len (last_dir):
       # print "dd"
    #print colnum
    """
    if subdirs or last_dir[-1] in root:
        last_dir.append(root)
        if len(root) > len(last_dir[-1]):
            #last_dir = root
            j += 1
            print "j " + str(j) + " root: " + str(root)
            k += 1
        else:
            juke = 0
            #while len(n) < len(root):
                
                #juke += 1
            #last_dir = root
            #print "k " + str(k)
            #print "j " + str(j)
            j = j - k
            print "j " + str(j) + " root: " + str(root)
            k = -1 # fix here, 0 or -1 have diff effects
            #fix for back one, not all of k
            #--
            #---
            #----
            #---
            #---
            #--
    temp = []
    temp.append({'root': root})
    temp.append({'subdirs': subdirs})
    temp.append({'filenames': filenames})
    temp.append({'iter_number': i})
    temp.append({'column_number': j})
    graph_data.append(temp)
    i += 1
    """
    
for item in graph_data:
    print str(item[0]['root'])
    print "iter " + str(item[-2]['iter_number']) + " column number " + str(item[-1]['column_number'])