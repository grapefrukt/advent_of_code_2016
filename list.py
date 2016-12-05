#!/usr/bin/python
 # coding=utf8

from __future__ import print_function
import os
import sys

PATH = './'

readme = open('readme.md', 'r')
tmp = open('tmp.md', 'w')

header_found = False
for line in readme:
    if line.startswith('## Projekt ##') : header_found = True
    print(line, file=tmp, end='')
    if header_found : break

readme.close()

if not header_found : quit()

folders = os.listdir(PATH)

languages = {}

for folder in folders :
    if not os.path.isdir(folder) : continue
    if folder.startswith('.') : continue
        
    split = folder.split('-')
    
    if not len(split) is 2 : continue
    
    user = split[0]
    language = split[1].lower()
    
    if not languages.has_key(language) : 
        languages[language] = []
    
    languages[language].append((user, folder))

print('| Språk | Användare | | Språk | Användare |', file=tmp)
print('| --- | --- | --- | --- | --- |', file=tmp)

i = 0
for language in sorted(languages) :
    print('| {0} |'.format(language), file=tmp, end='')
    
    for user in sorted(languages[language]) :
        print('[{0}](https://github.com/kodsnack/advent_of_code_2016/tree/master/{1})<br>'.format(user[0], user[1]), file=tmp, end='')
    
    print (' |', file=tmp, end='')
    if i % 2 is 1 : print('', file=tmp)
    i += 1
    
tmp.close()

os.remove('readme.md')
os.rename('tmp.md', 'readme.md')