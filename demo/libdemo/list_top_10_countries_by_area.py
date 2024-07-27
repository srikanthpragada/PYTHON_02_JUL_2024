import requests

response = requests.get("https://restcountries.com/v3.1/all")

countries = response.json()
top_10 = sorted(countries, key=lambda d: d['area'], reverse=True)[:10]
for country in top_10:
    print(f"{country['name']['common']:50}   {country['area']:12} {country['population']:12}")
