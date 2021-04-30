# Dictionary Comprehension

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

#creates a dictionary from two lists using a Dictionary Comprehension
my_dict = {name: hero for name, hero in zip(names, heros)}
print (my_dict)

#creates a dictionary from two lists using a Dictionary Comprehension
# this example uses an if statement to exclude Peter
my_dict = {name: hero for name, hero in zip(names, heros)if name != 'Peter'}
print (my_dict)

# same as above using a for loop
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print (my_dict)

