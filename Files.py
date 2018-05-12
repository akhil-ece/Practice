import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size!=0:
    old_file=open("./ages.json","r+")
    data=json.loads(old_file.read())
    print("currrent age is ", data["age"],"____adding a year")
    data["age"]=data["age"]+1
    print("new  age is",data["age"])
else:
    old_file=open("./ages.json","w+")
    data={"name":"Akhil","age":27}
    print("No file found ",data["age"])
old_file.seek(0)
old_file.write(json.dumps(data))

