year = 2019
event = 'Referendum'

print(f'Results of the {year} {event}')

# Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is
# useful for making columns line up
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

for name, phone in table.items():
  print(f'{name:10} ==> {phone:10d}')

# The str.format()
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))