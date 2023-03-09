# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name_zi='zuleyha'
age_zi=26

#Concatenate
print('hello, my name is' + name_zi + ' and I am ' + str(age_zi))

# String Formatting

#Argument by position

print('My name is {name_zi} and I am {age_zi}'.format(name_zi=name_zi,age_zi=age_zi ))

#F-String(3.6+)
print(f'Hello my name is {name_zi} and I am {age_zi}')

# String Methods

s_zi='hello world'

#capitilaze string
print(s_zi.capitilaze())

#uppercase
print(s_zi.upper())

#lowercase
print(s_zi.lower())

#swapcase
print(s_zi.swapcase())

#get lenght
print(len(s_zi))

#replace
print(S_zi.replace('world', 'everyone'))

#starts with
print(s_zi.startwith('d))
 
#find position
print(s_zi.find('r'))
                     
#split
print(s_zi.split())
#is all alphabetic
print(s_zi.isalpha())
       
