# Different solutions of one case


# Method 1
def are_you_sure1():
	while True:
		print("Are you sure? [Д/н (Y/n)]: ")
		response = input()
		
		
		if response == "Д" or response == "д":
			print("Positive answer 1: {}".format(response))
			
		elif response == "Y" or response == "y":
			print("Positive answer 1: {}".format(response))
		
		elif response == "Н" or response == "н":
			print("Negative answer 1: {}".format(response))
			
		elif response == "N" or response == "n":
			print("Negative answer 1: {}".format(response))
		
		else:
			print("Incorrect input 1: {}".format(response))
			
are_you_sure1()


# Method 2
def are_you_sure2():
	while True:
		print("Are you sure? [Д/н (Y/n)]: ")
		response = input().upper()
		
		if response == "Д" or response == "Y":
			print("Positive answer 2: {}".format(response))
			
		elif response == "Н" or response == "N":
			print("Negative answer 2: {}".format(response))
			
		else:
			print("Incorrect input 2: {}".format(response))
			
are_you_sure2()


# Method 3
def are_you_sure3():
	while True:
		print("Are you sure? [D-russ/н (Y/n)]: ")
		response = input()
		
		if response in ["Д", "д", "Y", "y"]:
			print("Positive answer 3: {}".format(response))
			
		elif response in ["Н", "н", "N", "n"]:
			print("Negative answer 3: {}".format(response))
		
		else:
			print("Incorrect input 3: {}".format(response))
			
are_you_sure3()


# Method 4
import re


def are_you_sure4():
	while True:
		print("Are you sure? [Д/н (Y/n)]: ")
		response = input()
		
		if re.match("[yYдД]", response):
			print("Positive answer 4: {}".format(response))
			
		elif re.match("[nNнН]", response):
			print("Negative answer 4: {}".format(response))
			
		else:
			print("Incorrect input 4: {}".format(response))
			
are_you_sure4()


# Method 5
def are_you_sure5():
	while True:
		response = input("Are you sure? [Д/д (Y/n)]: ")
		try:
			print(0 <= "YyДдNnНн".index(response) <=3 and "Positive answer 5" or "Negative answer 5")
		except ValueError:
			print("Incorrect input 5")
			
are_you_sure5()
