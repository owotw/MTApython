# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:09:48 2021

@author: MTAEXAM
"""

dict1 ={"A":"A:內向",
        "B":"B:外向",
        "O":"O:堅強",
        "AB":"AB:聰明"}
blood = input("輸入血型:")
name = dict1.get(blood)
if name == None:
    print("\033[1;31m 錯誤 \033[0m")
else:
    print(name)