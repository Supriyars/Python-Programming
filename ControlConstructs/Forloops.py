# for i in range(1, 11):
#     print(i)

for i in range(1,11):
    if(i%2==0):
        print(i)
    else:
        print("Number is not even")

i=0
while(i<10):
    print(i+100)
    i = i+1

for i in range(1,11):
    if(i==6):
        continue
    print(i)

for i in range(1,11):
    if(i==5):
        break
    print(i)