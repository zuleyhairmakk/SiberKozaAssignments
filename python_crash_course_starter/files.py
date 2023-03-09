# Python has functions for creating, reading, updating, and deleting files.


#open a file 
myFile = open('myFile.txt', 'w')


#Get some info from file
print('Name : ' , myFile.Name)
print('Is Closed : ' , myFile.Closed)
print('Mode : ' , myFile.Mode)


#Write to file
myFile.write(' I love python ' )
myFile.write(' and I also love javaScrript')
myFile.close()

#Append a file
myFile = open('myFile.txt', 'a')
myFile.write(' I also  like php ' )
myFile.close()


#Read from a file 
myFile = open('myFile.txt', 'r+')
z_text = myFile.read(100)
print(z_text)