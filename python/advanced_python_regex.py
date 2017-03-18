import csv
import re
from collections import defaultdict

# use for debugging
# import pdb
# pdb.set_trace()

data = []

with open('faculty.csv', newline='') as csvfile:
    faculty = csv.reader(csvfile, delimiter=',')
    next(faculty) # skips the header
    for row in faculty:
        data.append({'name':    row[0],
                     'degree' : row[1],
                     'title' :  row[2],
                     'email' :  row[3]})

def cleandata():
    """
    This converts all the data containing the degrees into a single format
    """
    # degree regex
    # test: https://regex101.com/r/TbOu0J/3
    r_phd = (re.compile(r'\s*(Ph\.*D\.*)'), 'PhD')
    r_scd = (re.compile(r'\s*(Sc\.*D)\.*'), 'ScD')
    r_md = (re.compile(r'\s*(MD)'), 'MD')
    r_mph = (re.compile(r'\s*(MPH)'), 'MPH')
    r_jd = (re.compile(r'\s*(JD)'), 'JD')
    r_ma = (re.compile(r'\s*(MA)'), 'MA')
    r_ms = (re.compile(r'\s*(M\.*S\.*)'), 'MS')
    r_bsed = (re.compile(r'\s*(B\.*S\.*Ed)'), 'BSEd')
    r_degrees = [r_phd, r_scd, r_md, r_mph, r_jd, r_ma, r_ms, r_bsed]

    # title clean
    # test: https://regex101.com/r/b4x6PA/1
    r_title = (re.compile(r'\s(of|is)\sBiostatistics'), r'')

    for k in data:
        # degree clean
        deg = k['degree']
        deg_data = []

        for reg in r_degrees:
            if reg[0].search(deg):
                deg_data.append(reg[1])
        
        k['degree'] = deg_data

        # title clean
        repl = re.sub(r_title[0], r_title[1], k['title'])
        k['title'] = [repl]
        
        # email clean
        k['email'] = [k['email']]

cleandata()

# Example:
# d = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
#              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
# d = { 'lastname' : [[ellenberg1], [ellenburg2]]}
#                     [degrees, title, email], etc.
def make_dict():
    _dict = {}
    r_lastname = re.compile(r'(\w*)$')
    for v in data:
        # get last name
        lastname = r_lastname.search(v['name']).group(1)
        
        # if it's a new name, just make a new list, else, just append the new list
        if lastname not in _dict.keys():
            _dict[lastname] = [ [v['degree'], v['title'][0], v['email'][0]] ]
        else:
            _dict[lastname].append( [v['degree'], v['title'][0], v['email'][0]] )
    return _dict

def freq(_iter, field=''):
    """
    Returns the frequency of the values within an iterable of a field
    """
    freq = defaultdict(int)
    for k in _iter:
        if field:
            for v in k[field]:
                freq[v] += 1
        else:
            freq[k] += 1
    return freq

def relfreq(count):
    """
    Returns the relative frequency of a default dict
    """
    total = 0
    rel_frequencies = defaultdict(float)
    # these two passes seem inefficient and might be better as vectors
    for k, v in count.items():
        total += v
    for k, v in count.items():
        rel_frequencies[k] += v/total
    
    return rel_frequencies
        
def getlistof(field, fl=False):
    # fl = flatten list
    if fl:
        return [v[field] if field is 'degree'
                else v[field][0]
                for v in data]
    else:
        return [v[field] for v in data]

def getemaildomains():
    r_domain = re.compile(r'@(.*)')
    return [r_domain.search(v).group(1) for v in getlistof('email', fl=True)]