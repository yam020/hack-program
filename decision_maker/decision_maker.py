#!/usr/bin/env python

"""
Functions of hello world type code 
Decision maker 
1. Yes or No 
2. What should I do today? 
3. Fortune 
4. What color? 
5. Quote of the day
"""

import random 
import pandas as pd

# URL path to a CSV of famous quotes 
URL = "https://raw.githubusercontent.com/yam020/hack-program/main/data/quotes.csv"

# Read the csv file
df_quotes = pd.read_csv(URL)

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
		yesorno()
	if arg_lower == "do":
		whatshoudIdo()
	if arg_lower == "color":
		color()
	if arg_lower == "fortune":
		fortune()
	if arg_lower == "quotes":
		quotes()

def yesorno():
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

def whatshoudIdo():
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

def color():
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

def fortune():
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

def quotes():
	"""
	Pick a quote from the dataset randomly

    Parameters
    ----------
    No parameter needed 

    Print
    ------
    String: One quote
	"""
	row = df_quotes.sample()
	say = row.iat[0,1]
	print(say)


if __name__ == "__main__":
    # ask user to input the category of the decision
	arg = input("Make a decions for what ? :")
	# convert to lowercase
	arg_lower= arg.lower()
	# make the random decision based on the input
	if arg_lower == "yesno":
		yesorno()
	if arg_lower == "do":
		whatshoudIdo()
	if arg_lower == "color":
		color()
	if arg_lower == "fortune":
		fortune()
	if arg_lower == "quotes":
		quotes()
	else:
		print("Please enter 'yesno', 'do', 'color', 'fortune', or 'quotes'")
	


	

