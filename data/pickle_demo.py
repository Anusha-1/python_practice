
"""
Pickling - Serialization and deserialization(unpickling) with binary data format 
- improves performance for data oriented modules,
suitable for DB and socket

byte streams: 0,1 flattening ,marshalling

Data analysis(NLTK) nlp algorithms : for example : 5 mins algorithm took 5 secs

Pickle
PicklingError if python object is nt supported( like text data we cant pickle , or )
unPicklingError if corrupted data

very easy to handle large size of data,secure,fast
drawbacks : languages other than python can not get this and unpickle it
"""
import json
import requests
import pickle

emps={1:'Murthy',2:50000,3:'IT',4:"Hyderabad"}
pkl_on=open('emp.pickle',"wb")
pickle.dump(emps,pkl_on)
pkl_on.close()
print("Binary serialization is done")

print("Now unpickle")
pkl_off=open("emp.pickle","rb")
emps=pickle.load(pkl_off)
print(emps)

#----------------------
response = requests.get(
    "https://jsonplaceholder.typicode.com/todos", verify=False)

todos = json.loads(response.text)

with open('data.pk','wb') as fw:
    pickle.dump(todos, fw)
    print("Done Todos pickling")

with open('data.pk', 'rb') as fr:
    data=pickle.load(fr)
    print(data)
