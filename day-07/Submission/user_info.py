file = open('user_info.txt.' , 'w')

sentence = input("Enter your name: ")

file.write(sentence)

file.close()
