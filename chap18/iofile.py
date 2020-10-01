# readfile
# open fucntion 
# read method
# seek method
# ṭell methodd
# read line method
# read lines method
# close method 

f = open('file1.txt','r')
print(f"cursor position {f.tell()}")
# print(f.readline(), end ="")
# print(f.readline())

lines = f.readlines()
print(len(lines))
for line in lines:
    print(line, end=" ")

print(f.name)

# print(f.read())
# print(f"cursor position {f.tell()}")
# f.seek(0)
# print(f"cursor position {f.tell()}")
# print(f.read())
f.close()
print(f.closed)