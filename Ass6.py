'''n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)'''

for i in range(1,31):
    for j in range(1,31):
        print(i * j, end="\t")
    print()