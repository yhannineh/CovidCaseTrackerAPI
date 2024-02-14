import requests
# Import using pip

# Prompt the user to input the necessary parameters
city_name = input("Enter the city name: ")
region_province = input("Enter the state: ")
iso = "USA"
region_name = "US"
q = "US " + region_province
date = input("Enter the date in the format YYYY-MM-DD: ")


# Construct the querystring with user inputs
querystring = {
    "city_name": city_name,
    "region_province": region_province,
    "iso": iso,
    "region_name": region_name,
    "q": q,
    "date": date
}

# Headers 
headers = {
    # ---API KEY NEEDED---
	"X-RapidAPI-Key": "###",
	"X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com"
}

# The URL for the API endpoint
url = "https://covid-19-statistics.p.rapidapi.com/reports"

# Sending the GET request
response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    myJSON = response.json()
    
    # Record the data
    if 'data' in myJSON and len(myJSON['data']) > 0:
        for record in myJSON['data']:
            date = record.get('date', 'N/A')
            confirmed = record.get('confirmed', 'N/A')
            deaths = record.get('deaths', 'N/A')

            print(f"Date: {date}")
            print(f"Confirmed Cases: {confirmed}")
            print(f"Deaths: {deaths}")
            print("-" * 20)  # Separator between records
    else:
        print("No data found.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
