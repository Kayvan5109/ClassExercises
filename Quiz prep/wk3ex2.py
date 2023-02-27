import requests
import json
url1 = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&apikey=JIJJ0HI51KVKAHDL'
data1 = requests.get(url1)
print(json.dumps(data1.json(), indent=4))
data1vF = data1.json()

print(data1vF['Time Series (Daily)']['2023-02-06']['5. adjusted close'])

url2 = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=JIJJ0HI51KVKAHDL'
data2 = requests.get(url2)
print(json.dumps(data2.json(), indent = 4))
data2vF = data2.json()

import csv
url3 = 'https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&symbol=IBM&horizon=12month&apikey=JIJJ0HI51KVKAHDL'
with requests.Session() as s:
    data3 = s.get(url3)
    decoded_content = data3.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    print(my_list)

#search for Analyst target price, Price to book ratio, Next report date and EPS estimate
print(data2vF['AnalystTargetPrice'])
print(data2vF['PriceToBookRatio'])
print("Next Report Date: " + my_list[1][2])
print("EPS Estimate: "+ my_list[1][4])