Service Listener gives the files for announce Service Announcer:

We listen announcer's IP address and gives the lists of file that you can download with json



Service Announcer prints the files that you can download:

We announce the User's IP address and gives the list of file which is can download for listeners every 5 second . 

	
Server is keep the files:

In this part program accepted the connection from user and then we print out users information.
Get the files name and change the names to utf-8 in order to ignored not important bytes.
Before the send files we divided 1024 parts of file and send after that we close the connection and socket and
Write the information to log file and we close the file.




Downloader is for download the files:

First of all we create a socket and we want to user's IP 
Enter the files name 
We get the data from sender and we write the data for file which is opened by program 
We close the file and socket 
Opened the file for download log and get the current date
and it close the program 