#latihan purwadhika

x = [40,100,99,5,25,10,900,3242,324,32,2,44,5,3]
c = 0

for i in range(len(x)-1):
    for a in range(i,(len(x))):
        # print(x[i],x[a])
        if x[i] > x[a]:
            c=x[i]
            x[i] = x[a]
            x[a] = c
           
print(int(c))
print(list(x))
print(x[0])
print(len(list(x)))
print (x[(len(list(x))-1)])

y = sorted(x)
print (y)

            
