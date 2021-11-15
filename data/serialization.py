import requests,json

response= requests.get("https://jsonplaceholder.typicode.com/todos",verify=False)
todos=json.loads(response.text)
print(todos)




#serialization : Conceptof getting state from websiteor file system and storing themin socket/db for further processing
# 1. memory level in JSON(process it and dump it in other files), #converting dict to json and write in memory, indent is same as nested levels
# 2. file level(csv/json) , parse_csv is a csv level serialization  
# 3. database(mysql/ ..) , 
# 4.sockets

#memory level
data =json.dumps(todos,indent=2)
print (data) 

#file level serialization
with open('datafile.json','w') as writefile: #this is json file serialization
    json.dump(data,writefile)  # it is for writing into file whereas dumps is memory level serialization
    print('json serialization is done')

with open('datafile.json','r') as readfile:
    data=json.load(readfile)
    print("After deserialization", data)

