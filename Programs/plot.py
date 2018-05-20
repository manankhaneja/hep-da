# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:00:33 2018

@author: Manan Khaneja
"""
print("Reference for column numbers \n")
print("column number 0 = event number\n")
print("column number 1 = parent ID\n")
print("column number 2 = track ID\n")
print("column number 3 = particle name\n")
print("column number 4 = eKin (Mev) \n")
print("column number 5 = time (ns)\n")
print("column number 6 = posX (m)\n")
print("column number 7 = posY (m)\n")
print("column number 8 = posZ (m)\n")
print("column number 9 = monX\n")
print("column number 10 = monY\n")
print("column number 11 = monZ\n")
print("column number 12 = Vname\n")
print("column number 13 = code\n")
print("column number 14 = interaction type\n")
import os
import matplotlib.pyplot as plt
user_input =input("Enter the path of your file: \n")
particle=input("Which particle is the file associated to?\n")
assert os.path.isfile(user_input), "I did not find the file"
print("\n")
k= open(user_input, "r+")
var_data= []
col=int(input("Which variable you want to use (enter the number): \n"))
for line in k:
    if particle in line:
        var_data.append(float(line.split(" ")[col]))
bins=int(input("how many bins? \n"))
plt.hist(var_data, bins, range= (0,100))
plt.savefig('graph.png', bbox_inches='tight')

        
