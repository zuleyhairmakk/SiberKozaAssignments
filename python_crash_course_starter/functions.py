# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces




#create function
def sayHello(name):
    print(f'Hello my name is {name}')
    
    
sayHello('zuleyha') #equals def sayHello(name='zuleyha')

#Return values 
def getSum(num1, num2):
    totalNumber = num1 + num2
    return totalNumber
num = getSum(2,2)
print(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2
print(getSum(17,3)