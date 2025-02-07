from datetime import datetime, timedelta

current_day = datetime.now()
new_day = current_day - timedelta(days=5)
print("5 days ago:", new_day.strftime("%Y.%m.%d"))