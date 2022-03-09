import json as j


data = '{"name":"nava", "status":"sytu"}'
myjsondata = j.loads(data)
print(myjsondata["name"])