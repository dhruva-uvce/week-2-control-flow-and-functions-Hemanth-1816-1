# Q05. FizzBuzz (for loop + if-else)
#
# Ask the user for a positive integer n.
# Print all numbers from 1 to n, but:
#   - For multiples of 3, print "Fizz" instead of the number
#   - For multiples of 5, print "Buzz" instead of the number
#   - For multiples of both 3 and 5, print "FizzBuzz"
#
# Sample Input:   Enter n: 15
# Sample Output:
#   1
#   2
#   Fizz
#   4
#   Buzz
#   ...
#   FizzBuzz

# --l=list(range(1,16))


    
l=list(range(1,16)
for i  in range(len(l)):
  if l[i]%3==0 and l[i]%5==0:
       l[i]="fizz buzz"
  elif l[i]%5==0:
      l[i]="buzz"
  elif l[i]%3==0 :
        l[i]=" fizz"
print(l) 

