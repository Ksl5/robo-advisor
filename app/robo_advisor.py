# app/robo_advisor.py
import requests
import json
import datetime
import os
import csv

def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71



# Info inputs
request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"
response = requests.get(request_url)
#print(type(response)) #> <class 'requests.models.Response'>
#print(response.status_code) #> 200
#print(response.text)

parsed_response = json.loads(response.text)
#parsed_response.keys
#parsed_response["Meta Data"]
#parsed_response["Meta Data"].keys
#parsed_response["Meta Data"]["3. Last Refreshed"]

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]
dates = list(tsd.keys())
latest_day = dates[0] #>"2020-06-15"
now = datetime.datetime.now()

high_prices = []
low_prices = []
for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))


selected_symbol = parsed_response["Meta Data"]["2. Symbol"]
latest_close = tsd [latest_day]["4. close"]
recent_high = max(high_prices)
#recent_high = tsd[latest_day]["2. high"]
recent_low = min(low_prices)

#breakpoint()

# info outputs
#csv_file_path = "data/prices.csv" # stock prices filepath
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)

    writer.writeheader() # uses fieldnames set above
           
    writer.writerow({
        "timestamp": "TODO",
        "open":"TODO", 
        "high":"TODO",
        "low":"TODO",
        "close":"TODO",
        "volume":"TODO"
    })
    

print("-------------------------")
print("SELECTED SYMBOL: " + selected_symbol)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA")
print("REQUEST AT: " + now.strftime('%Y-%m-%d %H:%M:%S %p'))
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print("LATEST CLOSE: " + to_usd(float(latest_close)))
print("RECENT HIGH: " + to_usd(float(recent_high)))
print("RECENT LOW: " + to_usd(float(recent_low)))
print("-------------------------")
print("RECOMMENDATION: BUY!") #>TODO
print("RECOMMENDATION REASON: TODO") #>TODO
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")