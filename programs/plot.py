# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:00:33 2018

@author: Manan Khaneja
"""
def plot():
    print("Reference for column numbers in the new file \n")
    print("column number 0 = eKin\n")
    print("column number 1 = cosine(theta)\n")
    print("column number 2 = Detection height\n")
    print("column number 3 = interaction type\n")

    import os
    import matplotlib.pyplot as plt
    import seaborn as sns
    ax = plt.axes()
    user_input =input("Enter the path of your directory: \n")
    assert os.path.isdir(user_input), "I did not find the directory"
    print("\n")
    filename = input("Enter the filename \n")
    file_path = os.path.join(user_input,filename)
    plot_name = filename[0:len(filename)-4:1]
    k = open(file_path, "r+")
    var_data = []
    col = int(input("Which variable you want to use (enter the column number choice): \n"))
    for line in k:
            var_data.append(float(line.split(" ")[col]))
    bins = int(input("how many bins do you want to use? \n"))
    min = int(input("Enter the range integer -start value \n"))
    max = int(input("Enter the range integer -end value \n"))
    (n, bins, patches) = plt.hist(var_data, bins, range= (min,max))
    xlabel = input("What is the x label \n")
    ylabel = input("What is the y label \n")
    ax.xaxis.set_major_locator(plt.MultipleLocator((max-min)/10))
    ax.xaxis.set_minor_locator(plt.MultipleLocator((max-min)/100))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(plot_name)
    plt.savefig(user_input + '/' + plot_name + '.png', bbox_inches='tight', dpi = 500)
    for i in range(len(bins)-1):
        print("number ", n[i] , "bin ", bins[i] ,"\n")

plot()
