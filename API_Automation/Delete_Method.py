import requests

url = "https://reqres.in/api/users/2"

response = requests.delete(url)
print(response.status_code) # To get the response code

assert response.status_code == 204

# now the user will be deleted and we can check from the data and run the api and check the user
# is available in the data or not