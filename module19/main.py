import requests

headers = {'accept': 'application/json'}
status = 'available'
url = f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}'

# res = requests.get(url, headers=headers)
#
# print(res.status_code)
# print(res.text)
# print(res.json())
# print(type(res.json()))

resp = requests.get(url, headers=headers, params={'status': 'available'})

print(resp.status_code)

if 'application/json' in resp.headers['Content-Type']:
    print(resp.json())
else:
    print(resp.text)
