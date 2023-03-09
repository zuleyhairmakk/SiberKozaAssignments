# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

#create a dict
  person_zi={
      'first_name':'zuleyha',
      'last_name':'irmak',
      'age':26
  }
    #use constructor
    person2_zi = (first_name='sara',last_name="williams)
    #get value
    print(person_zi['first_name']
    print(person_zi.get['last_name']
    #add key/value
    person['phone'] = '56554-5144-544'
    #get dict keys
    print(person_zi.keys())
    #get dict items 
    print(person_zi.items())   
    #copy dict
    person2_zi = person_zi.copy()
    person2['city'] = 'boston'
    #remove item
    del(person_zi['age'])
    person_zi.pop('phone')
          
    #clear
    person_zi.clear()
    #length
    print(len(person2_zi))
          
    #list of dict 
          people_zi = [
              {'name': 'martha','age':30}
               ]
          print(people_zi)
          
    print(person_zi)