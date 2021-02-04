# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:22:18 2021

@author: MTAEXAM
"""
f = open("測試.txt","r")
for line in f:
    print(line)
f.close()

with open("測試.txt","r") as f:
    for line in f:
        print(line)
