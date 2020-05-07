def count(lst):
    c=0
    for i in lst:
       if len(i)>5:
           c+=1
    return c
lst1=[]
for i in range(10):
    lst1.append(input("enter the name"))
print(lst1)
print(count(lst1))