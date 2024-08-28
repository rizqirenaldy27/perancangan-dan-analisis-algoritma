from datetime import datetime

departure_time = datetime.strptime("08:52:45", "%H:%M:%S")
arrive_time = datetime.strptime("12:15:10", "%H:%M:%S")

trip_duration = arrive_time - departure_time

hour = trip_duration.seconds // 3600
minute = (trip_duration.seconds % 3600) // 60
second = trip_duration.seconds % 60

print(f"Waktu yang dihabiskan dalam perjalanan: {hour} jam, {minute} menit, {second} detik.")
