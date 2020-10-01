# iterating in a word
it=[i for i in 'humans']
print(it)

# positive no finder
num=[11,-11,23,-44.4,22,67,-98.5,3.5,5,45,35,6,5,55]
pos=[i for i in num if i>0]
print(pos)

# copy of list

# def copi(l):
#     copied =[i for i in l]
#     print(copied)
# copi(num)

# #double 
# def dbl(m):
#     doub=[i*2 for i in num]
#     print(doub)
# dbl(num)


# even
# def even(l):
#     eve=[i for i in num if i%2==0]
#     print(eve)
# even(num)


# making string
# def st(l):
#     s=[str(i) for i in num if i%5==0]
#     print(s)
# st(num)

sent = 'i am slipping through the cracks of your cold embrace'
def s(m):
    l=[]
    for i in m:
        if i == ' ':
            continue
        else:
            l.append(str(len(i)))
    print(l)
s(sent)