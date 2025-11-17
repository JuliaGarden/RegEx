import re

s = "time is a road to break up 09:25:16 14:12:01 22:00:00"
res = re.findall(r'\b\d{2}:\d{2}:\d{2}\b', s)
print(res)
