import discord
import datetime
import os

token = os.environ.get('token')
client = discord.Client()

command_list_dict = {
    "!hello": "Greets the user.",
    "!commands": "displays available commands",
    "!release": "displays time to release",
    "!wowhead search query": "to search classic wowhead",
    "!classic": "for a link to classic guides",
    "!talents": "for a link to talent calculators",
    "!map": "for a high resolution map of classic wow",
    "!classicresources": "for a extensive list of classic resources",
    "!wowmusic": "for a link to wow soundtrack",
    "!reddit": "for a link to classicwow subreddit",
    "!streams": "for a list of wow streams",
    "!duckit search query": "to display search results from DuckDuckGo",
    "!groovy": "for help regarding groovy"
    }
command_list = ["!hello", "!commands - displays available commands", "!release - displays time to release",
                "!wowhead search query - to search classic wowhead", "!classic - for a link to classic guides",
                "!talents - for a link to talent calculators", "!map - for a high resolution map of classic wow",
                "!classicresources - for a extensive list of classic resources",
                "!wowmusic - for a link to wow soundtrack",
                "!reddit - for a link to classicwow subreddit", "!streams - for a list of wow streams",
                "!duckit search query - to display search results from DuckDuckGo",
                "!groovy - for help regarding groovy"]
now = datetime.datetime.now()
release_date = datetime.datetime(2019, 8, 27)
time_to_release = f'{release_date.month - now.month} months and {release_date.day - now.day} days to release'
wow_map_url = "https://i.imgur.com/DlKMA5H.jpg"
classic_resources = "https://barrens.chat/viewtopic.php?t=1091"
wow_soundtrack = "https://youtu.be/gQFOLOur1jM"
wow_streams = "https://www.twitch.tv/directory/game/World%20of%20Warcraft"
reddit_url = "https://www.reddit.com/r/classicwow/"
duckduckgo = "https://duckduckgo.com/?q="
blue_tracker = "https://classic.wowhead.com/bluetracker"


@client.event
async def on_message(message):
    channel_id = client.get_channel(580544385196883978)

    if message.author == client.user:
        return

    if message.content == '!hello':
        author = message.author.mention
        msg = f'Hello {author}, type !commands for available commands.'
        await message.channel.send(msg)
    elif message.content == "!commands2":
        embed = discord.Embed(title="WoWHypeBot's commands", description="Here are all of the WoWHypeBot's commands.")
        for key, val in command_list_dict.items():
            embed.add_field(name=f"{key}", value=f"{val}")
        await message.channel.send(content=None, embed=embed)
    elif message.content.lower() == '!groovy':
        msg = f"-play youtube_link to play a youtube video's audio, -stop to stop playing audio. "\
            f"-help to open groovy help"
        await message.channel.send(msg)
    elif message.content.startswith('!duckit'):
        keywords = message.content.split()
        kw_string = ""
        length = len(keywords)
        for i in range(length)[1:]:
            kw_string += f"{keywords[i]}+"
        url = f'{duckduckgo}{kw_string[:-1]}'
        msg = f'{url}'
        await message.channel.send(msg)
    elif message.content.startswith('!wowhead'):
        keywords = message.content.split()
        kw_string = ""
        length = len(keywords)
        for i in range(length)[1:]:
            kw_string += f"{keywords[i]}+"
        url = f'https://classic.wowhead.com/search?q={kw_string[:-1]}'
        msg = f'{url}'
        await message.channel.send(msg)
    elif message.content.lower() == '!blues':
        msg = f"{blue_tracker}"
        await message.channel.send(msg)
    elif message.content.lower() == '!reddit':
        msg = f"{reddit_url}"
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
    elif message.content.lower() == "!commands":
        list_string = f""
        for command in command_list:
            list_string += f'{command}\n'
        msg = f'List of commands:\n{list_string}'
        await message.channel.send(msg)
    elif message.content.lower() == "!release":
        msg = f'{time_to_release}.'
        await message.channel.send(msg)
    elif message.content.lower() == '!druidguide' and message.author.id == "114689178028998657":
        msg = "https://www.warcrafttavern.com/guides/taladrils-treatise-on-druid-tanking-in-vanilla/"
        await message.channel.send(msg)


@client.event
async def on_ready():
    print("Bot is ready")

client.run(token)
