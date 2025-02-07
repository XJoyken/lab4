from datetime import datetime, timedelta

current_day = datetime.now()
yesterday = current_day - timedelta(days=1)
tomorrow = current_day + timedelta(days=1)
print("Yesterday:", yesterday.strftime("%Y.%m.%d"), "\nToday:", current_day.strftime("%Y.%m.%d"), "\nTomorrow:", tomorrow.strftime("%Y.%m.%d"))