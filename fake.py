from faker import Faker
import numpy as nu
import pandas as p
import random
from datetime import datetime
import csv

#def fake():
    
    #f=Faker()
    
    #obj=set()
 
    #out=[{
         #nu.random.randint(2010,2021),
         #33,
         #nu.random.random_integers(1,2),
         #nu.random.random_integers(2,5)
    
    #}]
    #for i in range(1,101):
        #obj.add(out)
        #return obj
   
    
    


with open('dat.csv', 'w', encoding='UTF8',newline='') as f:
    # create the csv writer
    writer = csv.writer(f)
    keys=['year','state','Suspected_object','People_Involved']   
    # write a row to the csv file
    #writer.writerow(fake())
    count=0
    for data in range(1,100):
        values=[nu.random.randint(2010,2021),2,nu.random.random_integers(1,2),nu.random.random_integers(2,5)]
        
        if count == 0:
            header = keys
            writer.writerow(header)
            count += 1
            
        
        writer.writerow(values)
 
      
        