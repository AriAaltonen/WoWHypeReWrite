import discord
import os
import requests
import xmltodict
import json
from datetime import datetime
from dateutil import relativedelta

token = os.environ.get('token')
client = discord.Client()

command_list_dict = {
    "!hello": "Greets the user.",
    "!commands": "Embeds this view to channel",
    "!release": "Posts the time to classic release",
    "!wowhead keywords": "Searches WoWHead for given keywords",
    "!classic": "Posts a link to classic guides",
    "!talents": "Posts a link to classic talent calculators",
    "!map": "Posts a link to a high resolution map of classic wow",
    "!classicresources": "Posts a link to an extensive list of classic resources",
    "!wowmusic": "Posts a link to the wow soundtrack",
    "!reddit": "Posts a link to the classicwow subreddit",
    "!streams": "Posts a link to the list of wow streams on twitch",
    "!duckit keywords": "Searches DuckDuckGo for given keywords",
    "!groovy": "Posts a help message regarding groovy",
    "!stats": "Posts a message stating item's required level and iLevel",
    "!youtube keywords": "Searches youtube for given keywords",
    "!rwowhead keywords": "Searches retail WoWHead for given keywords",
    "!dungeons": "Posts a link to a world map with dungeons marked"
    }

release_date = datetime(2019, 8, 27)
classic_resources = "https://barrens.chat/viewtopic.php?t=1091"
wow_soundtrack = "https://youtu.be/gQFOLOur1jM"
wow_streams = "https://www.twitch.tv/directory/game/World%20of%20Warcraft"
blue_tracker = "https://classic.wowhead.com/bluetracker"
reddit_url = "https://www.reddit.com/r/classicwow/"
duckduckgo_url = "https://duckduckgo.com/?q="
cwowhead_url = "https://classic.wowhead.com/search?q="
wow_map_url = "https://i.imgur.com/DlKMA5H.jpg"
rwowhead_url = "https://www.wowhead.com/search?q="
dungeons_url = "https://i.imgur.com/8BtEi2I.jpg"


@client.event
async def on_message(message):
    channel_id = client.get_channel(580544385196883978)

    if message.author == client.user:
        return

    if message.content == '!hello':
        author = message.author.mention
        msg = f'Hello {author}, type !commands for available commands.'

        await message.channel.send(msg)

    elif message.content.startswith("!stats"):
        keywords = message.content.split()
        kw_string = ""
        length = len(keywords)

        for i in range(length)[1:]:
            kw_string += f"{keywords[i]}+"
        
        url = f'https://classic.wowhead.com/item={kw_string[:-1]}&xml'
        r = requests.get(url)
        response_dict = xmltodict.parse(r.content)
        
        if not response_dict.get("wowhead").get("error"):
            jsone = response_dict['wowhead']['item']['json']
            item_json = f'{{{jsone}}}'
            jsondicte = json.loads(item_json)
            name = f'{jsondicte["name"]}'
            response_str = f"Required level to use {name[1:]} is {jsondicte['reqlevel']}, iLevel is {jsondicte['level']}."
            msg = f'{response_str}'
        else:
            msg = "Item not found"
    
        await message.channel.send(msg)

    elif message.content == "!commands":
        embed = discord.Embed(title="WoWHypeBot's commands", description="Here are all of the WoWHypeBot's commands.")
        for key, val in command_list_dict.items():
            embed.add_field(name=f"{key}", value=f"{val}")

        await message.channel.send(content=None, embed=embed)

    elif message.content.lower() == '!groovy':
        msg = f"-play youtube_link to play a youtube video's audio.\n" \
            f"-stop to stop playing audio.\n"\
            f"-help to get further help from Groovy.\n"

        await message.channel.send(msg)

    elif message.content.startswith('!duckit'):
        keywords = message.content.split()
        kw_string = ""
        length = len(keywords)

        for i in range(length)[1:]:
            kw_string += f"{keywords[i]}+"
        
        url = f'{duckduckgo_url}{kw_string[:-1]}'
        msg = f'{url}'

        await message.channel.send(msg)

    elif message.content.startswith('!youtube'):
        keywords = message.content.split()
        kw_string = ""
        length = len(keywords)
        
        for i in range(length)[1:]:
            kw_string += f"{keywords[i]}+"
        
        url = f'"https://www.youtube.com/results?search_query="{kw_string[:-1]}'
        msg = f'{url}'

        await message.channel.send(msg)

    elif message.content.startswith('!rwowhead'):
        keywords = message.content.split()
        kw_string = ""
        length = len(keywords)

        for i in range(length)[1:]:
            kw_string += f"{keywords[i]}+"

        url = f'{rwowhead_url}{kw_string[:-1]}'
        msg = f'{url}'

        await message.channel.send(msg)

    elif message.content.startswith('!wowhead'):
        keywords = message.content.split()
        kw_string = ""
        length = len(keywords)
        
        for i in range(length)[1:]:
            kw_string += f"{keywords[i]}+"
        
        url = f'{cwowhead_url}{kw_string[:-1]}'
        msg = f'{url}'

        await message.channel.send(msg)

    elif message.content.lower() == '!blues':
        msg = f"{blue_tracker}"
        await message.channel.send(msg)

    elif message.content.lower() == '!reddit':
        msg = f"{reddit_url}"
        await message.channel.send(msg)

    elif message.content.lower() == '!dungeons':
        msg = f"{dungeons_url}"
        await message.channel.send(msg)

    elif message.content.lower() == '!streams':
        msg = f"{wow_streams}"
        await message.channel.send(msg)

    elif message.content.lower() == '!wowmusic':
        msg = f"{wow_soundtrack}"
        await message.channel.send(msg)

    elif message.content.lower() == '!map':
        msg = f"{wow_map_url}"
        await message.channel.send(msg)

    elif message.content.lower() == '!classicresources':
        msg = f"{classic_resources}"
        await message.channel.send(msg)

    elif message.content.lower() == '!classic':
        msg = "https://classic.wowhead.com/guides/classic-wow-classes-and-talent-overview"
        await message.channel.send(msg)

    elif message.content.lower() == '!talents':
        msg = "https://classic.wowhead.com/talent-calc"
        await message.channel.send(msg)
    elif message.content.lower() == "!release":
        now = datetime.now().date()
        r = relativedelta.relativedelta(release_date, now)
        msg = f'{r.days} days to release.'
        await message.channel.send(msg)
    elif message.content.lower() == '!druidguide':
        msg = f"https://www.warcrafttavern.com/guides/taladrils-treatise-on-druid-tanking-in-vanilla/"
        await message.channel.send(msg)


@client.event
async def on_ready():
    print("Bot is ready")

client.run(token)
