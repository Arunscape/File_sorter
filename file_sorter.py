#!/usr/bin/env python3
import os
import csv
import shutil #for moving files
from sys import platform #to detect which os the person is using
from getpass import getuser #to get username of the person running script

#import setup
#need to actually make setup file, for now just get base functionality working

#def firstrun():

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
        #the csv in excel, but would maybe have to edit JSON for example, or install pandas as a depencency, at least I think
        with open('settings.csv') as f:
            data=list(csv.reader(f))
        data[0][1]=dir
        with open('settings.csv','w') as f:
            csv.writer(f).writerows(data)
    return dir

get_dir()
