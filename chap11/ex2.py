def func(names,**kwargs):
    print(kwargs)
    if kwargs.get('reverse_str')==True:
        return [i[::-1].title() for i in names]
    else:
        return [i.title() for i in names]
    







m=['mihir','verma']
print(func(m,reverse_str = True))
