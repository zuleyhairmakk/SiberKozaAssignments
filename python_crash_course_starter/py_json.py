# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary


import json

#sample json
z_userJSON = '{"first_name": "jhon", "last_name": "Doe", "age":30 }

#parse to dict
user = json.load(z_userJSON)
print(user)
print(user['first_name'])


#opposite
 car = {'name': 'ford' , 'moduul': 'mustang', 'year':1970 }
    carJSON =json.dumps(car)
    print(carJSON)
    
 