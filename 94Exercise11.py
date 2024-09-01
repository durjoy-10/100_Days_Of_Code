#Exercise 11-Drink Water Reminder

#Write a python which reminds you of drinking water every hour or two.
#Your program can either beep or send desktop notification for a specific system


'''import time
from plyer import notification

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,  # If you have an icon, specify the path here
        timeout=10  # Notification will disappear after 10 seconds
    )

if __name__ == "__main__":
    while True:
        notify("Drink Water Reminder", "Remember to drink water now!")
        time.sleep(3600)  # Remind every hour (3600 seconds)'''
        
        
import time
import winsound
from plyer import notification

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,  # If you have an icon, specify the path here
        timeout=10  # Notification will disappear after 10 seconds
    )

if __name__ == "__main__":
    while True:
        # Send desktop notification
        notify("Drink Water Reminder", "Remember to drink water now!")
        
        # Beep sound
        winsound.Beep(1500, 1000)  # Beep with frequency 1500 Hz for 1 second  
        
        #winsound.Beep(frequency,time in ms)
        
        # Wait for 1 hour
        time.sleep(3600)  # Remind every hour (3600 seconds)

