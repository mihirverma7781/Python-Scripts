user_info ={
'name':'mihir',
'age':19,
'fav_movies':['titanic','harry potter','passengers'],
'fav_songs':['aadat','tum se hi','aansan nahi yaha'],
}

# check if key exist in dict

if 'names' in user_info:
    print('y')
else:
    print('n')

# check the values exist
if 'mihir' in user_info.values():
    print('y')
else:
    print('n')

# loops in dict

for i in user_info.values():
    print(i)

o = user_info.values()
print(o)

# keys method

m= user_info.keys()
print(m)

# pritnting values with keys in loop
for i in user_info:
    print(user_info[i])

# item method
user1= user_info.items()
print(user1)
print(type(user1))
    

for key, values in user_info.items():
    print(f" {key} == {values}")