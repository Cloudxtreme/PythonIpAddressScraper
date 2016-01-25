# PythonIpAddressScraper

A short Python script that allows for a computer to get the computer's local and global IP address.  

I have a discount internet supplier here in Canada.  Sometimes I need to connect remotely to my home computer.  However, my ISP does not garuntee a static IP.  While it is 'static', it may change for whatever reason and without notice.  In addition, my computer is connected via wifi so sometimes after restarts, my computer takes on a new local IP address.  

In order to combat these two challenges, I have created a windows task scheduler action to execute the script whenever the computer is started.  In addition the script is executed twice a day, once at 12h00 noon and again at 0h00 midnight.  Therefore I should never be more than 12 hours away from an update if need be.  

The script is set up in such a way to allow the current iteration and the last 4 IPs to be saved.  No real reason for this other than I think it's kind of cool to see it when I run it on my laptop.  

## Setup

In addition to the two files you need some kind of remote access to the output file you can access whenever you need to.  I.e. you need a Dropbox account (or similar service).  if you just write to, say, the desktop, you on't be able to access the file when you teed to. N'est–ce pas?

Once you create a folder within your online storage service, you then can download the ip.py and PythonIP.xml and place them in your folder that will be reading and writing these IP addresses.  

If you are running Python 3.5 (x86) then he only thing you need to do is update the working directory in the PythonIP.xml file.  I prefer to do this in an editor, such as Notepad, rather than in Windows Task Scheduler.  Simply find the line 
 
    <WorkingDirectory>C:\##INSERT WORKING DIRECTORY HERE##</WorkingDirectory>

and change the contents to the actual working directory of the file.  E.g C\Users\DropBox\IP\

if you have another edition of pyton installed, then you need to update the following line of the xml as well.

    <Command>"C:\Program Files (x86)\Python 3.5\python.exe"</Command>

for Python 3.3

    <Command>"C:\Python33\python.exe"</Command>

After that, all you need to do is open Windows Task Scheduler.  Open the start menu and type in Task Schedler.  Open it. Once open, go to "Action" > "Import Task..." and navigate to PythonIP.xml.  You can  double check that all the of the settings aer as you want them (Such as adding more time triggeres, or updating once per week, etc.)
