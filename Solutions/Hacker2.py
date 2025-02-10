#find second smallest element in list
li = list(map(int,input().split(',')))
li=list(set(li))
li.sort() #sort method wont return anything and "null" will be returned.
print("Smallest element: ",li[0])
print("Second smallest element: ",li[1])
print("Largest element: ",li[-1])
print("Second Largest element: ",li[-2])



