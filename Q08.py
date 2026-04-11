# Q08. Sum of Digits (while loop)
#
# Ask the user for a positive integer.
# Print the sum of its digits using a while loop.
#
# Sample Input:   Enter a number: 9876
# Sample Output:  Sum of digits of 9876 = 30

# --- YOUR CODE HERE ---
l=1234
sum=0
for i in range(len(str(l))):
    rem=l%10
    sum+=rem
    l=l//10
print("sum is",sum,"got ans")    
