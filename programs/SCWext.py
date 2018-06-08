# -*- coding: utf-8 -*-
"""
Created on Wed May 16 18:08:30 2018

@author: Manan Khaneja
"""
#this program gives you the information about all the different types of particles, interaction types and detection heights present in a file
#only works for files directly generated by GEANT4 or modified only by master_new.py (i.e. files in which formatting of a line is unchanged)
def scw_ext():
    import os
    user_input =input("Enter the path of your file: \n")
    col=int(input("1. Know all the particles \n2. Know all the interaction types\n3. Know all the detection heights\n"))
    assert os.path.isfile(user_input), "I did not find the file"
    print("\n")
    f= open(user_input, "r+")
    var_data= []
    if col==1:
        col=3       #3 corresponds to the column with particle name
    elif col==2:
        col=14      #14 corresponds to interaction type
    elif col==3:
        col=12      #12 corresponds to all the detection heights
    line=f.readline()
    while line:
        line=f.readline()
        if '-->' in line:
            line=f.readline()
        elif '###' in line:
            pass
        elif line.strip():
                name= line.split(" ")[col]
                if name not in var_data:
                    var_data.append(line.split(" ")[col])
    f.close()
    print(var_data)
scw_ext()
