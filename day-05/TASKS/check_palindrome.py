# Write the code ↓ to prompt the user to enter a word.
print("PALINDROME CHECKER FOR ALF")

word = input("Please, enter a word/s to check: ")
# Be cautious when reading input of various data types.







# Write the code ↓ to check if the entered word is a palindrome.
reversed_word = word[::-1]
# Utilize string functions to compare the original word with its reverse.






# Write the code ↓ to display whether the entered word is a palindrome or not.
if reversed_word == word:
    print("'%s' is a palindrome" %(word))
else:
    print("'%s' is not a palindrome" %(word))
# Select and employ a string concatenation method based on your personal preference and comfort level.






