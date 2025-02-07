from datetime import datetime

without_mcs = datetime.now().replace(microsecond=0)

print(without_mcs)