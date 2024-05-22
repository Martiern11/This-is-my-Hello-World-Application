#This is my Hello World Application

#import class library
import json

#create the data objects and keys.

data1 = {
    
    'name' : 'john Doe',
    'age' : 30,
    'city' : 'New York, NY',
    'interests' : ['traveling','soccer','running','voleyball','videogames','math'],
    'is_student' : True
    
}


#creating a jason and writing the python object contents in the json.
with open('data1.json','w') as json_file:
    
    json.dump(data1,json_file,indent=4)
    
print("data has been written to data1.json")

#create a json to read the data we created. 
with open('data1.json','r') as json_file:
    
    #create an object called loaded_data load the json file into the argument parameter.
    loaded_data = json.load(json_file)
    
print("sucessfully able to read data.json")
print(loaded_data)

#Altering the json object.
loaded_data['age'] = 34 #<--ints
loaded_data['interests'].append('Secret Hobby')

#Rewerite the cvhanges in the json file.
with open('data1.json','w') as json_file:

 json.dump(data1,json_file,indent=4)
    
print("data has been re-written to data1.json")