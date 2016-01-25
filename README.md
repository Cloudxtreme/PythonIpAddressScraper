# PythonIpAddressScraper
A short Python script that allows for a computer to get the computer's local and global IP address.  

I have a discount internet supplier here in Canada.  Sometimes I need to connect remotely to my home computer.  However, my ISP does not garuntee a static IP.  While it is 'static', it may change for whatever reason and without notice.  In addition, my computer is connected via wifi so sometimes after restarts, my computer takes on a new local IP address.  

In order to combat these two challenges, I have created a windows task scheduler action to execute the script whenever the computer is started.  In addition the script is executed twice a day, once at 12h00 noon and again at 0h00 midnight.  Therefore I should never be more than 12 hours away from an update if need be.  

The script is set up in such a way to allow the current iteration and the last 4 IPs to be saved.  No real reason for this other than I think it's kind of cool to see it when I run it on my laptop.  
