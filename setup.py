from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(
		name="cptools",
		version="0.0.1",
		author="Biorad",
		author_email="cyz_19930904@163.com",
		description="A series of Chinese processing tools",
		long_description=open("README.rst").read(),
		license="MIT",
		url="https://github.com/desion/tidy_page",
		packages=['cptools'],
		install_requires=[
			"pyahocorasick",
			],
		classifiers=[
			"Environment :: Web Environment",
			"Intended Audience :: Developers",
			"Operating System :: OS Independent",
			"Topic :: Text Processing :: Indexing",
			"Topic :: Utilities",
			"Topic :: Internet",
			"Topic :: Software Development :: Libraries :: Python Modules",
			"Programming Language :: Python",
			"Programming Language :: Python :: 2",
			"Programming Language :: Python :: 2.6",
			"Programming Language :: Python :: 2.7",
			],
		)
