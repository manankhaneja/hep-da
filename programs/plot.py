# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:00:33 2018

@author: Manan Khaneja
"""
import variables
import os
import matplotlib.pyplot as plt

def plot():
    print("Reference for column numbers in the new file \n")
    print("column number 0 = eKin\n")
    print("column number 1 = cosine(theta)\n")
    print("column number 2 = Detection height\n")
    print("column number 3 = interaction type\n")

    ax = plt.axes()
    assert os.path.isdir(variables.dir_path), "I did not find the directory"
    print("\n")
    index,flag = 1,1
    plot_name = "plot"
    var_data = [[],[],[],[],[],[],[],[],[],[]]             #can plot maximum 10 plots simultaneously
    bins = int(input("how many bins do you want to use? \n"))
    min = int(input("Enter the range integer -start value \n"))
    max = int(input("Enter the range integer -end value \n"))
    xlabel = input("What is the x label \n")
    ylabel = input("What is the y label \n")
    col = int(input("Which variable you want to use (enter the column number choice): \n"))
    while flag:
        filename = input("Enter the filename \n")
        particle = input("Enter the associated particle \n")
        file_path = os.path.join(variables.dir_path,filename)
        plot_name = plot_name + '_' + filename[3:len(filename)-4:1]
        k = open(file_path, "r+")
        var_data[index] = []
        for line in k:
                var_data[index].append(float(line.split(" ")[col]))
        (n, bins, patches) = plt.hist(var_data[index], bins, range = (min,max), histtype = 'step', alpha = 0.5, label = particle )
        plt.legend(loc = 'upper right')
        print("\n")
        for i in range(len(bins)-1):
            print("number ", n[i] , "bin ", bins[i] ,"\n")
        flag = int(input("Do you want to give another file? \n1. Yes \n0.No \n"))
        index = index + 1
    plot_name = plot_name + '_' + xlabel
    ax.xaxis.set_major_locator(plt.MultipleLocator((max-min)/10))
    ax.xaxis.set_minor_locator(plt.MultipleLocator((max-min)/100))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(plot_name)
    plt.savefig(variables.dir_path + '/' + plot_name + '.png', bbox_inches='tight', dpi = 500)
