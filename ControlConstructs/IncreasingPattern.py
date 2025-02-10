rows = int(input("Enter a rows: "))
cols = int(input("Enter a cols: "))
for i in range(rows):
    for j in range(i+1):
        print("*", end="")
    print()
