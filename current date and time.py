#import the 'datetime' module to work with date and datetime
import datetime

#get the current date and time 
now = datetime.datetime.now()

#create a datetime object representing the current date and time

#display a message indicating what is being printed
print("Current date and time : ")

#print the current date and time in a specific format
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Use the 'strftime' method to format the datatime object as a string with the desired format 
