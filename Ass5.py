s1 = int(input("Subject 1 Marks: "))
s2 = int(input("Subject 2 Marks: "))
s3 = int(input("Subject 3 Marks: "))
s4 = int(input("Subject 4 Marks: "))
s5 = int(input("Subject 5 Marks: "))
per = (s1 + s2 + s3 + s4 + s5) / 5
print("Percentage =", per)
if s1 < 35 or s2 < 35 or s3 < 35 or s4 < 35 or s5 < 35:
    print("Failed in Subject")
elif per >= 75:
    print("Distinction")
elif per >= 60:
    print("First Class")
elif per >= 50:
    print("Second Class")
elif per >= 35:
    print("Pass")
else:
    print("Fail")