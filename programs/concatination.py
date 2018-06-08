# -*- coding: utf-8 -*-
""" first test now second
Created on Sun May 13 17:00:54 2018

@author: Manan Khaneja
"""
#selectively append files in a particular directory
def concatination():
    import os
    import fileinput
    flag = 1
    filenames = []
    dir_path = input("Enter the path of the directory: \n")
    assert os.path.isdir(dir_path), "I did not find the directory"
    print("\n")
    while flag:
        user_input=input("Enter the name of your file: \n")
        filenames.append(user_input)
        flag=int(input("Do you want to give another file? \n0. NO \n1. YES\n"))
    complete_names=[]
    for index in range(0,len(filenames),1):
        complete_names.append(os.path.join(dir_path,filenames[index]))
        filenames[index] = filenames[index][0:len(filenames[index])-4:1]
    outfile = '_'.join(filenames) + '.txt'
    outfile_path = os.path.join(dir_path,outfile)
    with open(outfile_path, 'w') as fout , fileinput.input(complete_names) as fin:
        for line in fin:
            fout.write(line)

concatination()
