import requests

url = "https://sridurgayadav-chart-lyrics-v1.p.rapidapi.com/apiv1.asmx/SearchLyricDirect"

querystring = {"artist":"michael jackson","song":"bad"}

headers = {
  "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
  "X-RapidAPI-Host": "sridurgayadav-chart-lyrics-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())