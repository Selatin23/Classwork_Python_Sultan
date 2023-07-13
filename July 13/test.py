import json

myfile = open("example.txt", encoding="utf-8")
mydata = json.load(myfile)
myfile.close()

print(mydata)

mydata['students'][0] = 'Рамазан'

with open('out_json', 'w') as out_file:
    json.dump(mydata, out_file)

mydata = json.load(file)
mydata = json.loads(string)

json.dump(mydata, file)
json.dumps(data, string)