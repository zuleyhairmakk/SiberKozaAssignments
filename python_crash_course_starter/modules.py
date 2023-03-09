# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#core modules 
import datetime
from datetime import date 
import time import time 
#pip module
from camelcase  import CamelCase

#Custom modules
import validator
from validator import validate_email

today_zi = datetime.date.today() #look the documentatuon

today_zi_date.today #when we use from date time import date  code 

timestamp =time.time()
print(timestamp)
print(today_zi)



c_zi = CamelCase()
print(c.hump('hello there world'))

z_email = 'test@test.com'
if validate_email(email):
    print('email ls validate')
    
else:
    print('email is not validate')
    



#for instaling any packet we use pip install command 
