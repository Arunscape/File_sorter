import os
import csv
import shutil
def get_dir():
	
	try:
		with open('directory_to_monitor.txt') as f:
			dir=f.read()
			f.close()

	except:

		while True:
			dir=input('Enter the directory you wish to monitor:\n')
			if os.path.isdir(dir):
				break
			else: 
				print('Path entered was not valid, try again:')
		file=open('directory_to_monitor.txt','w')
		file.write(dir)
		file.close()
	
	return dir

def get_files_in_dir(dir):
	everything_in_folder=os.listdir(dir)
	files_in_dir=[f for f in everything_in_folder if os.path.isfile(dir+'\\'+f)]
	return files_in_dir

def sort_files(files_in_dir,dir):
	with open('windows-settings.csv') as f:
		data=list(csv.reader(f))
		data.pop(0) #get rid of the first line in the list from the csvfile

	for file in files_in_dir:
		file_ext=os.path.splitext(file)[1] #extension of the actual file

		for sublist in data:
			ext=sublist[0] #extension to compare to from csv file
			if ext == file_ext:
				move_to=sublist[1]+'\\'+file
				sourcefile=dir+'\\'+file
				try:
					shutil.move(sourcefile,move_to)
				
				except: #if destination directory doesn't exist, create it
					os.makedirs(sublist[1])
					shutil.move(sourcefile,move_to)

dir=get_dir()
files_in_dir=get_files_in_dir(dir)
sort_files(files_in_dir,dir)

#pseudo code:
#if settings.txt exists, skip the setup

#setup:
# get the directory to monitor
# get list of files in that directory
# make list of file extensions to sort
# write list to file 'settings.txt'
# read from file 
# choose folders into which the files will go to
# move the files


#failed ideas:
"""
class file_extension:
	def __init__(self,ext):
		self.ext = ext
"""
