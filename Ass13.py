def armstrong(n):
    s = 0
    for i in str(n):
        s += int(i)**3
    print("Armstrong" if s == n else "Not Armstrong")
armstrong(153)
armstrong(370)
armstrong(123)