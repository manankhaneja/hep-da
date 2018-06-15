# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 22:07:53 2018

@author: Manan Khaneja
"""

# take a file in a directory, reduces it by removing the unnecessary columns and calculates cosine theta
# and then saving it as NEWoriginal_name.txt in the same directory
import variables
import math
import os
def thetacalc(calcwords):       #For calculation of cosine theta i.e. the angle between position and momentum
    numerator = calcwords[0]*calcwords[3] + calcwords[1]*calcwords[4] + calcwords[2]*calcwords[5]
    num1 = math.sqrt( calcwords[0]*calcwords[0] + calcwords[1]*calcwords[1] + calcwords[2]*calcwords[2] )
    num2 = math.sqrt( calcwords[3]*calcwords[3] + calcwords[4]*calcwords[4] + calcwords[5]*calcwords[5] )
    denominator = num1 * num2
    costheta = 1.0*numerator/denominator
    return (costheta)

def newoutfile():
    old = open(variables.complete_name,'r+')
    new_name = 'NEW' + variables.filename
    save_path = os.path.join(variables.dir_path,new_name)
    new = open(save_path,'a+')
    line = old.readline()
    while line:
        words = line.split()
        calcwords = []
        for index in range(6,12,1):         #6 to 11 are the indices in the real file that correspond to posX,Y,Z momentumX,Y,Z respectively
            calcwords.append(float(words[index]))
        costheta = thetacalc(calcwords)
        new.write(words[4] + ' ' )
        new.write(str(costheta))
        new.write(' ' + words[12])
        new.write(' ' + words[14])
        new.write("\n")
        line = old.readline()
