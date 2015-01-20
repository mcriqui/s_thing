import time
import os
import datetime
from datetime import datetime, timedelta
#from non import nonBlockingRawInput

name = raw_input("Enter your name.")

print("Hello, " + name)

alarm_HH = raw_input("Enter the hour you want to wake up at")
alarm_MM = raw_input("Enter the minute you want to wake up at")

alarm_time = "{0}:{1}".format(alarm_HH, alarm_MM)

time_obj = datetime.strptime(alarm_time, '%I:%M')

change_in_time = timedelta(minutes=20)

new_time = time_obj - change_in_time


print "You want to wake up at {0}".format(new_time.time())

while True:
    now = time.localtime()
    # print now
    if now.tm_hour == int(new_time.hour) and now.tm_min == int(new_time.minute):
        print("ALARM NOW!")
        os.popen("samplesong.mp3")
        break

    # else:
    #     print("no alarm")
    timeout = 60 - now.tm_sec
