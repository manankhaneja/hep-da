# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 18:50:07 2018 - constantly improving ever since

@author: Manan Khaneja
"""
# Master program for data extraction without damaging file format
# takes in input the directory in which all the files have to be analysed ( eg. a directory from which neutron data is extracted)
#analyses all the files and names the txt file generated with those conditions.
# asks for the path of the directory where you want to save that file (eg. I want to save my neutron.txt file in a directory named 'Particles', hence give path of 'Particles')
#'variables.conditions' is accessing a list conditions in variable.py containing all the strings ( eg. neutron, DET0, protonInelastic etc.)
# hence while entering variables.conditions take care of the format(case sensitive)/ spelling)
import os
import math
import newoutfile
import plot
import variables
def isSubset(words,conditions):
    for cond_index in range(0,len(conditions),1):
        word_index = 0
        while word_index < len(words):
            if conditions[cond_index] == words[word_index]:
                break
            else:
                word_index = word_index + 1
        if word_index == len(words):
            return 0
    return 1

def dir_file_ext():
    user_input = input("Enter the path of your directory where all the files are present: \n")
    assert os.path.isdir(user_input), "I did not find the directory"
    print("\n")
    all_files = os.listdir(user_input)
    print(all_files)
    count = 0
    conditions = variables.conditions
    complete_name = variables.complete_name
    for file in all_files:
        f = open(user_input + "/" + file,"r+")
        k = open(complete_name, "a+")
        line = f.readline()
        while line:
            words = line.split()
            if isSubset(words,conditions):
                k.write(line)
                count += 1
                line = f.readline()
            else:
                line=f.readline()
        f.close()
        k.close()
    print("The number of such particles is ", count)
    flag = int(input("Do you want to create the condensed file? \n0. NO \n1. YES\n"))
    if flag:
        newoutfile.newoutfile()
        old_del = int(input("Do you want to delete the originally created file ? \n0. NO \n1. YES\n"))
        if old_del:
            os.remove(complete_name)

task = int(input("What do you want to do -\n0. Make a txt file with given conditions from a directory \n1. Call the plotting function\n"))
if task:
    plot.plot()
else:
    dir_file_ext()
