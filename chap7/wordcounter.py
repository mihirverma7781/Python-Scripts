# # word counter
# d={'a':3}

def wordcount(n):
    dic={}
    for i in n:
        dic[i]= n.count(i)
    return dic
print(wordcount('mihirverma'))