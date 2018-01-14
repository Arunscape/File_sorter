#!/usr/bin/env python3
import os
import csv
import shutil #for moving files

from sys import platform #to detect which os the person is using

print(platform)

def setup():
	print("Hello! Welcome to the setup for my file sorting app! ")

	with open('directories to monitor.txt','w') as f:

		done = False
		while not done:
			dir = input('Enter the path of the folder you wish to monitor')

			if os.path.isdir(dir):
				f.write(dir)

				more = input('Would you like to add another folder to monitor? (y/n)')
				while True:
					if more.lower()=='y':
						break;

					elif more.lower()=='n':
						done=True
						break;

					else:
						more=input("Oops! If you wanted to monitor more folders, type 'y' and hit enter, or if you don't want to monitor more folders, type 'n' and hit enter.")

	f.close()

def get_dirs():
	try:
		with open ('directories to monitor') as f:
			dirs=f.readlines()
			#print(dirs)
			f.close()

	# if the app is run for the first time, or 'directories to monitor' is
	# missing, the setup will run
	except:
		setup()


setup()
