# If/ Else conditions are used to decide to do something based on something being true or false

x_zi =10
y_zi =5



# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# we can say simple if 
if x_zi > y_zi:
    print(f'{x_zi} is greater than {y_zi}')
 #else
f x_zi > y_zi:
    print(f'{y_zi} is greater than {x_zi}')
    
#elif operator

if x_zi > y_zi:
    print(f'{x_zi} is greater than {y_zi}')

elif x_zi == y_zi:

    print(f'{x_zi} is equal to {y_zi}')
else:
f x_zi > y_zi:
    print(f'{y_zi} is greater than {x_zi}')
    
#Nested if 
if x_zi > 2:
    if x<=10:
        print(f'{x_zi} is greater than 2 and less than or equal to 10')
        

# Logical operators (and, or, not) - Used to combine conditional statements

#and conditional
if x_zi > 2 and  if x<=10:
        print(f'{x_zi} is greater than 2 and less than or equal to 10')

#or conditional 
if x_zi > 2 or if x<=10:
        print(f'{x_zi} is greater than 2 or less than or equal to 10')
        
#not conditional
if not(x_zi == y_Zi):
    print(f'{x_zi} is not equal to {y_zi}')
    
# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers_zi = [1,2,3,4,5]
# in conditional 
if x_zi in numbers_zi:
    print(x in numbers)
    

#not in conditional 
if  x_zi not  in numbers_zi:
    print(x not in numbers)
# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
#is
if x_zi is y_zi:
    print(x_zi is y_zi)
#is not 
if x_zi is not y_zi:
    print(x_zi is not y_zi)
