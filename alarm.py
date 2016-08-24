# Patrick Mogianesi
# Updated /Augest 24 2016/

# This stack  overflow helped http://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list-with-python

#Import libraries
import time
import webbrowser
import random
import os

#Check if the user has the YT.txt file in the same area as alarm.py


#The User can set the time they want to wake up. The String the user puts in must be the same as the example to work.
print "What time do you want to wake up?"
print "Use this form.\nExample: 06:30"
Alarm = raw_input("> ")


#I first need to state the Time variable so it's usable in the while-loop
Time = time.strftime("%H:%M")

if os.path.isfile("YT.txt") == False:
	content = "https://www.youtube.com/watch?v=RUAJ8KLGqis"
#This opens the text file with the youtube links
with open("YT.txt") as f:
	#the urls are stored in the content variable 
	content = f.readlines()


#When the Time does not equal the Alarm time string given above, print the time
while Time != Alarm:
	
	print "The time is " + Time
	
	#Restating the Time variable allows the time to refresh
	#When I tried keeping the variable outside of the loop it just repeated the inital time
	Time = time.strftime("%H:%M")
	
	#This keeps the loop from flooding the command line with updates of the time :P
	time.sleep(1)

#If the Time variable is equal to the Alarm string, this code activates
if Time == Alarm:

	print "Time to Wake up!"
	#from the variable content, a random link is chosen and then that link is stored in random_video variable
	random_video = random.choice(content)
	#Using the webbrowser library, it opens this youtube video link.
	#The videos are varius aphex twin songs
	webbrowser.open(random_video)
