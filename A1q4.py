f=open("mbox.txt")
t=0
count=0
for line in f:
    line=line.strip()
    line=line.split(":")
    if "X-DSPAM-Confidence" in line:
        count+=1
        t+=float(line[1])
print("Total count:",count) 
avg=t/count
print(f"Average spam confidence: {avg:.4f}")