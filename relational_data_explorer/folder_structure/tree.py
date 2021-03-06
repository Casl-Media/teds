
import os
import json

walk_dir = os.path.join("sample_dir")

def walk_path(path):
    head, tail = os.path.split(path)
    path_dict = {'name': tail}
    if os.path.isdir(path):
        path_dict['children'] = []
        for child_path in os.listdir(path):
            if child_path.startswith('.'):
                continue
            path_dict['children'].append(walk_path(path + '/' + child_path))
    return path_dict

with open('sample_data.js', 'w') as outfile:
    outfile.write("var sample_data = ")
    json.dump(walk_path(walk_dir), outfile, indent=4)
    
