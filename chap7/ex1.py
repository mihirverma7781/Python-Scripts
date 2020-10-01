def cube_finder(n):
    dic= {}
    for i in range(1,n+1):
        dic[i] = i**3
    return dic

print(cube_finder(10))
        