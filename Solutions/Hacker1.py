#finding second largest element in list
li = list(map(int,input().split()))
li = list(set(li))
li.sort(reverse=True)
print(li[1])