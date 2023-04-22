r = 0
n = 5

print("n: " + str(n))
print()

for i in range(n, 0, -1):
    print("i: " + str(i))

    for j in range(n, 0, -1):
        print("j: " + str(j))

        if (i * j <= n):
            r = r + 1
            print("yay!")
            
    print()
    
print("r: " + str(r))