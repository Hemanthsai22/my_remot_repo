a = 0
print('*'*50)
n = int(input('Enter a with we want check prime or not:'))
print('*'*50)
for i in range(1,n+1):
	if(n%i==0):
		a = a+1
if(a==2):
	print(n,'is a prime number')
else:
	print(n,'is not a prime number')