i=0
j=1
c=0
while i <= 2:
  for x in range(3):
    if i == 0 or i == 1:
      print("I=%d J=%d" % (i,j+i))
    elif c == 10:
      i=2
      print("I=%d J=%d" % (i,j+i))
    else:
      print("I=%.1f J=%.1f" % (i,j+i))
    j+=1
  i+=0.2
  j=1
  c+=1