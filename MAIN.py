from MultInv import *
import random


def convertToIntList(strInput):

	strInput = strInput.lower()

	numInput = [ord(i) - 96 for i in strInput]

	for i in range(len(numInput)):
		if numInput[i] < 0:
			tempIndex = i
			numInput.pop(i)
			numInput.insert(i, 0)

	return numInput


#pubKey is (p * q, e),p and q are both unique prime numbers and e is a number that is relatively prime to (p-1)(q-1))
def encyrptMessage(msg, pubKey):

	
	msg = convertToIntList(msg)

	outputList = []

	for i in range(len(msg)):
		outputList.append((msg[i] ** pubKey[1]) % pubKey[0])

	return outputList




def decryptMessage(msg, p, q, e):
	
	d = modinv(e, (p-1)*(q-1))

	outputList = []

	for i in msg:
		outputList.append((i ** d) % (p * q))

	return outputList


#This brute force solver doesn't work
def bruteForceSolve(numList, correctSolution):

	counter = 0
	e = 3
	test = []
	while test != correctSolution:
		for p in range(1, 100):
			for q in range(1, 100):
				d = modinv(e, (p-1)*(q-1))
				counter += 1
				for i in numList:
					test.append((i ** d) % (p * q))
					if test == correctSolution:
						break

				test = []
	print(test)

def isPrime(n):
    
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5), 2):
        if n % i == 0:
            return False

    return True

"""

print(convertToIntList('RENSBERGER')) #Shows what the output should look like after we decrypt

print(encyrptMessage('RENSBERGER', (5 * 11, 3))) #Encryptes HI with the output 17 14

print(decryptMessage([2, 15, 49, 39, 8, 15, 2, 13, 15, 2], 5, 11, 3)) #Decrypts 17 14 with the output 8 9 which when converted back to plaintext is HI

"""



print('Question 1: TOY PROBLEM encrypting my last name: RENSBERGER with the primes p=11 q=29 e=3')
print()
print('After decryption the output should be equal to')
print(convertToIntList('RENSBERGER'))
print('The encrypted message is')
print(encyrptMessage('RENSBERGER', (11 * 29, 3)))
print('The decrypted message is')
print(decryptMessage([90, 125, 192, 160, 8, 125, 90, 24, 125, 90], 11, 29, 3))

print()
print()

print('Question 2: Now implementing a function to find a 10 bit prime number since my last name, RENSBERGER, is 10 characters long')
print()
print('The decimal range of 10 bit numbers is 256 to 1023 so using the function I wrote I will generate every prime value within that range')
print()
primes = []
for i in range(256, 1024):
	if isPrime(i):
		primes.append(i)

print(primes)

print()
print('Then, using the random library, we can pick one of these 10 bit prime values')
print('Random value: ' + str(random.choice(primes)))

