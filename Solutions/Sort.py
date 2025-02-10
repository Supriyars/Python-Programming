li = [10,30,15,7,23,12]
li.sort() #sort in ascending
print(li)
li.sort(reverse=True) #sorting in descending
print(li)

#sort() will sort the original copy of list
#sorted() will store the copy of sorted list

#sorted()
li2 = [100,30,45,98,12]
sorted_li = sorted(li2)
print(sorted_li)