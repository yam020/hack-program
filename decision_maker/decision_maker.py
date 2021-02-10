#!/usr/bin/env python

"""
Functions of hello world type code 
Decision maker 
1. Yes or No 
2. What should I do today? 
3. Fortune 
4. What color? 
"""

import random 


def decision(arg):
	"""
	Make the random decision for yes/no, what to do, color, 
	and fortune

    Parameters
    ----------
    String (yesno, do, color, fortune)
	"""
	# convert the argument to the lowercase
	arg_lower= arg.lower()
	# make the random decision based on the input
	if arg_lower == "yesno":
		Yesorno()
	if arg_lower == "do":
		WhatshoudIdo()
	if arg_lower == "color":
		Color()
	if arg_lower == "fortune":
		Fortune()

def Yesorno():
	"""
	Pick yes or no randomly

    Parameters
    ----------
    No parameter needed 

    Print
    ------
    String: Yes/No
	"""
	ynlist = ["Yes", "No"]
	print(random.choice(ynlist))

def WhatshoudIdo():
	"""
	Pick one acitvity randomly

    Parameters
    ----------
    No parameter needed 

    Print
    ------
    String: One activity 
	"""
	todolist = [
		"Coding", "Painting", "Drawing", 
		"Reading", "Going out (6 feet)", "Eating", 
		"Netflixing", "Singing", "Gaming"
	]
	print(random.choice(todolist))

def Color():
	"""
	Pick a color randomly

    Parameters
    ----------
    No parameter needed 

    Print
    ------
    String: One color
	"""
	colorlist = [
		"Red", "Orange", "Yellow", 
		"Chartreuse", "Green", "Cyan", 
		"Azure", "Blue", "Violet",
		"Magenta", "Rose", "Spring Green"
	]
	print(random.choice(colorlist))

def Fortune():
	"""
	Pick a fortune randomly

    Parameters
    ----------
    No parameter needed 

    Print
    ------
    String: One fortune
	"""
	print("$"+str(random.randint(0,10)*100))


if __name__ == "__main__":
    # ask user to input the category of the decision
	arg = input("Make a decions for what ? :")
	# convert to lowercase
	arg_lower= arg.lower()
	# make the random decision based on the input
	if arg_lower == "yesno":
		Yesorno()
	if arg_lower == "do":
		WhatshoudIdo()
	if arg_lower == "color":
		Color()
	if arg_lower == "fortune":
		Fortune()
	


	

