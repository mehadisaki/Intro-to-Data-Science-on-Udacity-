# -*- coding: utf-8 -*-
"""
Created on Wed May 20 01:48:20 2020

@author: Mehadi
"""

##5 - Fixing Turnstile Data
name  = 'turnstile-110528.txt'
old = open(name, 'r') 
new = open('updated_'+name, 'w')
read = csv.reader(old,delimiter=',')
writer = csv.writer(new,delimiter=',')

for row in read :
    i=3

    while i<len(row):
        ru = [row[0],row[1],row[2]]
        for k in range(0,5):
            ru.append(row[i+k])
        writer.writerow(ru)
        i = i+5