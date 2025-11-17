import requests
from datetime import datetime

USERNAME = 'Write your id here'
password = 'write your pass here' 

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    'token': password,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config ={
    'id': 'graph1',
    'name' : 'ApplyGraph',
    'unit': 'minute',
    'type': 'int',
    'color' : 'sora'
}

headers = {'X-USER-TOKEN' : password}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


## Post A Pixel  POST - /v1/users/<username>/graphs/<graphID>
post_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}'

# today = datetime(year=2025, month=11, day=16)
today = datetime.now()
post_pixel_config = {
    'date' : today.strftime('%Y%m%d'), ##'20251117'
    'quantity': input("How mant minutes do you work for apply?")
}
# pixel_response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
# print(pixel_response.text)

## PUT - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
update_pixel = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{post_pixel_config['date']}'

update_config = {
    'quantity': '45'
}
# pixel_response = requests.put(url=update_pixel, json=update_config, headers=headers)
# print(pixel_response.text)


## Delete a pixel /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
# delete_pixel = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{post_pixel_config['date']}'
# pixel_response = requests.delete(url=delete_pixel, headers=headers)
# print(pixel_response.text)
