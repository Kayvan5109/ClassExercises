import requests 
import json 

API_KEY = "SGCO2WYJFACAICG2"
url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol=TSLA&apikey=SGCO2WYJFACAICG2"
data = requests.get(url)
print(json.dumps(data.json(), indent = 4))