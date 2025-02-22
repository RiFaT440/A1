email=[]
f=open("mbox.txt")
for line in f:
    line=line.split()
    if "From" in line:                
        email.append((line[1]))

print(set(email))
print(len(set(email)))