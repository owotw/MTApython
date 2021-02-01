# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:35:55 2021

@author: MTAEXAM
"""

a = int(input("num:"))
ans = 1

for i in range(1,a+1):
    ans *= i
    print(ans)

ans = 1
i = 1

while(i < a+1):
    ans *= i
    i +=1
    print(ans)