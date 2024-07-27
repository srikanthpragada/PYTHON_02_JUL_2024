import requests

response = requests.get("https://restcountries.com/v3.1/all")

countries = response.json()
top_10 = sorted(countries, key=lambda d: d['population'], reverse=True)[:10]
for country in top_10:
    print(f"{country['name']['common']:50}   {country['population']:12}")
