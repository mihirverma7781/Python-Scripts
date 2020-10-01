user = {}
name = input('enter your name : ')
age = int(input('ener your age : '))
fav_movies = list(input('enter fav movies : ').split(','))
fav_songs = list(input('enter fav songs : ').split(','))

user['name']=name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs
print(user)

for key,values in user.items():
    print(f"{key} == {values}")
