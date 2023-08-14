set_countries = {'Col', 'Mex', 'Bol'};

size = len(set_countries)
print(size)

print('Col' in set_countries)

# add
set_countries.add('Pe')
print(set_countries)
set_countries.add('Pe')
print(set_countries)

# update
set_countries.update({'Ar','Ecua','Pe'})
print(set_countries)

# remove
set_countries.remove('Ar')
set_countries.discard('Arg')
print(set_countries)

set_countries.clear()
print(set_countries)
