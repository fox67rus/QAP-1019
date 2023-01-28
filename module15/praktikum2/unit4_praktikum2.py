# прочитать json файл и сохранить в словарь
#

import json

response_requirements = {
    "timestamp": "int",
    "referer": "string (url)",
    "location": "string (url)",
    "remoteHost": "string",
    "partyId": "string",
    "sessionId": "string",
    "pageViewId": "string",
    "eventType": "string (itemBuyEvent или itemViewEvent)",
    "item_id": "string",
    "item_price": "int",
    "item_url": "string (url)",
    "basket_price": "string",
    "detectedDuplicate": "bool",
    "detectedCorruption": "bool",
    "firstInSession": "bool",
    "userAgentName": "string"
}

with open('response.json', encoding='utf-8') as file:
    response = json.load(file)


print(type(response))
print(response)