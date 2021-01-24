#File name: Exercise2_10
#Author: Pekka Lehtola
#Description: Clock with alarm function.


#Importing time for local tima, keyboard for setting up alarm and playsound
#To playback alarm sound
import time
import keyboard
from playsound import playsound

class Clock:

    def __init__(self):

        #Hour, minute and seconds set as local time. Alarm turned intialy
        #off with alarm time set to 00:00.
        self.hour = int(time.strftime("%H"))
        self.minute = int(time.strftime("%M"))
        self.second = int(time.strftime("%S"))
        self.alarm_time_hour = 0
        self.alarm_time_minute = 0
        self.alarm_set = False
        self.alarm_sound = False

    #Used for updating clocks time.
    def update_clock(self):

        self.hour = int(time.strftime("%H"))
        self.minute = int(time.strftime("%M"))
        self.second = int(time.strftime("%S"))

    #Takes time input from user and sets it as alarms time.
    #Prints out confirmation that alarm was set to users input.
    #Try used for avoiding crash if ValueError occours
    def setting_alarm(self):

        try:
            self.alarm_time_hour = int(input("Set up alarms hour: "))
            self.alarm_time_minute = int(input("Set up alarms minute: "))
            self.alarm_set = True
            print("Alarm set to: ", str(self.alarm_time_hour) + ":" + str(self.alarm_time_minute))

        except:
            print("Value error", end="\n\n")
            print("Time is: ", str(clock.hour) + ":" + str(clock.minute))

    #Sets alarm back to initial values.
    def turning_alarm_off(self):

        self.__init__()
        print("Alarm turned off at", str(clock.hour) + ":" + str(clock.minute))

clock = Clock()

#Printing out starting time and instruction for setting alarm.
print("To setup alarm press SPACE. Hold down SPACE to end alarm.", end="\n\n")
print("Time is: ", str(clock.hour) + ":" + str(clock.minute))


#Main function
def main():

    while True:

        #Detects if space is pressed. Depending if alarm is on or not
        #sets up alarm status.
        if keyboard.is_pressed("space"):

            if not clock.alarm_set:

                clock.setting_alarm()

            else:
                clock.turning_alarm_off()
                time.sleep(1)

        # If alarm is triggered plays alarm sound and prints out cheerful
        # message.Time.sleep used for avoiding alarm getting annoying.
        if clock.alarm_sound:
            print("Its time to wake up!")
            playsound("alarm.mp3")
            time.sleep(0.4)

        #Checks if its alarm time.
        if int(clock.alarm_time_hour) == (clock.hour):
            if int(clock.alarm_time_minute) == clock.minute:
                clock.alarm_sound = True

        #Checks if local time has changed, if yes updates the clock.
        #Prints out clock every minute.
        if clock.minute != int(time.strftime("%M")):
            clock.update_clock()
            print("Time is: ", str(clock.hour) + ":" + str(clock.minute))

main()
