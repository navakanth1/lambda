import json as j

data = {"name":"nava","status":"stude"}
jsondata = j.dumps(data)
myjsondata = j.loads(jsondata)
print(myjsondata["name"])
