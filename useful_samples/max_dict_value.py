import random
import time

n = 1_000_000
d = {}
for i in range(n):
    d["v"+str(i)]=random.randint(0,n)

start = time.time()
print( max(d.items(), key=lambda x: x[1])[0], time.time()-start )

start = time.time()
print( max(d, key=d.get) , time.time()-start )


