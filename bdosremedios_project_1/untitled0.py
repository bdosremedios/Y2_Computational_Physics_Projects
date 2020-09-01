# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 17:47:42 2019

@author: dosre
"""

def print_mult_table(start,end):
    for i in range(start,end):
        print(i,"|", end="\t")
    print(" \n")

    for j in range(start,end):
        for k in range(start,end):
            print(j * k, ":", end="\t")
        print("\n")
        
def main():  
    start = int(input("Start of table "))
    end = int(input("End of table "))
    print_mult_table(start, end)
    
main()