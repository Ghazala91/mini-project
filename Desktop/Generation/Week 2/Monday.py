my_list = ['cat', 'dog']
print (my_list)

# append
my_list.append('snakes')
print('new list', my_list)

# insert
my_list.insert (1, 'new item' )
print (my_list)

# edit
my_list[1] = 'camel'
print(my_list)

# remove
my_list.remove('snakes')
print('list after delete', my_list)

# pop
my_list.pop(1) # without index it will remove last element from list
print(my_list)

# del
del my_list[0]
print(my_list)