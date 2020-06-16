# app/robo_advisor.py
import requests
import json
import datetime
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
latest_day = "2020-06-15"
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
now = datetime.datetime.now()
selected_symbol = parsed_response["Meta Data"]["2. Symbol"]
latest_close = parsed_response["Time Series (Daily)"][latest_day]["4. close"]
recent_high = parsed_response["Time Series (Daily)"][latest_day]["2. high"]
recent_low = parsed_response["Time Series (Daily)"][latest_day]["3. low"]



#breakpoint()



# info outputs


print("-------------------------")
print("SELECTED SYMBOL: " + selected_symbol)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: " + now.strftime('%Y-%m-%d %H:%M:%S %p'))
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print("LATEST CLOSE: " + to_usd(float(latest_close)))
#print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: " + to_usd(float(recent_high)))
#print("RECENT HIGH: $101,000.00")
print("RECENT LOW: " + to_usd(float(recent_low)))
#print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!") #>TODO
print("RECOMMENDATION REASON: TODO") #>TODO
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")