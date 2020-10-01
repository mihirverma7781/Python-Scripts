# from keys
d= {'name':'unknown','age':'unknown'}
d = dict.fromkeys(['name',"age"],'mihiir')
print(d)

# getmethod
d= {'name':'unknown','age':'unknown'}
# print(d['name'])
print(d.get('name'))

# clear

# d.clear()
# print(d)


# copy method
# d1 =d.copy()    #nai copy generate karega
d1 = d  #ye same dictionary hai changes dono me ho jaenge
print(d1)

print(d1 is d)