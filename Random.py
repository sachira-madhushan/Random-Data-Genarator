import string
import random
f=open("output.txt","a")
def gen(s):
	letters = string.ascii_lowercase
	for x in range(s):
		
		text=''.join(random.choice(letters) for i in range(10))
		f.write(str(x+1)+" "+text+" "+str(random.randint(20,100))+" "+str(random.randint(20,100))+" "+str(random.randint(20,100))+"\n")
		
	
	print("Successfully Genarated "+str(s)+" Data !")
	f.close()



def intro():

	print("------ Random Data Genarator ------")
	print("  Developed By Sachira Madhushan")
	print("-----------------------------------")
	print(" ")
	x=int(input("[?] Enter Number Of Data :"))
	gen(x)


intro()