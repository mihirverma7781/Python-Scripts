def li(le):
    return [i for i in le if (type(i) == int or type(i)==float)]
no=[[1,2,3],'mihir','verma',1,2.2,4.4,4,5,(1,2),[2,34],'mv']

print(li(no))
