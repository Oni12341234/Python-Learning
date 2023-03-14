import requests

pixela_endpoint = "https://pixe.la/v1/users"
username = "oni"
token = "dslfjgh974hjjksfv"
user_params = {

    "token": "dslfjgh974hjjksfv",
    "username": "oni",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# response=requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
# graph_params = {
#     "id":"graph1",
#     "name":"New graph",
#     "unit":"Km",
#     "type":"float",
#     "color":"momiji",



# }
headers = {

    "X-USER-TOKEN": token
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print (response.text)

post_pixel_url = f"{graph_endpoint}/graph1"
# print (post_pixel_url)
params = {
    "date": "20220701",
    "quantity": "7.7"
 }
# response = requests.post(url=post_pixel_url, json=params, headers=headers)
# print(response.text)

put_pixel_url = f"{post_pixel_url}/{params['date']}"
put_params = {
    "quantity":"5.5",
}
response = requests.put(url=put_pixel_url, headers=headers, json=put_params)
print(response.text)