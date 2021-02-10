#!/usr/bin/env python

"""
Command line argparse for decision_maker
"""

import argparse
from decision_maker import decision

def parse_arguments():
	"""
	Parse command line arguments using argparse
	"""
	# init the argparse class object
	parser = argparse.ArgumentParser()
    
	parser.add_argument(
		"--yesno", 
		action="store_true",
		help="print the random yes/no choice"
	)

	parser.add_argument(
		"--do", 
		action="store_true",
		help="print the random activity to do for the day"
	)

	parser.add_argument(
		"--color", 
		action="store_true",
		help="print the random color choice"
	)

	parser.add_argument(
		"--fortune", 
		action="store_true",
		help="print the random amount of fortune"
	)

	# returns arg dict-like object contianing user arguments
	args = parser.parse_args()

	#error check 
	if sum([args.yesno, args.do, args.color, args.fortune]) > 1:
		raise SystemExit(
			"Only one of 'yesno', 'do', 'color' or 'fortune' at a time.")
	return args

def run_program():
	"runs the command line program"
	# get command line arguments
	args = parse_arguments()

	if args.yesno:
		decision("yesno")
	if args.do:
		decision("do")
	if args.color:
		decision("color")
	if args.fortune:
		decision("fortune")