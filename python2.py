string=input()
number=len(string)
max1=[]
for i in range(number-1):
    for num in range(1,number-i):
        for z in range(i+1,number-num+1):
            if string[i:i+num]==string[z:z+num]:
                max1.append(num)
if len(max1)==0:
    print(int(0))
else:
    print(max(max1))
