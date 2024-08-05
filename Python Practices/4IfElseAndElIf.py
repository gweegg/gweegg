# if condition == True: 
#	do this

#age = input('Input your age: ')
#
#if int(age) >= 16:
#	print('Hey your ' + age + '!')
#else: 
#	print('You are younger than 16!')

height = input("Enter your height: ")

if int(height) < 1:
	print('Please enter a number greater than 1.')
elif int(height) <= 2:
	print('You cannot ride, over ' + height + 'm')
else: 
	print('You can ride. Enjoy!')