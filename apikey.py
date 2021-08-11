import requests

for api_key in range(1,100,2):
    print(f"api_key is {api_key}")
    html = requests.get(f'http://10.10.36.85/api/{api_key}')
    print(html.text)