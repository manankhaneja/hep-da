# -*- coding: utf-8 -*-
"""
Created on Wed May 16 18:08:30 2018

@author: Manan Khaneja
"""

import os
user_input =input("Enter the path of your file: \n")
col=int(input("1. Know all the particles \n2. Know all the interaction types\n"))
assert os.path.isfile(user_input), "I did not find the file"
print("\n")
f= open(user_input, "r+")
k=open('temp.txt','w')
var_data= []
if col==1:
    col=3
elif col==2:
    col=14
line=f.readline()
while line:
    line=f.readline()
    if '-->' in line:
        line=f.readline()
    elif '###' in line:
        pass
    else:
        var_data.append((line.split(" ")[col]))
