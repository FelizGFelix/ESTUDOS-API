import requests

url = "https://www.retrogames.cc/arcade-games/marvel-vs-capcom-clash-of-super-heroes-980123-usa.html"

response = requests.get(url)

with open("MVSC.html", "w") as arquivo:
    arquivo.write(response.text)