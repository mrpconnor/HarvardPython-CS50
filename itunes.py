import requests
import sys

if len(sys.argv) != 2:
    sys.exit

response = requests.get("https://itunes.apple.com/search?term=jack+johnson&limit=50&entity=song")

o = response.json()
for result in o["results"]:
    print(result["trackName"])
    