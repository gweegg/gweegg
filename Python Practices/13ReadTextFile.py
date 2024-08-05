file = open('file.txt', 'r')

f = file.readlines()
#print(f)

newList = []
# for line in f:
	# if line[-1] == '\n':
		# newList.append(line[:-1])
	# else:
		# newList.append(line)
# print(newList)

for line in f:
	newList.append(line.strip())
print(newList)

file.close() 