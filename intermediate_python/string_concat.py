import os
names = ['James','Giff','Dairy','Ben']

for name in names:
    statement = ' '.join(['Hello there', name]) # use to add strings
    print(statement)

who = 'Gary'
how_many = 12

print('{} bought {} apples today'.format(who,how_many)) # use to fill sentences

path1 = "puneeth/home/func"
path2 = "sonething/nothing"

print(os.path.join(path1,path2))   # to add paths seems simple but use only this don't add with +
