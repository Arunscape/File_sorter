This is a python based app that I designed to sort my messy downloads folder. 


Firstly, you will need python 3 to run this app. I developed it using python 3.6

To start off, you want to open settings.csv and choose where which file types will be moved to. In windows, here are examples of valid paths:

C:\Users\your_username\Music
\users\your_username\Movies
D:\External_hard_drive\Pictures

In linux (at least in Ubuntu), here are examples of valid paths:
/home/your_username/Music
/home/your_username/Movies
/media/External_hard_drive/Pictures

In the csv file, you can also add additional file names, just remember to add the destination path beside it.
Also in the csv file, if you like what I set to be the default you will want to replace 'your_username' with your username. If you are unsure what your username is in Windows, just press the windows key and R buttons to open the run dialog and then type %username%. You will get an error message, and this error mesage will give your username in single quotation marks.

In linux, you should know what your username is, but if you're unsure, then in Ubuntu, you can press Ctrl+Alt+T and a terminal window will open and it will say your_username@your_computername

If you want a quick way to replace your_username in the .csv file for all of the entries, open excel, and use its built in find and replace function. :) (LibreOffice Calc works too)



When you first run the app, it will ask for a directory to monitor. I like to point it to my downloads folder (\users\my_username\Downloads) because that always gets messy very quickly.If you would like to change the directory later, you can open the file: 'directory_to_monitor.txt' and change the directory, or delete the file, run the app again and it will ask for a new directory to monitor. I may add functionality later to monitor multiple directories but for my needs right now, I can only see this application being useful to sort the downloads folder. 


The code could easily be modified, however, to sort files based on other criteria like file size, or file names. I believe the functionality to sort many folders could be added by writing multiple lines to the 'directory to monitor.txt', then using the following format.

with open('directory_to_monitor.txt') as f:
  for line in f:
    dir=f.readline()
    files_in_dir=get_files_in_dir(dir)
    sort_files(files_in_dir,dir)
 ou
So I would just need to rearrange a bit of code and add that for loop. If I get requests to do so, I will update this project.


Lastly, to get this to work automatically and in the background, you could make a shortcut to the main.py file, and put it in your startup folder. (Windows) The program will run for a few seconds or less then close automatically, and while you are using the computer, the files won't move around when you're not expecting them to.

For linux, there are other ways to run the script at startup
