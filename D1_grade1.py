# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:43:43 2021

@author: MTAEXAM
"""

score = int(input("分數:"))

if score > 100 or score < 0:
    print("錯誤")
else:
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("Not Good")
