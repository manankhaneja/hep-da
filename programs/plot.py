# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:00:33 2018

@author: Manan Khaneja
"""
print("Reference for column numbers \n")
print("column number 0 = eKin\n")
print("column number 1 = cosine(theta)\n")
print("column number 2 = Detection height\n")
print("column number 3 = interaction type\n")

import os
import matplotlib.pyplot as plt
user_input =input("Enter the path of your file: \n")
assert os.path.isfile(user_input), "I did not find the file"
print("\n")
k= open(user_input, "r+")
var_data= []
col=int(input("Which variable you want to use (enter the number): \n"))
for line in k:
        var_data.append(float(line.split(" ")[col]))
bins=int(input("how many bins? \n"))
plt.hist(var_data, bins, range= (0,100))
plt.savefig('graph.png', bbox_inches='tight')
