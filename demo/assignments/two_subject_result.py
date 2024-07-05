# calculate the result with subject 1 and subject 2

s1_mark = int(input("Enter s1_mark:"))
s2_mark = int(input("Enter s2_mark:"))

if s1_mark >= 50 and s2_mark >= 50:
    print("pass")
elif s1_mark > 70 or s2_mark > 70:
    print("pass")
elif s1_mark + s2_mark > 110:
    print("pass")
else:
    print("fail")
