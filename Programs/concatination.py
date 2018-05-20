# -*- coding: utf-8 -*-
"""
Created on Sun May 13 17:00:54 2018

@author: Manan Khaneja
"""
flag=1
filenames=[]
while flag:
    user_input=input("Enter the name of your file: \n")
    filenames.append(user_input)
    flag=int(input("Do you want to continue? \n0. NO \n1. YES\n"))
import os
import fileinput
with open('outfile.txt', 'w') as fout , fileinput.input(filenames) as fin:
    for line in fin:
        fout.write(line)
name= input("What do you want to name your file (with txt)")
os.rename('outfile.txt', name)        