# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:57:36 2021

@author: MTAEXAM
"""

scort = []

while True:
    inscort = int(input("分數:")) 
    if inscort == " ":
        #scort.sort()
        #scort.reverse()
        #print(scort)
        exit()
    if inscort > 100 or inscort < 0:
        print(scort)
        continue
    scort.append(inscort)
    #num = sorted(scort,reverse = True)
    scort.sort()
    scort.reverse()
    print(scort)
    