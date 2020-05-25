a=[1,2,3,4,5,6,7,8]
for item in range(1,len(a),2):
    print(item,end=" | ")

a=[1,2,3,4,5,6,7,8]
for num in range(0,8,2):
    print(a[num],end=" | ")

a=[1,2,3,4,5,6,7,8]
i=0
while i<len(a):
    print(a[i],end=" | ")
    i+=2
