def factoriel(x) :
	u = 1
	for i in range (1 ,  x +1):
		u *= i
	return u


number  = int(input("enter your number :"))

print(factoriel(number))