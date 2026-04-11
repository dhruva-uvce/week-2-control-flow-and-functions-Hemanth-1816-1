# Q01. Grade Calculator (if-elif-else)
#
# Ask the user for a score (integer, 0-100).
# Print the letter grade using these rules:
#   90-100  → A
#   80-89   → B
#   70-79   → C
#   60-69   → D
#   Below 60 → F
#
# If the score is below 0 or above 100, print "Invalid score".
#
# Sample Input:   Enter your score: 85
# Sample Output:  Grade: B

# --- YOUR CODE HERE ---
i=int(input("enter the score:"))
if i<0 or i>100:
  print("invalid score")
elif i>=90 and i<=100:
  print("a")
elif i>=80 and i<=89:
  print("b")
elif i>=70 and i<=79:
  print("c")
elif i>=60 and i<=69:
  print("D")
elif i<0 and i>100:
  print("invalid score")
else :
   print("f")
  
  git add .
git commit -m "Completed Week 2 assignment"
git push

