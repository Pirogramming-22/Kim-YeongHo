class Time:
    def __init__(self ,hour, minute, second):
        hour = hour
        minute = minute
        second = second
        
    @classmethod
    def is_time_valid(cls ,timeString):
        Time.hour , Time.minute , Time.second = map(int , timeString.split(":"))
        if(Time.hour < 0 or Time.hour > 24):
            return 0
        elif(Time.minute <0 or Time.minute > 60):
            return 0
        elif(Time.second <0 or Time.second > 60):
            return 0
        else:
            return 1
        
    @classmethod
    def from_string(cls, timeString):
        Time.hour , Time.minute , Time.second = map(int , timeString.split(":"))
        return cls(cls.hour,Time.minute,Time.second)
        


 
time_string = input()
 
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')