# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#create a class
class User:
    #Constructor
    def _init_(self, z_name, z_email, z_age):
        self.z_name = z_name
        self.z_email = z_email
        self.z_age = z_age
        
    def greeting(self)
        return f 'My name is ' {self.z_name} 'and I am ' {self.z_age} 'years old'
        
    def has_Birthday(self)
        self.z_age += 1 

#Extend class
class Customer(User):
    def _init_(self, z_name, z_email, z_age):
        self.z_name = z_name
        self.z_email = z_email
        self.z_age = z_age
        self.z_balance = 0 
        
    def set_balance(self, z_balance)
       self.balance = z_balance
        
        
        
        
    def greeting(self)
        return f 'My name is ' {self.z_name} 'and I am ' {self.z_age} 'years old' {self.z_balance}'is my balance'
    
        
        
 #Init customer Object 
 z_Janet = Customer('janet johson', 'jjohson@yahoo.com',25)
    z_Janet.z_balance(5000)
    
    





        
#Init a object 
z_brad = User('Brad Traversy', 'brad@gmail.com',37)
print(type(z_brad))
print(type(z_brad.z_name))
print(type(z_brad.z_age))


z_brad.hasBirtday()
print(z_brad.greeting())

      


        