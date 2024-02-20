file = open('story.txt', 'r')

content = file.readlines()
line_count = len(content)

print(content)
print("\nNumber of lines:", line_count)

file.close()
