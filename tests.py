# import requests

# url = f'http://127.0.0.1:8000/users/'

# token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJDbG91ZCIsImV4cCI6MTY4NzUxNTUyM30.X91xZ2hIft4aVFOMUS8g9dtgcVKAQo4c93DECn6il_4'

# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': f'Bearer {token}',
# }

# payload = {
#     'title': 'Hello, FastAPI!',
#     'content': 'auth test' 
# }

# resp = requests.get(url, headers=headers)
# print(resp.json())

# resp = requests.post(url, headers=headers, json=payload)
# print(resp.json())


# payload = {
#     'username': 'Cloud',
#     'password': 'Bingo'
# }

# url = f'http://127.0.0.1:8000/users/'

# resp = requests.get(url)
# print(resp.json())

# resp = requests.post(url, headers=headers, json=payload)
# print(resp.json())

# url = f'http://127.0.0.1:8000/users/Cloud'

# resp = requests.get(url)
# print(resp.json())