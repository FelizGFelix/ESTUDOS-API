import requests

url = "http://uol.com.br"

response = requests.get(url)

print(response)

print(response.text)

with open("UOL.html", "w") as arquivo:
    arquivo.write(response.text)

youtube = "http://youtube.com.br"

response2 = requests.get(youtube)

with open("YouTube.html", "w") as arquivo2:
    arquivo2.write(response2.text)