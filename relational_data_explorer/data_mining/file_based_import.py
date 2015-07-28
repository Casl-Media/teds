# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 07:01:56 2015

@author: jeclevenger
"""

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return True

def number_type(n):
    if "." in n:
        return float(n)
    else:
        return int(n)

#todo
#add dtype to create structured ndarrays http://wiki.scipy.org/Cookbook/Recarray
#should be able to use type() and some type of column name, could pass headers
#possibly a seperate function to convert to structured
#first try [(header,type(n)) for header,n in zip(headers,data[0])] is getting the shape wrong i believe
def data_from_file(filename, numpyarray=True, transpose=True):
    import numpy as np
    with open(filename) as f:
        data = []
        for line in f:
            c = 0
            if ".csv" in filename: # add else if for other special cases
                split_line = line.strip().split(",")
                if split_line[-1] == '':
                    del split_line[-1]
                elif split_line[0] == '':
                    del split_line[0]
            else:
                split_line = line.split()
            for s in split_line:
                c += 1
                if is_number(s):
                    if c == len(split_line):
                        data.append([number_type(p) for p in split_line])
                    continue
                else:
                    break        
    if numpyarray and transpose:
        return np.transpose(np.array(data))
    elif numpyarray:
        return np.array(data)
    elif transpose:
        return map(list, zip(*data))
        #python3.x list(map(list, zip(*data)))
    else:
        return data

""" 2nd try, not sure i like the workflow
def to_structured(numpyarray, headers, types):
    import numpy as np
    return np.core.records.fromarrays(numpyarray,names=headers,formats=types)
"""
