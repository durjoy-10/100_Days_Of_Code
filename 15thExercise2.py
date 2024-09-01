import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
min=int(time.strftime('%M'))
sec=int(time.strftime('%S'))
if(hour>12):
    print("Time:",hour-12,":",min,":",sec)
else:
    print("Time:",hour,":",min,":",sec)

if(hour>=0 and hour<12):
    print("Good Morning Sir!")
elif(hour>=12 and hour<17):
    print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
    print("Good NIght Sir!")
 