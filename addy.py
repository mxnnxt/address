import string
import random
from random import getrandbits
#USER INPUT 
times = int(input("Enter the number of times you would like to jig: "))
addy1 = str(input("Enter Address 1: "))
phone = input("Phone Number Prefix: ")

text_file = open("ADDY.txt", "w")

# ADDRESS 1 FUNCTION
def addy():
	size = 4
	chars1 = string.ascii_uppercase + string.digits
	chars2 = ''.join(random.choice(chars1) for _ in range(size))
	text_file.write(chars2+" "+addy1 + "\n")
	print(chars2+" "+addy1)
# ADDRESS 2 FUNCTION
def addy2():
	numbers = random.sample(range(10), 4)
	num1 = str((''.join(map(str, numbers))))
	size1 = 4
	chars3 = string.ascii_uppercase + string.digits
	chars4 = ''.join(random.choice(chars3) for _ in range(size1))
	text_file.write(chars4+" "+"APT "+num1 + "\n")
	print(chars4+" "+"APT "+num1)

#PRINT AND EXPORT ADDRESS 1 TO TXT
print("")
print("ADDRESS 1: ")
text_file.write("ADDRESS 1:" + "\n")
print("")

for i in range(times):
	addy()

#PRINT AND EXPORT ADDRESS 2 TO TXT
print("")
print("ADDRESS 2: ")
text_file.write("ADDRESS 2:" + "\n")
print("")

for i in range(times):
	addy2()
#PRINT AND EXPORT PHONE NUMBER TO TXT
print("")
print("PHONE NUMBER: ")
text_file.write("PHONE NUMBER:" + "\n")
print("")

for i in range(times):
	number5 = random.sample(range(10), 7)
	num2 = str((''.join(map(str, number5))))
	text_file.write(phone+num2 + "\n")
	print(phone+num2)

#PRINT AND EXPORT FIRST NAME TO TXT
print("")
print("FIRST NAME: ")
text_file.write("FIRST NAME:" + "\n")
print("")

for i in range(times):
	names = ["Beck","Glenn","Becker","Carl","Beckett","Samuel","Beddoes","Mick","Beecher","HenryWard","Beethoven","Ludwigvan","Begin","Menachem","Bell","Alexander","Graham","Belloc","Hilaire","Bellow","Saul","Benchley","Robert","Benenson","Peter","BenGurion","David","Benjamin","Walter","Benn","Tony","Bennington","Chester","Benson","Leana","Bent","Silas","Bentsen","Lloyd","Berger","Ric","Bergman","Ingmar","Berio","Luciano","Berle","Milton","Berlin","Irving","Berne","Eric","Bernhard","Sandra","Berra","Yogi","Berry","Halle","Berry","Wendell","Bethea","Erin","Bevan","Aneurin","Bevel","Ken","Biden","Joseph","Bierce","Am","Brose","Biko","Steve","Billings","Josh","Biondo","Frank","Birrell","Augustine","Black","Elk","Blair","Ro","Bert","Blair","Tony","Blake","William","Blakey","Art","Blalock","Jolene","Blanc","Mel","Blanc","Raymond","Blanchet","Cate","Blix","Hans","Blood","Rebecca"]
	firstName = names[random.randint(0, 99)]
	text_file.write(firstName+"\n")
	print(firstName)

#PRINT AND EXPORT LAST NAME TO TXT
print("")
print("LAST NAME: ")
text_file.write("LAST NAME:" + "\n")
print("")

for i in range(times):
	names = ["Beck","Glenn","Becker","Carl","Beckett","Samuel","Beddoes","Mick","Beecher","HenryWard","Beethoven","Ludwigvan","Begin","Menachem","Bell","Alexander","Graham","Belloc","Hilaire","Bellow","Saul","Benchley","Robert","Benenson","Peter","BenGurion","David","Benjamin","Walter","Benn","Tony","Bennington","Chester","Benson","Leana","Bent","Silas","Bentsen","Lloyd","Berger","Ric","Bergman","Ingmar","Berio","Luciano","Berle","Milton","Berlin","Irving","Berne","Eric","Bernhard","Sandra","Berra","Yogi","Berry","Halle","Berry","Wendell","Bethea","Erin","Bevan","Aneurin","Bevel","Ken","Biden","Joseph","Bierce","Am","Brose","Biko","Steve","Billings","Josh","Biondo","Frank","Birrell","Augustine","Black","Elk","Blair","Ro","Bert","Blair","Tony","Blake","William","Blakey","Art","Blalock","Jolene","Blanc","Mel","Blanc","Raymond","Blanchet","Cate","Blix","Hans","Blood","Rebecca"]
	lastName = names[random.randint(0, 99)]
	text_file.write(lastName+"\n")
	print(lastName)
	


