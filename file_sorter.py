#!/usr/bin/env python3
import os
import csv
import shutil #for moving files
from sys import platform #to detect which os the person is using
from getpass import getuser #to get username of the person running script

#import setup
#need to actually make setup file, for now just get base functionality working

#depending on the os, slashes for folders are different, and in the csv file,
#windows locations are in the 2nd column, and linux locations are in the 3rd column
if platform.startswith('linux'):
    slash='/'
    fldr_idx=2
elif platform.startswith('win32'):
    slash='\\'
    fldr_idx=1
else:
    raise Exception('OS not supported, use Windows or Linux!')

def get_dir():
    with open('settings.csv') as f:
        #before, the whole file was read. Now, this just gets the 1st row, then trims to get 1st column
        dir=next(csv.reader(f))[1]

    if os.path.isdir(dir):
        pass
    else:
        while not os.path.isdir(dir):
            while 1:
                use_dwnld_fldr = input('Would you like to monitor and sort the downloads folder? (y)es/(n)o: ')
                if use_dwnld_fldr.startswith('y'):
                    #for some reason, had to make u a variable, otherwise when I tried to concatenate strings,
                    #it would say function object at 0x>memory address< instead of the username
                    u=getuser()
                    if platform.startswith('linux'):
                        dir='/home/{}/Downloads'.format(u)
                        break
                    elif platform.startswith('win32'):
                        dir='C:\\Users\\{}\\Downloads'.format(u)
                        break
                    else:
                        raise Exception('OS not supported, use Windows or Linux!')

                elif use_dwnld_fldr.startswith('n'):
                    dir=input('Enter the path of the folder you wish to monitor\n')
                    if os.path.isdir(dir):
                        break
                    else:
                        print('Oops! Invalid path entered, start again...')

                else:
                    print('Oops! Invald selection, try again!')

        #update settings. Is costly, because it has to copy entire file to memory, then rewrite every single line
        #again but will stick with this so that it's still user friendly to change the setings for which file types
        #go where. If I was to switch to using some other data structure, then the user probably could not just edit
        #the csv in excel, but would maybe have to edit JSON for example, or install pandas as a depencency, at least
        #I think. Also, it should only have to run once.
        with open('settings.csv') as f:
            data=list(csv.reader(f))
        data[0][1]=dir
        with open('settings.csv','w') as f:
            csv.writer(f).writerows(data)
    return dir

def get_files_in_dir(dir):
    #global slash
    everything_in_folder=os.listdir(dir)
    files_in_dir=[f for f in everything_in_folder if os.path.isfile(''.join([dir,slash,f]))]
    return files_in_dir

def sort_files(files_in_dir,dir):
    #global slash, fldr_idx
    with open('settings.csv') as f:
        #skip the first 2 lines
        next(csv.reader(f))
        next(csv.reader(f))
        #read relevant info from file
        data=list(csv.reader(f))

        for line in data:
            for file in files_in_dir:
               #if actual file extension == extension in csv file
                if os.path.splitext(file)[1] == line[0]:
                    #if: input file
                    #of: output file
                    _if=''.join([dir,slash,file])
                    _of=''.join([line[fldr_idx],slash,file])

                    try:
                        shutil.move(_if,_of)
                        #print('{}\nmoved to\n{}\n'.format(_if,_of))

                    except FileNotFoundError:
                        os.makedirs(line[fldr_idx])
                        shutil.move(_if,_of)

                    except:
                        raise Exception('Something happened, file could not be moved.')

dir=get_dir()
sort_files(get_files_in_dir(dir),dir)
