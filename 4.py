from datetime import datetime


day1 = datetime(2030, 12, 2, 2, 3, 4)
day2 = datetime(2025, 6, 5, 16, 35, 51)

diff = abs(day1 - day2)
print(diff.days * 24 * 60 * 60 + diff.seconds)