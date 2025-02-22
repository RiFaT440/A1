import re 
print("Roll","    Grade","    GPA")
print("----","    -----","    ---")
f=open("marks.txt")
for line in f:
  txt=line.strip()
  a,b,c,d,e=txt.split()
  ress=(int(c)+int(b))/2+int(d)+int(e)
  if ress>=80 and ress<=100:
    print(a,'      A+','        4.00')
  elif ress>=75 and ress<80:
    print(a,'      A','         3.75')
  elif ress>=70 and ress<75:
    print(a,'      A-','        3.5')
  elif ress>=65 and ress<70:
    print(a,'      B+','        3.25')
  elif ress>=60 and ress<65:
    print(a,'      B','         3.00')
  elif ress>=55 and ress<60:
    print(a,'      B-','        2.75')
  elif ress>=50 and ress<55:
    print(a,'      C+','        2.50')
  elif ress>=45 and ress<50:
    print(a,'      C','         2.25')
  elif ress>=40 and ress<45:
    print(a,'      D','         0.0')
  elif ress>=0 and ress<40:
    print(a,'      F','         0.00')
  else:
    print(a,"     Number is invalid")