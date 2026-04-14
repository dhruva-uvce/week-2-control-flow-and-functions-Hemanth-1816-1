
l=1234
sum=0
for i in range(len(str(l))):
    rem=l%10
    sum+=rem
    l=l//10
print("sum is",sum,"got ans")    
