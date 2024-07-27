import requests

response = requests.get("https://api.github.com/users/gvanrossum")
if response.status_code != 200:
    print("Sorry! Could not get details!")
    exit(1)

details = response.json()  # converts response (json) to dict

print(f"Name       : {details['name']}")
print(f"Location   : {details['location']}")
print(f"Company    : {details['company']}")
print(f"Created On : {details['created_at']}")
