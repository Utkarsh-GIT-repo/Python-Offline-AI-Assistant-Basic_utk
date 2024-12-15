import datetime

def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
    return current_date, current_time



current_date, current_time =  tell_time()

print(current_date, current_time)