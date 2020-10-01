user_info ={
'name':'mihir',
'age':19,
'fav_movies':['titanic','harry potter','passengers'],
'fav_songs':['aadat','tum se hi','aansan nahi yaha'],
}

# how to add data
user_info['fav_actors']=['akki','sallu']
print(user_info)
popped=user_info.pop('fav_songs')
print(popped)
print(user_info)

# pop item method

popped_item =user_info.popitem()
print(f"popped =  {popped_item}")