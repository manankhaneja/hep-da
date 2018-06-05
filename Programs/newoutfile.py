# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 22:07:53 2018

@author: Manan Khaneja
"""
import os
import math

def thetacalc(calcwords):       #For calculation of cosine theta i.e. the angle between position and momentum      
    numerator = calcwords[0]*calcwords[3] + calcwords[1]*calcwords[4] + calcwords[2]*calcwords[5]
    num1 = math.sqrt( calcwords[0]*calcwords[0] + calcwords[1]*calcwords[1] + calcwords[2]*calcwords[2] ) 
    num2 = math.sqrt( calcwords[3]*calcwords[3] + calcwords[4]*calcwords[4] + calcwords[5]*calcwords[5] )
    denominator = num1 * num2
    costheta = 1.0*numerator/denominator
    return (costheta)

def newoutfile():
    user_input = input('Enter the path of your file: \n')
    assert os.path.isfile(user_input)
    old = open(user_input,'r+')
    filename = input('What is the name of file you want to save the output in ?\n')
    save_path = input('Enter the path of the directory where the output file has to be saved \n')
    complete_name = os.path.join(save_path,filename)
    new = open(complete_name,'a+')
    line = old.readline()
    while line:
        words = line.split()
        calcwords=[]
        for index in range(6,12,1):         #6 to 11 are the indices in the real file that correspond to posX,Y,Z momentumX,Y,Z respectively
            calcwords.append(float(words[index]))
        costheta = thetacalc(calcwords)
        new.write(words[4] + ' ' )
        new.write(str(costheta))
        new.write(' ' + words[14])
        new.write("\n")     
        line = old.readline()
newoutfile()        