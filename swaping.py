# Python program to swap two variables

x = int(input('Enter the value of x: '))
y = int(input('Enter the value of y: '))

# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {0}'.format(x))
print('The value of y after swapping: {0}'.format(y))