import requests

response = requests.get("https://api.github.com/users/srikanthpragada/repos?sort=created&direction=desc")
if response.status_code != 200:
    print("Sorry! Could not get details!")
    exit(1)

repos = response.json()  # converts response (json) to list of dict

for repo in repos:
    lang = repo['language']
    if lang is None:
        lang = "Unknown"
    print(f"{repo['name']:30}  {repo['created_at'][:10]}   {lang:10}")
