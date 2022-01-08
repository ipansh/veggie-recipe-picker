import requests

url = "https://yummly2.p.rapidapi.com/feeds/search"

querystring = {"start":"0","maxResult":"30","meatyMax":"0.5","maxTotalTimeInSeconds":"3600","meatyMin":"0.4","FAT_KCALMax":"1000"}

headers = {
    'x-rapidapi-host': "yummly2.p.rapidapi.com",
    'x-rapidapi-key': "0e7d662bd7mshf50a60a4f53eb1cp199dd6jsne50b62cf20ac"
    }

response = requests.request("GET", url, headers=headers, params=querystring).json()

for item in response['feed']:
    item['tracking-id']