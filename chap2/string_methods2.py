# fine and replace method
string = 'is name is mihir is verma'
print(string.replace(" ","_"))
print(string.replace("my","the"))

# find method
pos1 = string.find("is")
pos2=string.find("is",pos1+1)
print(string.find("is",pos2+1))