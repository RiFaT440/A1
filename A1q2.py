n=[]
f=open("regex-sum-42.txt")
for line in f:
    parts=line.split()
    for num in parts:
        if num.isdigit():
            n.append(float(num))
print(sum(n))