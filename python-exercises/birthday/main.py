import datetime
import bday_messages

today = datetime.date.today()

next_birthday = datetime.date(2026,10,4)

time_differences = next_birthday - today 
days_away = time_differences
if today == next_birthday:
    print(ch(bday_messages))
else:
    print(f"My next birthday is {time_differences} days away!")
print(time_differences)
