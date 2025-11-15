size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:
    for i in range(size):
        print("*", end="")
    # Move to the next line after each row
    print()
    row += 1
 
