# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:01:01 2021

@author: MTAEXAM
"""

age = int(input("age:"))

if age < 6:
    print("普遍級")
elif age < 12:
    print("普遍級and保護級")
elif age < 18:
    print("限制級以外都能看")
else:
    print("都能看")    
