li1 = [1,2,3,4,5]
duplicate_li1 = [i for i in li1]
print(duplicate_li1)
even = [i for i in li1 if(i%2==0)]
print(even)
sq_root = [i**2 for i in li1]
print(sq_root)
new_ele = [ele+2 for ele in li1]
print(new_ele)
even_odd = ['even' if(i%2==0) else 'odd' for i in li1]
print(even_odd)
#Multiple for loops inside list comprehension
li = [[10,20],[30,40],[50,60]]
new_li = [ele for sublist in li for ele in sublist]
print(new_li)