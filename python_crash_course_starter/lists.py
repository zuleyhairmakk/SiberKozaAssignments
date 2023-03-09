# A List is a collection which is ordered and changeable. Allows duplicate members.

#Create list
numbers_zi = [1,2,3,4,5]
fruits_zi = ['apples', 'oranges', 'grapes', 'pears']

#use a constructur 
number2_zi = list((1,2,3,4,5))

print(numbers_zi, number2_zi))

#get a value 
print(fruits_zi[1])

#get length
print(len(fruits_zi))

#append to list 
fruits_zi.append('mangos')

#remove from list 
fruits_zi.remove('grapes)
                 
        
#insert into position
fruits_zi(2,'strawberries')
                 
#remove by  position
fruits_zi.pop(2)
                 
#reverse list 
fruits_zi.reverse()

                 
#sort list
fruits_zi.sort()
 #reverse sort
 fruits_zi.sort(reverse=True)

#change value 
fruits_zi[0]='blueberries'
print(fruits_zi)
                 