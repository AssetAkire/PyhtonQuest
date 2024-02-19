# Write the code ↓ to prompt the user to enter a word.
print("VOWEL COUNTER FOR ALF")

Word = input("Please, enter a word/s to check: ").lower()
# Be cautious when reading input of various data types.








# Write the code ↓ to count the number of vowels in the entered word.
a_count = Word.count('a')
e_count = Word.count('e')
i_count = Word.count('i')
o_count = Word.count('o')
u_count = Word.count('u')
total = a_count + e_count + i_count + o_count + u_count
# Utilize string functions to iterate through the characters and identify vowels.







# Write the code ↓ to display the count of vowels in the word.
print("The number of vowels in '%s' is: %d" %(Word, total))
# Select and employ a string concatenation method based on your personal preference and comfort level.
        





