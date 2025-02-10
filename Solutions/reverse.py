#reverse method will reverse original  objects
li = [ 10,20,30,40]
print("before reverse:", li)
li.reverse()
print("After reverse:",li)

#list(reversed())
li2 = [11,90,3,67]
reverse_li = list(reversed(li2))
print(reverse_li) #it will give iterator object
li3 = [1,5,2,9]
new_reverse_li3 = list(reversed(li3))
print(new_reverse_li3)