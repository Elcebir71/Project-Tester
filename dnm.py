sm ,lst,order= 0,[0],[0]
h=lst[0]
for i in range(1,24):
    sm=sm^i
    lst.append(sm)
    order.append(i)
print(lst)
print(order)
for j in range(5,len(lst)):
    #print(h,lst[j])
    h = h ^ lst[j]

print(h)
