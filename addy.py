import string
import random

times = int(input("Enter the number of times you would like to add: "))
addy1 = input("Enter Address 1: ")

def addy():
	size = 4
	chars1 = string.ascii_uppercase + string.digits
	chars2 = ''.join(random.choice(chars1) for _ in range(size))
	print(chars2+" "+addy1)


for i in range(times):
	addy()
