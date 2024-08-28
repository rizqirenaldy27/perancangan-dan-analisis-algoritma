from datetime import datetime, timedelta

departure_time = datetime.strptime("08:52:45", "%H:%M:%S")
duration = timedelta(seconds=5000)

arrive_time =  departure_time + duration

print(f"Arrive time : {arrive_time.strftime('%H:%M:%S')}")
