# -*- coding: utf-8 -*-
"""
Created on Thu May 21 22:36:43 2020

@author: Mehadi
"""
import datetime

'''
    The dates in our subway data are formatted in the format month-day-year.
    The dates in our weather underground data are formatted year-month-day.
    
    In order to join these two data sets together, we'll want the dates formatted
    the same way.  Write a function that takes as its input a date in the MTA Subway
    data format, and returns a date in the weather underground format.
'''

date = '12-12-90'
## Convert string data to time date formate

t= datetime.datetime.strptime(date,'%m-%d-%y')

 ## Convert   time date formate data to string data  as require formate
 
date_formatted = t.strftime('%y-%m-%d')