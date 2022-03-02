print('My name is')

for i in range(5):
	print('Jimmy Five Times ({})'.format(str(i)))


#The range() function can also be called with three arguments. 
# The first two arguments will be the start and stop values, and the third will be the step argument. 
# The step is the amount that the variable is increased by after each iteration.
for i in range(0, 10, 2):
    print(i)

#You can even use a negative number for the step argument to make the for loop count down instead of up.

for i in range(5, -1, -1):
    print(i)

