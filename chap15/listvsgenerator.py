# memory test
# list first
import time
t1=time.time()
m=[i**2 for i in range(1,10000000 )]
t2=time.time()
print(t2-t1)

# generator
m=[i**2 for i in range(1,10000000)]
