# f = open('file1.txt')
# f.read()
# f.close()

# with block
# context manager
with open('file2.txt','r+') as f:
    f.seek(len(f.read()))
    f.write('\n  is neccesary')
    

print(f.closed)
