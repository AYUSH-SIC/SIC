def my_range(start,stop,step):
    list = []
    if start>stop and step>0:
        return list
    for i in range(start,stop,step):
        list.append(i)
    return list
print(my_range(0,10,2))
print(my_range(10,0,9))