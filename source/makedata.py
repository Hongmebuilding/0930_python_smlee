import random as rd
import numpy as np
import pandas as pd

def get_name():
    names = ['Doyle','Christie','Connelly','Chandler','Poe','Hammet','Child','Sayers'
            ,'Carre','Leonard','King']
    return rd.choice(names)

def get_age(start=20, end=40):
    return np.random.randint(start, end+1)

def make_data(rows=10):
    datas = []
    for i in range(rows):
        data = {'Age':get_age(), 'Name':get_name()}
        datas.append(data)
    return datas

# for Test
#print(make_data(3))