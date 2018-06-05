# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 18:50:07 2018 - constantly improving ever since

@author: Manan Khaneja
"""
# Master program for data extraction without damaging file format
# takes in input the directory in which all the files have to be analysed ( eg. a directory from which neutron data is extracted)
#analyses all the files and asks for the name you want to give the txt file generated with those conditions (eg. let's name that file neutron.txt)
# asks for the path of the directory where you want to save that file (eg. I want to save my neutron.txt file in a directory named 'Particles', hence give path of 'Particles')
#'conditions' is a list containing all the strings ( eg. neutron, DET0, protonInelastic etc.) hence while entering conditions take care of the format(case sensitive)/ spelling)
def screener (conditions):
    count=0
    for file in all_files:
        f= open(user_input+"/"+file,"r+")
        k= open(complete_name, "a+")
        line=f.readline()
        while line:
            words= line.split()
            for condition in conditions:
                if condition in words:
                    k.write(line)
                    count+=1
            line= f.readline()
        f.close()
        k.close()
    return(count)

import os
user_input =input("Enter the path of your directory: \n")
assert os.path.isdir(user_input), "I did not find the directory"
print("\n")
all_files=os.listdir(user_input)
print(all_files)
flag=1
filename=input("What is the name of file you want to save the output in ?\n")
save_path=input("Enter the path of the directory where the output file has to be saved \n")
complete_name=os.path.join(save_path,filename)
while flag:
    conditions=[]
    temp=input("Enter the condition\n")
    conditions.append(temp)
    flag=int(input("Do you want to give another condition? \n0. NO \n1. YES\n"))
count= screener(conditions)
print("The number of such particles is ", count)
