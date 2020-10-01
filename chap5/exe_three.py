list_str = ['abc','tuv','lmn']

def str_rev(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements
print(str_rev(list_str))
