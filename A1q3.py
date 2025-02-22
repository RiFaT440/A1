Order=[]
f=open('amth.txt')
for line in f:
    if "Applied" not in line:
        line=line.split()
        for word in line:
            Order.append(word)
print(sorted(set(Order)))