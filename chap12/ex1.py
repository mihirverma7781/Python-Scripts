# 158

def average_finder(*args):
    avg=[]
    for pair in zip(*args):
        avg.append(sum(pair)/len(pair))
    return avg
l1 = [1,3,5,7]
l2 = [2,4,6,8]
l3 = [3,5,2,3]
print(average_finder(l1,l2,l3))

# only in one line

m = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
print(m(l1,l2,l3))