list = [1,1,1,2]
r1 = (0,1)
r2 = (0,1,2)
r3 = (0,1)
combinations = [[i,j,k] for i in range(r1+1) for j in range (r2+1) for k in range (r3+1) if i+j+k!=2 ]
print(combinations)
