import os
data=[{'name': 'aakash kumar', 'phone': '987654567', 'age': '20', 'id': '2', 'expire': '7/6/2021'}, {'name': 'sudhakar kumar', 'phone': '23457654', 'age': '18', 'id': '3', 'expire': '7/6/2022'}, {'name': 'daniyal haider', 'phone': '23654', 'age': '19', 'id': '4', 'expire': '7/6/2020'}, {'name': 'junaid khan', 'phone': '6456789', 'age': '26', 'id': '5', 'expire': '7/6/2021'}]
namef=open('database_test.txt','r+')
for i in range(len(data)):
    namef.write(data[i]['name']+'\n')



