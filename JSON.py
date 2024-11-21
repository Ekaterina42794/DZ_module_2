#Источник: https://pythonstart.ru/string/preobrazovanie-stroki-v-json-v-python

# converting string to json
import json
# initialize the json object
i_string = {'C_code': 1, 'C++_code' : 26, 'Java_code' : 17, 'Python_code' : 28}
# printing initial json
i_string = json.dumps(i_string)
print("The declared dictionary is ", i_string)
print("It's type is ", type(i_string))
# converting string to json
res_dictionary = json.loads(i_string)
# printing the final result
print("The resultant dictionary is ", str(res_dictionary))
print("The type of resultant dictionary is", type(res_dictionary))
