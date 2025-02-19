my_dict = {}
my_dict = {1: 'apple', 2: 'ball'} 
my_dict = {'name': 'jhon', 1: [2, 4, 4]}
my_dict = {'name': 'jack', 'age': 20}
print(my_dict['name'])
print(my_dict.get('age'))
my_dict['age'] = 23
print(my_dict)
my_dict['address'] = 'Downtow'
print(my_dict)
my_dict.pop('age')
print(my_dict)
print("Adress :", my_dict.get('address'))
my_dict.clear()
print(my_dict)
