from faker import Faker
import numpy as nu
import pandas as p
import random
from datetime import datetime
import csv

def value():
    l=values=[nu.random.randint(2010,2021),3,nu.random.random_integers(1,2),nu.random.random_integers(2,5)]
    return l

def write_file(file_name,data):
    file=open(file_name,'a',newline='')
    writer=csv.writer(file)
    writer.writerow(data)

keys=['year','state','Suspected_object','People_Involved']

#write_file('test.csv',keys)
for i in range(0,100):
    write_file('test.csv',value())
 
      
        
