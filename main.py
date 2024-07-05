import requests
import random
from fake_useragent import UserAgent

random_email = f"whisper{random.randint(100000,999999)}@gmail.com"
ua = UserAgent().random

user = input('[+] TikTok UserName : ')
link = input('[+] Video Link : ')

payload = {
    "link": link,
    "tiktok_username": user,
    "email": random_email
}

headers = {
    "Host": "api.likesjet.com",
    "Content-Length": "137",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Sec-Ch-Ua-Mobile": "?1",
    "User-Agent": ua,
    "Sec-Ch-Ua-Platform": "\"Android\"",
    "Origin": "https://likesjet.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://likesjet.com/",
    "Accept-Language": "en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5"
}

response = requests.post('https://api.likesjet.com/freeboost/3', json=payload, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code} - {response.reason}")
