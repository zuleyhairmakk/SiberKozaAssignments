# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
x_zi = 1 #int
y_zi = 2.5 #float
name_zi = 'zuleyhairmak'  #string
is_cool_zi = True   #boolean type

#multiple assigment
 x_zi,y_zi,name_zi,is_cool_zi = (1,2.5, 'zuleyhairmak',True)
    
    
#basic mat operator
a_zi = x_zi+y_zi
print(x_zi,y_zi, name_zi, is_cool_zi,a_zi)

print(type(a_zi))

#casting
x_zi=str(x_zi)
y_zi=int(y_zi)
z_zi=float(y_zi)



