# -*- coding: utf-8 -*-
"""
Created on Wed May 20 01:51:02 2020

@author: Walton
"""

import pandas as pd
import pandasql as ps

weather_data = pd.read_csv("weather_underground.csv")

## count the rainy day
q ="""SELECT count(*) FROM weather_data WHERE rain ==1 ;"""
rainy_days = ps.sqldf(q.lower(),locals())
print(rainy_days)

## Temp on Foggy and Nonfoggy Days
q="""SELECT fog,maxtempi FROM weather_data  GROUP BY fog;"""
Fogy_days = ps.sqldf(q.lower(),locals())
Fogy_days
 
 ## Mean Temp on Weekends
f="""SELECT avg(cast(meantempi as integer)) FROM weather_data  
     WHERE cast(strftime('%w', date) as integer) in (6,0) ;""" 

mean_temp_weekends = ps.sqldf(f.lower(),locals())

##Mean Temp on Rainy Days
q = """
    SELECT avg(cast(mintempi as intiger))FROM weather_data WHERE rain=1 AND cast(mintempi as intiger) > 55 ;
    """
    
avg_min_temp_rainy = ps.sqldf(q.lower(), locals())
