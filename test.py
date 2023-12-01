import requests

query = 'biji-bekatul'
api_url = 'https://parentify-ch2-ps318.as.r.appspot.com/{}'.format(query)
response = requests.get(api_url)
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)