# Get Request API Get response and Display response
import jsonpath
import requests
import json
url = "https://reqres.in/api/users?page=2"

response = requests.get(url) # It is used to store the response code of the url
print(response)
    #Used to just fetch data and check the response of the aPi
    # print(response)
    #
    # # To print the Body of the API we use
    # Api_Body = response.content
    # print(Api_Body)
    #
    # # To print the headers of the API
    # print(response.headers)

# Methods to check and validate the data we get from the API
# Parse content to json format

json_response = json.loads(response.text)
print(json_response) #To convert the contant in json format to use json path and get the value

data = jsonpath.jsonpath(json_response, "data[0].id") # Total pages is a field in the content and we pick the total pages and print the value of that
print(data)
 # The values return in list format so we use the indexing to get the values
# assert pages[0] == 2
# How we can write the complex json and how we can get the values of same key from the json file

