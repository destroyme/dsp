import advanced_python_regex as faculty
import csv
import re

def make_q6_dict():
    _dict = {}
    r_lastname = re.compile(r'(\w*)$')
    for v in faculty.data:
        # get last name
        lastname = r_lastname.search(v['name']).group(1)
        
        # if it's a new name, just make a new list, else, just append the new list
        if lastname not in _dict.keys():
            _dict[lastname] = [ [' '.join(v['degree']), v['title'][0], v['email'][0]] ]
        else:
            _dict[lastname].append( [' '.join(v['degree']), v['title'][0], v['email'][0]] )
    return _dict

def make_q7_dict():
    _dict = {}
    r_name = re.compile(r'\b(\w+)+')
    for v in faculty.data:
        # get name
        name = r_name.findall(v['name'])
        firstname = name[0]
        lastname = name[-1]

        # if it's a new name, just make a new list, else, just append the new list
        if (firstname, lastname) not in _dict.keys():
            _dict[(firstname, lastname)] = [ [' '.join(v['degree']), v['title'][0], v['email'][0]] ]
        else:
            _dict[(firstname, lastname)].append( [' '.join(v['degree']), v['title'][0], v['email'][0]] )
    return _dict

def make_q8_dict():
    _dict = {}
    r_name = re.compile(r'\b(\w+)+')
    for v in faculty.data:
        # get name
        name = r_name.findall(v['name'])
        firstname = name[0]
        lastname = name[-1]

        # if it's a new name, just make a new list, else, just append the new list
        if (lastname, firstname) not in _dict.keys():
            _dict[(lastname, firstname)] = [ [' '.join(v['degree']), v['title'][0], v['email'][0]] ]
        else:
            _dict[(lastname, firstname)].append( [' '.join(v['degree']), v['title'][0], v['email'][0]] )
    return _dict


# Scarlett L. Bellamy
# Warren B. Bilker
# Matthew W Bryan
# Jinbo Chen
# Susan S Ellenberg
# Jonas H. Ellenberg
# Rui Feng
# Benjamin C. French
# Phyllis A. Gimotty
# Wensheng Guo
# Yenchih Hsu
# Rebecca A Hubbard
# Wei-Ting Hwang
# Marshall M. Joffe
# J. Richard Landis
# Yimei Li
# Mingyao Li
# Hongzhe Li
# A. Russell Localio
# Nandita Mitra
# Knashawn H. Morales
# Kathleen Joy Propert
# Mary E. Putt
# Sarah Jane Ratcliffe
# Michelle Elana Ross
# Jason A. Roy
# Mary D. Sammel
# Pamela Ann Shaw
# Russell Takeshi Shinohara
# Haochang Shou
# Justine Shults
# Alisa Jane Stephens
# Andrea Beth Troxel
# Rui Xiao
# Sharon Xiangwen Xie
# Dawei Xie
# Wei (Peter) Yang