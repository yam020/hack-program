#!/usr/bin/env python

"""
Install decision_maker pacakage. To install locally use:
	`pip install -e .`
"""

from setuptools import setup

setup(
	name = "decision_maker",
	version = "0.0.1",
	entry_points = {
		"console_scripts": ["decision_maker = decision_maker.__main__:run_program"]
	}
)