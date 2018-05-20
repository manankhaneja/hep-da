# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 18:50:07 2018

@author: Manan Khaneja
"""
# Master program for data extraction without damaging file format
# After using this program remove the output files from the folder 
#since the program uses write and not append commands, so it will delete all the
#previous data if a file with the same name is found 
# If program is used for multiple cases one after the other, 
#the final output will be stored in the file you named. you can delete all the intermediate files 
#the variable count keeps track of the particles satisfying the conditions that are asked for by the user
global b
def screener (particle_var):
    count=0
    f= open(user_input,"r+")
    k= open(particle_var+".txt", "w")
    line=f.readline()
    while line:
        words= line.split()
        if particle_var in words or "###" in words:
            k.write(line)
            count+=1
        elif "-->" in words:
            k.write(line)
            line=f.readline()
            k.write(line)
        line= f.readline()
    global b        
    b =str(particle_var)    
    f.close()
    k.close()
    return(count-1)
def particle_case (num1):
    switcher={
        1: "neutron",
        2: "gamma",
        3: "nu_e",
        4: "anti_nu_mu",
        5: "nu_mu",
        6: "e-",
        7: "e+",
        8: "proton",
    }
    return switcher.get(num1," ")    
def height_case (num2):
    switcher={
        1: "DET0",
        2: "DET10km",
        3: "DET20km",
        4: "DET50km",
        5: "DET100km",
    }
    return switcher.get(num2," ")
    
def interaction_case (num3):
    switcher={
        1: "neutronInelastic",
        2: "protonInelastic",
        3: "conv",
        4: "Decay",
        5: "eBrem",
        6: "pi-Inelastic",
        7: "kaon+Inelastic",
        8: "annihil",
        9: "pi+Inelastic",
        10: "kaon0LInelastic",
        11: "nCapture",
        12: "primary",
        13: "compt",
        14: "hBertiniCaptureAtRest",
        15: "alphaInelastic",
    }
    return switcher.get(num3," ")
import sys
import os
user_input =input("Enter the path of your file: ")
assert os.path.isfile(user_input), "I did not find the file"
print("\n")
flag=1
while flag:
    print("How do you want to extract specific data- (enter the option number) \n")
    print("1. On the basis of particle of interaction \n2. On the basis of detection height \n3. On the basis of type of interaction")
    num=int(input())
    if num==1:
        print("Which particle data you want to get- (enter only the option number)")
        print("1. neutron \n2. gamma \n3. nu_e \n4. anti_nu_mu \n5. nu_mu \n6. e- \n7. e+ \n8. proton")
        num1=int(input())
        count=screener(particle_case(num1))
        user_input=particle_case(num1)+".txt"
    elif num==2:
        print("What detection height do you want to classify with")
        print("1. 0 km \n2. 10km \n3. 20km \n4. 50km \n5. 100km" )
        num2=int(input())
        count=screener(height_case(num2))
        user_input=height_case(num2)+".txt"
    elif num==3:
        print("what type of interaction you want to classify with")
        print("1. neutronInelastic \n2. protonInelastic \n3. conv \n4. Decay \n5. eBrem \n6. pi-Inelastic \n7. kaon+Inelastic")
        print("8. annihil \n9. pi+Inelastic \n10. kaon0LInelastic \n11. nCapture \n12. primary \n13. compt \n14. hBertiniCaptureAtRest")
        print("15. alphaInelastic")
        num3=int(input())
        count=screener(interaction_case(num3))
        user_input=interaction_case(num3)+".txt"
    flag=int(input("Do you want to continue? \n0. NO \n1. YES\n"))
print("The number of such particles is ", count)  
name= input("What do you want to name your file (with txt)")
os.rename(b+".txt", name)
      
        
    

     
        
