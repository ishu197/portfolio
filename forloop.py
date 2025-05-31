list = [1,2,3,4,5,6]
print(list)
print(list[0])
print(list[1])

for adfa in list:
    print("list:",adfa)

for i in range(1,11,3):
    print("range:",i)

for i in range(1,5):
    value = i%2
    print("value",value)
    if value!=0:
        if i==1:
            break
        if v==0:
            print("odd:",i)
    else:
        print("even:",i)

name=("computer")
for i in range(9):
    print(name[0:i])
