#!/usr/bin/env python3
import os
import csv
import shutil  # for moving files
from sys import platform  # to detect which os the person is using
from getpass import getuser  # to get username of the person running script
from datetime import datetime  # for logs

#import setup
# need to actually make setup file, for now just get base functionality working

# depending on the os, slashes for folders are different, and in the csv file,
# windows locations are in the 2nd column, and linux locations are in the 3rd column
if platform.startswith('linux'):
    slash = '/'
    fldr_idx = 2
elif platform.startswith('win32'):
    slash = '\\'
    fldr_idx = 1
else:
    raise Exception('OS not supported, use Windows or Linux!')


def get_dir():
    """Reads from 'settings.csv' and returns the directory that the user chose to monitor.
    If the directory is invalid, i.e. when the script runs for the first time, the user goes through a setup process

    Args:
        None

    Returns:
        String which represents a directory
    """
    with open('settings.csv') as f:
        # before, the whole file was read. Now, this just gets the 1st row, then trims to get 1st column
        dir = next(csv.reader(f))[1]

    if os.path.isdir(dir):
        pass
    else:
        # first run
        print("Hi! Welcome to Arun's File Sorter.")

        # for some reason, had to make u a variable, otherwise when I tried to concatenate strings,
        # it would say function object at 0x>memory address< instead of the username
        u = getuser()
        while not os.path.isdir(dir):
            while 1:
                use_dwnld_fldr = input(
                    'Would you like to monitor and sort the downloads folder? (y)es/(n)o: ')
                if use_dwnld_fldr.startswith('y'):
                    if platform.startswith('linux'):
                        dir = '/home/{}/Downloads'.format(u)
                        break
                    elif platform.startswith('win32'):
                        dir = 'C:\\Users\\{}\\Downloads'.format(u)
                        break

                elif use_dwnld_fldr.startswith('n'):
                    dir = input(
                        'Enter the path of the folder you wish to monitor\n')
                    if os.path.isdir(dir):
                        break
                    else:
                        print(
                            'Oops! Invalid path entered, or folder does not exist! Start again...')

                else:
                    print('Oops! Invald selection, try again!')

        # update settings. Is costly, because it has to copy entire file to memory, then rewrite every single line
        # again but will stick with this so that it's still user friendly to change the setings for which file types
        # go where. If I was to switch to using some other data structure, then the user probably could not just edit
        # the csv in excel, but would maybe have to edit JSON for example, or install pandas as a depencency, at least
        # I think. Also, it should only have to run once.
        with open('settings.csv') as f:
            data = list(csv.reader(f))
        data[0][1] = dir

        if use_dwnld_fldr.startswith('y'):
            for line in data:
                line[fldr_idx] = line[fldr_idx].replace('your_username', u)

        else:
            if platform.startswith('linux'):
                if not dir.endswith('/'):
                    dir += '/'
                for line in data:
                    line[2] = line[2].replace(
                        '/home/your_username/Downloads/', dir)

            elif platform.startswith('win32'):
                if not dir.endswith('\\'):
                    dir += '\\'
                for line in data:
                    line[1] = line[1].replace(
                        '\\Users\\your_username\\Downloads\\', dir)

        if platform.startswith('linux'):
            with open('settings.csv', 'w') as f:
                csv.writer(f).writerows(data)
        elif platform.startswith('win32'):
            with open('settings.csv', 'w', newline='') as f:
                csv.writer(f).writerows(data)

        print('''\nI have automatically configured some settings for you. Files inside the folder you chose to monitor will be moved to a subfolder for its corresponding file type.\n
                For example: if you chose the Downloads folder, your pictures in the Downloads folder will be moved to Downloads{0}Pictures. If you would like to change where these files get moved to, feel free to edit the settings.csv file with your favourite editor like Excel, and edit the column for Linux or Windows\n'''.format(slash))
        input('Press Enter to continue...')
    return dir


def get_files_in_dir(dir):
    '''Returns a list of files in a directory

    Args:
        dir: the directory

    Returns:
        list of files in the directory

    Examples:
    #In windows
    >>> get_files_in_dir('C:\\Users\The_Virgin_Windows_User\\Downloads')
    ['virus.exe','pr0n.mp4','katyperry.mp3']
    #In linux:
    >>> get_files_in_dir('/home/The_Chad_Linux_User/Downloads')
    ['script.sh','git-cheatsheat.tex','rm -rf script']
    '''

    everything_in_folder = os.listdir(dir)
    files_in_dir = [f for f in everything_in_folder if os.path.isfile(
        ''.join([dir, slash, f]))]
    return files_in_dir


def sort_files(files_in_dir, dir):
    '''Sorts files in a given directory, the heart of this script

    Args:
        dir: the directory
        files_in_dir: the files in the directory

    Returns:
        Nothing, but it moves files, and the data is logged in log.txt
    '''

    #global slash, fldr_idx
    with open('settings.csv') as f:
        # skip the first 2 lines
        next(csv.reader(f))
        next(csv.reader(f))
        # read relevant info from file
        data = list(csv.reader(f))

    # speed improvements:
    # I just read the first lines in the csv file to skip them, instead of
    # copying the entire csv file then popping data I need to eliminate

    # before, I was iterating over every file, then attempting to find a matching
    # extension in the csv file. Now, I iterate over the extensions in the
    # csv file and try to find files that match. That way, if there are
    # multiple files with the same extension, I don't read the list as many
    # times. Additionally, before if there were files with extensions that
    # aren't on the list, the extension would still be compared with the csv file.
    # Also, theoretically, as more files get sorted, there are less files to
    # compare extensions with
    # It is possible that all these 'enhancements' produce no perceptible difference in performance lol

    # Now, I'm considering reading the data from the csvfile as a dictionary
    # to improve performance but I kind of want to keep this naive approach
    f = open('log.txt', 'a')
    now = datetime.now().strftime("%A, %B. %d %Y %I:%M:%S %p")
    f.write('================================================================\n')
    f.write(now + '\n')
    f.write('----------------------------------------------------------------\n\n')
    for line in data:
        for file in files_in_dir:
           # if actual file extension == extension in csv file
            if os.path.splitext(file)[1] == line[0]:
                # if: input file
                # of: output file
                _if = ''.join([dir, slash, file])
                _of = ''.join([line[fldr_idx], slash, file])

                try:
                    f.write('Attempting to move {}\n to\n{}\n'.format(_if, _of))
                    shutil.move(_if, _of)
                    #print('{}\nmoved to\n{}\n'.format(_if,_of))

                except FileNotFoundError:
                    f.write('FileNotFoundError: attempting to fix by creating directory: {}\n'.format(
                        line[fldr_idx]))
                    f.write('Trying again...\n')

                    os.makedirs(line[fldr_idx])
                    shutil.move(_if, _of)

                    f.write('Success\n\n')
                except:
                    f.write(
                        'Error: failed to move {}\n to\n{}\nYour file has not been moved\n\n'.format(_if, _of))

                else:
                    f.write('Success!\n\n')
    f.write('================================================================\n\n')
    f.close()


dir = get_dir()
sort_files(get_files_in_dir(dir), dir)
