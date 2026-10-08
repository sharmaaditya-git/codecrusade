for i in range(7):
    for j in range(i+1):
        if i ==3 and j ==2:
            pass
        elif i ==4 and j==2:
            print(" ")
        elif i ==4 and j==3:
            pass
    print("*", end="")
print()


rows = int(input("Enter num:"))

for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end="")

    # Print stars and inner spaces
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == rows:
            print("*", end="")
        else:
            print(" ", end="")
 
    print()