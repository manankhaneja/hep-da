import os

flag = 1
conditions=[]
while flag:
    temp=input("Enter the condition\n")
    conditions.append(temp)
    flag=int(input("Do you want to give another condition? \n0. NO \n1. YES\n"))

run = input("Which run is this? (e.g. run3) \n")
filename = ''.join(conditions) + run + '.txt'
dir_path = input("Enter the path of the directory where the output file has to be saved \n")
complete_name = os.path.join(dir_path,filename)
