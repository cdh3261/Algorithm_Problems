import time
start = time.time()

a = []
for v in range(1,10000000):
    a += [v]
print('{}초 걸림'.format(time.time()-start))

start2 = time.time()
b = []
for i in range(1,10000000):
    b.append(i)
print('{}초 걸림'.format(time.time()-start2))

start3 = time.time()
d = [i for i in range(1,10000000)]
print('{}초 걸림'.format(time.time()-start3))



# 1.4172654151916504초 걸림
# 1.027250051498413초 걸림
# 0.4697437286376953초 걸림

st1 = time.time()
f,g=[],[]
for i in range(1,10000000):
    if i%2:
        f.append(i)
    else:
        g.append(i)
print('{}초 걸림'.format(time.time()-st1))

st2 = time.time()
j,k=[],[]
for i in range(1,10000000):
    j.append(i) if i%2 else k.append(i)
print('{}초 걸림'.format(time.time()-st2))