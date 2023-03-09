# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#create tuple

fruits_zi=('apples', 'oranges', 'grapes')
#fruits2_zi= tuple(('apples', 'oranges', 'grapes'))

#single value needs trailing comma
fruits2_zi('apples',)
print(fruits2_zi, type(fruits2_zi))

#get value
print(fruits2_zi[1])

#cannot change value
fruits2_zi[0]= 'pears'
#delete tuple
del fruits2_zi
#get length
print(len(fruits_zi)
# A Set is a collection which is unordered and unindexed. No duplicate members.
#creare a set 
fruits_set_zi={'apples','oranges','mango'}
      
#check if in set
print('apples' in fruit_set_zi)
      
#add duplicate
fruits_set_zi.add('apples')
      
#add to set 
fruits_set_zi.add('grape')
      
#remove
fruits_set_zi.remove('apple')
      
#clear set
fruits_set_zi.clear()
      
#delete 
del fruits_set_zi
      
print(fruits_set_zi)
      
      
      
      
      
      
      
      
      