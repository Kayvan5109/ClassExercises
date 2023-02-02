import requests 
import json 

API_KEY = "SGCO2WYJFACAICG2 "
url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol=TSLA&apikey=YOUR_API_KEY"
data = requests.get(url)
print(json.dumps(data.json(), indent = 4))