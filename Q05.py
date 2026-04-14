l=list(range(1,16)
for i  in range(len(l)):
  if l[i]%3==0 and l[i]%5==0:
       l[i]="fizz buzz"
  elif l[i]%5==0:
      l[i]="buzz"
  elif l[i]%3==0 :
        l[i]=" fizz"
print(l) 

