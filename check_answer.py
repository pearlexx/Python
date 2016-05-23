# Different solutions of one case


# Method 1
def are_you_sure1():
	while True:
		print("Are you sure? [D-russ/n-russ (Y/n)]: ")
		response = input()
		
		
		if response == "D-russ" or response == "d-russ":
			print("Positive answer: {}".format(response))
			
		elif response == "Y" or response == "y":
			print("Positive answer: {}".format(response))
		
		elif response == "N-russ" or response == "n-russ":
			print("Negative answer: {}".format(response))
			
		elif response == "N" or response == "n":
			print("Negative answer: {}".format(response))
		
		else:
			print("Incorrect input: {}".format(response))
			
are_you_sure1()


# Method 2
def are_you_sure2():
	while True:
		print("Are you sure? [D-russ/n-russ (Y/n)]: ")
		response = input().upper()
		
		if response == "D-russ" or response == "Y":
			print("Positive answer: {}".format(response))
			
		elif response == "N-russ" or response == "N":
			print("Negative answer: {}".format(response))
			
		else:
			print("Incorrect input: {}".format(response))
			
are_you_sure2()


# Method 3
def are_you_sure3():
	while True:
		print("Are you sure? [D-russ/n-russ (Y/n)]: ")
		response = input()
		
		if response in ["D-russ", "d-russ", "Y", "y"]:
			print("Positive answer: {}".format(response))
			
		elif response in ["N-russ", "n-russ", "N", "n"]:
			print("Negative answer: {}".format(response))
		
		else:
			print("Incorrect input: {}".format(response))
			
are_you_sure3()


# Method 4
import re


def are_you_sure4():
	while True:
		print("Are you sure? [D-russ/n-russ (Y/n)]: ")
		response = input()
		
		if re.match("[yYдД]", response):
			print("Positive answer: {}".format(response))
			
		elif re.match("[nNнН]", response):
			print("Negative answer: {}".format(response))
			
		else:
			print("Incorrect input: {}".format(response))
			
are_you_sure4()


# Method 5
def are_you_sure5():
	while True:
		response = input("Are you sure? [Д/д (Y/n)]: ")
		try:
			print(0 <= "YyДдNnНн".index(response) <=3 and "True" or "False")
		except ValueError:
			print("Incorrect input")
			
are_you_sure5()


















