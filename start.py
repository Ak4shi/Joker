# Discord Card Wars Bot
import sys
import os
import discord
from discord.ext import commands
import requests
import csv
import datetime
import json
import aiohttp
import urllib.parse
import funcs
import asyncio
from PIL import Image
import random
from discord_components import DiscordComponents
from paginate import paginate
import get
from discord.ext.tasks import loop
#from server import keep_alive
#from pretty_help import DefaultMenu, PrettyHelp
execk = 0

@loop(hours=1)
async def git_pull():
		os.system("git pull")
		if execk != 0:
			os.execv(sys.executable, ['python'] + sys.argv)
		execk += 1
devs = []


def log_write(text):
    with open("log.log","a") as log:
        all = "[{}] : \t{}\n".format(str(datetime.datetime.now()),text)
        print(text)
        log.write(all)

log_write("Starting BOT!!!")
#
bot = commands.AutoShardedBot(command_prefix='jk!')
#bot.remove_command('help')
#menu = DefaultMenu(page_left="⬅️", page_right="➡️", remove="❌", active_time=10)
#bot.help_command=PrettyHelp(menu=menu)
@bot.event
async def on_ready():
    DiscordComponents(bot)
    """
    pfp_path = "pfp/download_1.jpeg"

    fp = open(pfp_path, 'rb')
    pfp = fp.read()
    await bot.user.edit(avatar=pfp)
    """
    await bot.change_presence(activity=discord.Game(name='Card Wars'))
    log_write('We have logged in as {0.user}'.format(bot))

@bot.command()
async def servers(ctx):
    if ctx.author.id in devs:
        embed = discord.Embed(title="servers",description="servers of the bot")
        for guild in bot.guilds:
            embed.add_field(name=f"{guild.name}",value=f"{guild.id}")
        await ctx.author.send(embed=embed)


@bot.command()
async def invite(ctx):
    embed = discord.Embed(title="Invite",description="[Invite](https://discord.com/oauth2/authorize?&client_id=858548922771701770&scope=applications.commands+bot&permissions=2088234230)",color=ctx.author.color)
    await ctx.send(embed=embed)

@bot.command(aliases=["mview"])
async def mythicview(ctx, *, arg):
    with open('./cards.csv') as cfile:
        csv_file = csv.reader(cfile, delimiter=',',quotechar='"')
        # Find card and return value
        log_write("{1} \t$c {0}".format(arg,ctx.message.author))
        search=[]
        s2=[]
        for row in csv_file:
            if arg.lower() in row[0].lower():
                search.append(row[0])
                returned_card=row
            if arg == row[0]:
                s2.append(row[0])
                returned_card=row
        if len(search) != 1:
            if len(s2)==1:
                search = s2
            if len(search) > 1:
                embed = discord.Embed(color=0xfff100)
                embed.set_author(name="Did you mean:")
                x=1
                for ting in search:
                    embed.add_field(name=str(x)+".", value=ting, inline=False)
                    x+=1
                try:
                    embed.add_field(name="Disclaimer", value="Try typing it with proper capitalization.", inline=False)
                    await ctx.send(embed=embed)
                    log_write("".join(search))
                    log_write("")
                except:
                    await ctx.send("That search exceeds the limit ({} cards were returned). Please be more specific.".format(str(len(search))))
                    log_write("Call for {} cards.".format(str(len(search))))


        if len(search) == 1:
            print(returned_card)
            embed = discord.Embed(color=0xfff100)
            cardname = returned_card[0]
            insert = ""
            cardurlname = cardname.split()
            for item in cardurlname:
                insert += item
            urlz=f"https://github.com/641i130/card-wars-discord-bot/raw/master/images/{insert}.jpg"
            print(urlz)
            embed.set_image(url=f"attachment://{returned_card[0]}.jpg")

            embed.set_author(name=returned_card[0], icon_url="https://cdn.discordapp.com/avatars/705581980628025415/0a89eae2186c741e269d72b10c407b47.webp")
            embed.add_field(name="Deck / Quantity", value=returned_card[8].rstrip(), inline=False)
            embed.set_thumbnail(url="http://35.184.199.95/images/{}.jpg".format(urllib.parse.quote(returned_card[0])))

            if (returned_card[2].rstrip() == "Creature"):
                embed.add_field(name="Landscape", value=returned_card[3].rstrip(), inline=True)
                embed.add_field(name="Type", value=returned_card[2].rstrip(), inline=True)
                embed.add_field(name="Cost", value=returned_card[4].rstrip(), inline=True)
                embed.add_field(name="ATK", value=returned_card[5].rstrip(), inline=True)
                embed.add_field(name="DEF", value=returned_card[6].rstrip(), inline=True)
                embed.add_field(name="Description", value=returned_card[1].rstrip(), inline=True)

            if (returned_card[2].rstrip() == "Spell" or returned_card[2].rstrip() == "Building" or returned_card[2].rstrip() == "Teamwork"):
                embed.add_field(name="Landscape", value=returned_card[3].rstrip(), inline=True)
                embed.add_field(name="Type", value=returned_card[2].rstrip(), inline=True)
                embed.add_field(name="Cost", value=returned_card[4].rstrip(), inline=True)
                embed.add_field(name="Description", value=returned_card[1].rstrip(), inline=True)

            if (returned_card[2].rstrip() == "Hero"):
                embed.add_field(name="Type", value=returned_card[2].rstrip(), inline=True)
                embed.add_field(name="Description", value=returned_card[1].rstrip(), inline=True)
                #embed.add_field(name="Card Set", value=returned_card[9].rstrip(), inline=True)

            await ctx.send(embed=embed)

            log_write("".join(search))
            log_write("")

@bot.command(aliases=["mimage"])
async def mythicimage(ctx, *, arg):
    if ctx.author.id == 746904488396324864:
        return await ctx.send("Ee")
    with open('./cards.csv') as cfile:
        csv_file = csv.reader(cfile, delimiter=',',quotechar='"')
        # Find card and return value
        log_write("{1} \t$c {0}".format(arg,ctx.message.author))
        search=[]
        s2=[]
        for row in csv_file:
            if arg.lower() in row[0].lower():
                search.append(row[0])
                returned_card=row
            if arg == row[0]:
                s2.append(row[0])
                returned_card=row
        if len(search) != 1:
            if len(s2)==1:
                search = s2
            if len(search) > 1:
                embed = discord.Embed(color=0xfff100)
                embed.set_author(name="Did you mean:")
                x=1
                for ting in search:
                    embed.add_field(name=str(x)+".", value=ting, inline=False)
                    x+=1
                try:
                    embed.add_field(name="Disclaimer", value="Try typing it with proper capitalization.", inline=False)
                    await ctx.send(embed=embed)
                    log_write("".join(search))
                    log_write("")
                except:
                    await ctx.send("That search exceeds the limit ({} cards were returned). Please be more specific.".format(str(len(search))))
                    log_write("Call for {} cards.".format(str(len(search))))
        if len(search) == 1:
            await ctx.send(file=discord.File("images/{}.jpg".format(returned_card[0])))

            log_write("".join(search))
            log_write("")

@bot.command(aliases=["aview"])
async def animeview(ctx,*,query=None):

    try:

        if query == None:
            return await ctx.send("please enter a card name.")
        loadring = await ctx.send("loading...")
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'From': 'cool5tarxv@gmail.com'  # This is another valid field
        }
        query = query.replace(" ","+")
        print(query)
        response = requests.request("POST",f'https://www.animecharactersdatabase.com/api_series_characters.php?character_q={query}',headers=headers)
        print(response.text)
        anime = response.json()
        pages = []
        embed = discord.Embed(title="Welcome to the Anime Pack",description="For a targetted user please use their id or enjoy all results for that name",color=ctx.author.color)
        pages.append(embed)
        for item in anime["search_results"]:
            name = item["name"]
            e = name.replace(" ","-")
            amtx = 1
            image = "."
            e = e.lower()
            print(e)
            ex = "."
            while ex.startswith("""<?xml version="1.0" encoding="UTF-8"?>""") == False:
                if ex.startswith("""<?xml version="1.0" encoding="UTF-8"?>""") == False:
                    image = requests.request("GET",f"https://d2l56h9h5tj8ue.cloudfront.net/images/cards/{e}-{amtx}.jpg")
                    ex = image.text
                    if ex.startswith("""<?xml version="1.0" encoding="UTF-8"?>""") == False:
                        amtx += 1
            if ex.startswith("""<?xml version="1.0" encoding="UTF-8"?>""") == True and amtx == 1:
                image = item["character_image"]

            else:
                image = f"https://d2l56h9h5tj8ue.cloudfront.net/images/cards/{e}-2.jpg"
            print(image)
            id = item["id"]
            gender = item["gender"]
            desc = item["desc"]
            collection = item["anime_name"]
            card = item["id"]
            cost = "not found."
            if int(card) < 10:
                cost = int(card)*1000
            elif int(card) < 100:
                cost = int(card)*1000
            elif int(card) < 1000:
                cost = int(card)*100
            elif int(card) < 10000:
                cost = int(card)*10
            elif int(card) < 100000:
                cost = int(card)
            else:
                cost = int(card)
            classer = get.getclass(int(id))
            att = get.getattack(int(id))
            hp = get.gethp(int(id))
            embed = discord.Embed(title=f"{name}",description=f"**Id:** `{id}`\n**Gender:** {gender}\n**Editions:** {amtx}\n**collection:** {collection}\n**description:** *{desc}*\n**Cost:** `{cost}`\n**Class:** {classer}\n**Attack:** `{att}`\n**Health:** `{hp}`",color=ctx.author.color)
            embed.set_image(url=image)
            pages.append(embed)
        await paginate(bot,ctx,pages,loadring)
    except IndexError:
        return await loadring.edit(content="Not Found.")
@bot.command(aliases=["acview"])
async def animecollectionview(ctx,*,query=None):

    with open("data/collections.json","r") as k:
        cel = json.load(k)
    try:

        if query == None:
            return await ctx.send("please enter a collection name.")
        loadring = await ctx.send("loading...")
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'From': 'cool5tarxv@gmail.com'  # This is another valid field
        }
        query = query.replace(" ","+")
        print(query)
        response = requests.request("POST",f'https://www.animecharactersdatabase.com/api_series_characters.php?anime_q={query}',headers=headers)
        print(response.text)
        anime = response.json()
        pages = []
        embed = discord.Embed(title="Welcome to the Anime Pack",description="For a targetted collection please use their id or enjoy all results for that name",color=ctx.author.color)
        pages.append(embed)
        for item in anime["search_results"]:
            char = requests.request("POST",f"""{item["characters_url"]}""",headers=headers)
            char = char.json()
            image = item["anime_image"]
            name = item["anime_name"]
            id = item["anime_id"]
            embed = discord.Embed(title=f"{name}'s card",description=f"**Id:** `{id}`\n**name:** {name}",color=ctx.author.color)

            embed.set_image(url=image)
            for namez in char["characters"]:
                card = namez["id"]
                cost = "not found."
                if int(card) < 10:
                    cost = int(card)*1000
                elif int(card) < 100:
                    cost = int(card)*1000
                elif int(card) < 1000:
                    cost = int(card)*100
                elif int(card) < 10000:
                    cost = int(card)*10
                elif int(card) < 100000:
                    cost = int(card)
                else:
                    cost = int(card)
                embed.add_field(name=f"""{namez["name"]}""",value=f"""id: `{namez["id"]}`\ncost: `{cost}`""")

            pages.append(embed)
        await paginate(bot,ctx,pages,loadring)
    except IndexError:
        return await loadring.edit(content="Not Found.")
#@bot.command()
@bot.command(aliases=["aimage"])
async def animeimage(ctx,*,query=None):
    if query == None:
        return await ctx.send("please enter a card name.")
    loadring = await ctx.send("loading...")
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'From': 'cool5tarxv@gmail.com'  # This is another valid field
    }
    query = query.replace(" ","+")
    print(query)
    response = requests.request("POST",f'https://www.animecharactersdatabase.com/api_series_characters.php?character_q={query}',headers=headers)
    print(response.text)
    anime = response.json()
    image = anime["search_results"][0]["character_image"]
    await loadring.edit(content=str(image))

@bot.command(aliases=["ainv"])
async def animeinventory(ctx,user:discord.Member=None):
    ids = []
    amt = 0
    loadring = await ctx.send("loading...")
    pages = []
    if user == None:
        user = ctx.author

    with open("data/bank.json","r") as f:
        bank = json.load(f)
    for val in bank[str(user.id)]["cards"]:
        for item in bank[str(user.id)]["cards"][val]:
        #print(bank[str(user.id)]["cards"][item][0])
            print(item)
            print( bank[str(user.id)]["cards"][val][0])
            name = item
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
            'From': 'cool5tarxv@gmail.com'  # This is another valid field
            }
            if item == bank[str(user.id)]["cards"][val][0]:
                namez = name.replace(" ","+")
                anime = requests.request("POST",f'https://www.animecharactersdatabase.com/api_series_characters.php?anime_q={namez}',headers=headers)
                anime = anime.json()
                anime_id = anime["search_results"][0]["anime_id"]
                embed = discord.Embed(title=f"{name} collection",description=f"{name}",color=ctx.author.color)
                characters = discord.Embed(title=f"{name} characters",description=f"The characters for {name}:",color=ctx.author.color)
                for valuex in bank[str(user.id)]["cards"][val]:
                    #print(valuex)
                    if valuex != bank[str(user.id)]["cards"][val][0]:
                        char_name = ""
                        lzt = valuex.split()
                        end = len(lzt)
                        #print(end-1)
                        for valuem in lzt:
                            if valuem != lzt[end-1]:
                                char_name += " " + valuem
                        #print(lzt)
                        characters.add_field(name=f"{char_name}",value=f"id: `{lzt[end-1]}`")
                embed.set_image(url=anime["search_results"][0]["anime_image"])
                if anime_id not in ids:
                    amt += 1
                    await loadring.edit(f"loading... **{amt}**")
                    ids.append(anime_id)
                    pages.append(embed)
                    pages.append(characters)

            for value in bank[str(user.id)]["cards"][val]:
                if item != bank[str(user.id)]["cards"][val][0]:
                    lzt = item.split()
                    end = len(lzt)
                    id = lzt[end-1]
                    itemz = requests.request("POST",f'https://www.animecharactersdatabase.com/api_series_characters.php?character_id={id}',headers=headers)
                    print(itemz.text)
                    itemz = itemz.json()
                    name = itemz["name"]
                    e = name.replace(" ","-")
                    amtx = 1
                    image = "."
                    e = e.lower()
                    print(e)
                    ex = "."
                    while ex.startswith("""<?xml version="1.0" encoding="UTF-8"?>""") == False:
                        if ex.startswith("""<?xml version="1.0" encoding="UTF-8"?>""") == False:
                            image = requests.request("GET",f"https://d2l56h9h5tj8ue.cloudfront.net/images/cards/{e}-{amtx}.jpg")
                            ex = image.text
                            if ex.startswith("""<?xml version="1.0" encoding="UTF-8"?>""") == False and amt == 1:
                                amtx += 1
                    if amtx != 1:
                        image = f"https://d2l56h9h5tj8ue.cloudfront.net/images/cards/{e}-2.jpg"
                    else:
                        image = itemz["character_image"]
                    print(image)
                    id = itemz["id"]
                    gender = itemz["gender"]
                    desc = itemz["desc"]
                    collection = itemz["origin"]
                    card = itemz["id"]
                    cost = "not found."
                    if int(card) < 10:
                        cost = int(card)*1000
                    elif int(card) < 100:
                        cost = int(card)*1000
                    elif int(card) < 1000:
                        cost = int(card)*100
                    elif int(card) < 10000:
                        cost = int(card)*10
                    elif int(card) < 100000:
                        cost = int(card)
                    else:
                        cost = int(card)
                    classer = get.getclass(int(id))
                    att = get.getattack(int(id))
                    hp = get.gethp(int(id))
                    embed = discord.Embed(title=f"{name}",description=f"**Id:** `{id}`\n**Gender:** {gender}\n**Editions:** {amtx}\n**collection:** {collection}\n**description:** *{desc}*\n**Cost:** `{cost}`\n**Class:** {classer}\n**Attack:** `{att}`\n**Health:** `{hp}`",color=ctx.author.color)
                    embed.set_image(url=image)

                    if id not in ids:
                        amt += 1
                        await loadring.edit(f"loading... **{amt}**")
                        pages.append(embed)
                        ids.append(id)
    #print(pages)
    await loadring.edit(f"{ctx.author.mention} loaded!")
    await paginate(bot,ctx,pages,loadring)



@bot.command()
async def buy(ctx,card):
    if card == None:
        return await ctx.send("please enter a card name/id.")
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'From': 'cool5tarxv@gmail.com'  # This is another valid field
    }
    card = card.replace(" ","+")
    response = requests.request("POST",f'https://www.animecharactersdatabase.com/api_series_characters.php?character_id={card}',headers=headers)
    print(response.text)
    anime = response.json()
    if int(card) < 10:
        cost = int(card)*1000
    elif int(card) < 100:
        cost = int(card)*1000
    elif int(card) < 1000:
        cost = int(card)*100
    elif int(card) < 10000:
        cost = int(card)*10
    elif int(card) < 100000:
        cost = int(card)
    else:
        cost = int(card)
    with open("data/bank.json","r") as f:
        bank = json.load(f)
    if cost > bank[str(ctx.author.id)]["balance"]:
        balance = bank[str(ctx.author.id)]["balance"]
        return await ctx.send(f"please up your current balance `{balance}` to `{cost}`")
    collection = anime["origin"]
    if collection not in bank[str(ctx.author.id)]["cards"]:
        bank[str(ctx.author.id)]["cards"][str(collection)] = []
    if collection not in bank[str(ctx.author.id)]["cards"][str(collection)]:
        bank[str(ctx.author.id)]["cards"][str(collection)].append(collection)
    if anime["id"] not in bank[str(ctx.author.id)]["cards"][str(collection)]:
        toappend = f"""{anime["name"]} {anime["id"]}"""
        bank[str(ctx.author.id)]["cards"][str(collection)].append(str(toappend))
    else:
        return await ctx.send(f"""You already have {anime["name"]}""")
    bank[str(ctx.author.id)]["balance"] -= int(cost)
    with open("data/bank.json","w") as z:
        json.dump(bank,z)
    name = anime["name"]
    e = name.replace(" ","-")
    amtx = 1
    image = "."
    e = e.lower()
    print(e)
    ex = "."
    while ex.startswith("""<?xml version="1.0" encoding="UTF-8"?>""") == False:
        if ex.startswith("""<?xml version="1.0" encoding="UTF-8"?>""") == False:
            image = requests.request("GET",f"https://d2l56h9h5tj8ue.cloudfront.net/images/cards/{e}-{amtx}.jpg")
            ex = image.text
            if ex.startswith("""<?xml version="1.0" encoding="UTF-8"?>""") == False and amtx == 1:
                amtx += 1
    if amtx != 1:
        image = f"https://d2l56h9h5tj8ue.cloudfront.net/images/cards/{e}-2.jpg"
    else:
        image = anime["character_image"]
    embed = discord.Embed(title=f"successfully bought {name}",description=f"You bought {name} from {collection}",color=discord.Color.green())
    embed.set_image(url=image)
    await ctx.send(embed=embed)
@bot.command(aliases=["bal"])
async def balance(ctx,user:discord.Member=None):
    if user == None:
        user = ctx.author
    with open("data/bank.json","r") as f:
        bank = json.load(f)
    balance = bank[str(user.id)]["balance"]
    embed = discord.Embed(title=f"{user.name}'s balance",description=f"**balance:** `{balance}`💳",color=ctx.author.color)
    await ctx.send(embed=embed)
@bot.command()
async def trivia(ctx):
    with open("data/bank.json","r") as f:
        bank = json.load(f)
    response = requests.request("GET","https://opentdb.com/api.php?amount=1&category=31")
    anime = response.json()
    type = anime["results"][0]["type"]
    diff = anime["results"][0]["difficulty"]
    qn = anime["results"][0]["question"]
    qn = qn.replace("&quot;","")
    qn = qn.replace("&#039;","")
    correct = anime["results"][0]["correct_answer"]
    inc = anime["results"][0]["incorrect_answers"]
    answers = []
    answers.append(correct)
    for item in inc:
        answers.append(item)
    a = random.choice(answers)
    answers.remove(a)
    b = random.choice(answers)
    answers.remove(b)
    c = random.choice(answers)
    answers.remove(c)
    d = random.choice(answers)
    answers.remove(d)
    embed = discord.Embed(title="Anime Trivia",description=f"Pick an answer from A-D\nQuestion:{qn}\n**A)** {a}\n**B)** {b}\n**C)** {c}\n**D)** {d}",color=ctx.author.color)
    await ctx.send(embed=embed)
    try:

        choice = await bot.wait_for("message", check = lambda msg: msg.author == ctx.author, timeout = 30)
        if choice.content == "a" or choice.content == "A":
            answergiven = a
        elif choice.content == "b" or choice.content == "B":
            answergiven = b
        elif choice.content == "c" or choice.content == "C":
            answergiven = c
        elif choice.content == "d" or choice.content == "D":
            answergiven = d
        else:
            answergiven = "null"

    except asyncio.TimeoutError:
        return await ctx.send(f"You didn't answer, the answer was `{correct}`.")
    print(answergiven)
    if answergiven == correct:
        injected = random.randint(1,5000)
        await ctx.send(f"you won `{injected}` 💳")
        bank[str(ctx.author.id)]["balance"] += injected
        with open("data/bank.json","w") as z:
            json.dump(bank,z)
    else:
        return await ctx.send(f"You got it wrong, the answer was `{correct}`.")
@bot.command(aliases=["abox"])
async def box(ctx,action=None,type=None):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'From': 'cool5tarxv@gmail.com'  # This is another valid field
    }
    if action == None:
        embed = discord.Embed(title="Box Shop",description="Bronze box:\nfrom ids 1-1000\ncost: `10000`💳\nSilver box:\nfrom ids 1-10000\ncost: `100000`💳\nGold box:\nfrom ids 1-100000\ncost: `50000`💳",color=ctx.author.color)
        return await ctx.send(embed=embed)
    if action == "buy":
        if type == None:
            return await ctx.send("please enter a type such as `bronze`")
        id = 0
        cost = 0
        if type == "bronze":
            id = random.randint(1,1000)
            cost = 10000
        elif type == "silver":
            id = random.randint(1,10000)
            cost = 100000
        elif type == "gold":
            id = random.randint(1,100000)
            cost = 500000
        else:
            return await ctx.send("please enter a valid type")
        card = id
        response = requests.request("POST",f'https://www.animecharactersdatabase.com/api_series_characters.php?character_id={card}',headers=headers)
        print(response.text)
        anime = response.json()
        with open("data/bank.json","r") as f:
            bank = json.load(f)
        collection = anime["origin"]
        if collection not in bank[str(ctx.author.id)]["cards"]:
            bank[str(ctx.author.id)]["cards"][str(collection)] = []
        if collection not in bank[str(ctx.author.id)]["cards"][str(collection)]:
            bank[str(ctx.author.id)]["cards"][str(collection)].append(collection)
        if anime["id"] not in bank[str(ctx.author.id)]["cards"][str(collection)]:
            toappend = f"""{anime["name"]} {anime["id"]}"""
            bank[str(ctx.author.id)]["cards"][str(collection)].append(str(toappend))
        else:
            return await ctx.send(f"""You already have {anime["name"]} Bad Luck!""")
        bank[str(ctx.author.id)]["balance"] -= int(cost)
        with open("data/bank.json","w") as z:
            json.dump(bank,z)
        name = anime["name"]
        embed = discord.Embed(title=f"successfully bought {name}",description=f"You bought {name} from {collection}",color=discord.Color.green())
        embed.set_image(url=anime["character_image"])
        await ctx.send(embed=embed)

@bot.command()
async def deck(ctx,id=None):
    inte = True
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'From': 'cool5tarxv@gmail.com'  # This is another valid field
    }
    pages = []
    with open("data/bank.json","r") as f:
        bank = json.load(f)
    try:
        int(id)
    except:
        inte = False
    if inte != False:
        comment = ""
        it = "null"
        found = False
        try:
            int(id)
        except:
            return await ctx.send("Please only use ids to add to your deck")

        classer = get.getclass(int(id))
        if bank[str(ctx.author.id)]["deck"][classer] == str(id):
            bank[str(ctx.author.id)]["deck"][classer] = "None set yet use `jk!deck id` to add/remove a card"
            comment = "removed"
        else:
            bank[str(ctx.author.id)]["deck"][classer] = str(id)
            comment = "added"
        with open("data/bank.json","w") as z:
            json.dump(bank,z)
        return await ctx.send(f"Successfully {comment} `{id}` from deck")
    else:
        loadring = await ctx.send("loading...")
        if id != None:
            user = id
        else:
            user = ctx.author
        embed = discord.Embed(title=f"{user.name}'s deck",description=f"Your deck is used in battle, the order of combat from 1st to last:\n1. Beserker\n2. Rider\n3. Lancer\n4. Saber\n5. Archer\n6. Assassin\n7. Caster",color=ctx.author.color)
        pages.append(embed)
        for item in bank[str(user.id)]["deck"]:
            print(item)
            ids = bank[str(user.id)]["deck"][item]
            if ids == "None set yet use `jk!deck id` to add/remove a card":
                embed = discord.Embed(title=f"{item}",description="None set yet use `jk!deck id` to add/remove a card",color=ctx.author.color)
                pages.append(embed)
            else:
                itemz = requests.request("POST",f'https://www.animecharactersdatabase.com/api_series_characters.php?character_id={ids}',headers=headers)
                print(itemz.text)
                itemz = itemz.json()
                image = itemz["character_image"]
                name = itemz["name"]
                idx = itemz["id"]
                gender = itemz["gender"]
                desc = itemz["desc"]
                collection = itemz["origin"]
                card = itemz["id"]
                cost = "not found."
                if int(card) < 10:
                    cost = int(card)*1000
                elif int(card) < 100:
                    cost = int(card)*1000
                elif int(card) < 1000:
                    cost = int(card)*100
                elif int(card) < 10000:
                    cost = int(card)*10
                elif int(card) < 100000:
                    cost = int(card)
                else:
                    cost = int(card)
                classer = get.getclass(int(idx))
                att = get.getattack(int(idx))
                hp = get.gethp(int(idx))
                embed = discord.Embed(title=f"{item}",description=f"**Id:** `{id}`\n**Gender:** {gender}\n**collection:** {collection}\n**description:** *{desc}*\n**Cost:** `{cost}`\n**Class:** {classer}\n**Attack:** `{att}`\n**Health:** `{hp}`",color=ctx.author.color)
                embed.set_image(url=image)
                pages.append(embed)
        await asyncio.sleep(1)
        await loadring.edit(f"{ctx.author.mention} loaded!")
        await paginate(bot,ctx,pages,loadring)

@bot.command()
async def fight(ctx,user:discord.Member=None):
	embed = discord.Embed(title="Fight time!",description=f"{ctx.author.name} has challenged {user.name} to a fight.\n Type `accept` to start the fight.",color=ctx.author.color)
	await ctx.send(embed=embed)
	try:
		choice = await bot.wait_for("message", check = lambda msg: msg.author == user, timeout = 30)
		if choice.content.startswith("accept"):
			embed = discord.Embed(title="Fight time!",description=f"{ctx.author.name} has challenged {user.name} to a fight!",color=ctx.author.color)
			embed.set_image(url="https://steamuserimages-a.akamaihd.net/ugc/1743429419938967655/FE544A0351697618062E05713EC1CFA482C595E1/?imw=268&imh=268&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true")
			embed.add_field(name="loading",value="Fetching cards...")
			await ctx.send(embed=embed)

	except asyncio.TimeoutError:
		return await ctx.send("Well maybe next time.")


@bot.command()
async def public(ctx,action,action1=None,*,args=None):
    pub = funcs.getpub()
    if str(ctx.author.id) not in pub["users"]:
        funcs.openpub(ctx.author)
    if action == "view":
        if action1 == None:
            action1 = ctx.author.id
        if action1 not in pubs["users"]:
            await ctx.send("User not found! Please view by user id or use the search function.")
        # loading data to embed!
        with open("data/bank.json","r") as f:
            bank = json.load(f)
        avatar = pub["users"][str(action1)]["avatar"]
        desc = pub["users"][str(action1)]["description"]
        name = pub["users"][str(action1)]["name"]
        bal = bank[str(action1)]["balance"]
        amt = 0
        for item in bank[str(action1)]["cards"]:
            amt += 1
        embed = discord.Embed(title=f"{name}'s Profile!",description="",color=ctx.author.color)
        embed.set_image(url=avatar)
        embed.add_field(name="Description:",value=f"Status: {desc}\nBalance: {bal}\nCollections: {amt}",inline=False)
        await ctx.send(embed=embed)
    #if action == "":






@bot.listen("on_message")
async def open_account(message):
    pub = funcs.getpub()
    if str(message.author.id) not in pub:
        funcs.openpub(message.author)
    with open("data/bank.json","r") as f:
        bank = json.load(f)
    if str(message.author.id) not in bank:
        bank[str(message.author.id)] = {}
        bank[str(message.author.id)]["balance"] = 0
        bank[str(message.author.id)]["cards"] = {}
        # Deck
        bank[str(message.author.id)]["deck"] = {}
        bank[str(message.author.id)]["deck"]["beserker"] = "None set yet use `jk!deck id` to add/remove a card"
        bank[str(message.author.id)]["deck"]["rider"] = "None set yet use `jk!deck id` to add/remove a card"
        bank[str(message.author.id)]["deck"]["lancer"] = "None set yet use `jk!deck id` to add/remove a card"
        bank[str(message.author.id)]["deck"]["saber"] = "None set yet use `jk!deck id` to add/remove a card"
        bank[str(message.author.id)]["deck"]["archer"] = "None set yet use `jk!deck id` to add/remove a card"
        bank[str(message.author.id)]["deck"]["assassin"] = "None set yet use `jk!deck id` to add/remove a card"
        bank[str(message.author.id)]["deck"]["caster"] = "None set yet use `jk!deck id` to add/remove a card"
    """
    with open("data/collections.json","r") as k:
        cel = json.load(k)
    for item in cel:
        if item not in bank[str(message.author.id)]["cards"]:
            bank[str(message.author.id)]["cards"] = {}
            bank[str(message.author.id)]["cards"][str(item)] = []
    """
    with open("data/bank.json","w") as z:
        json.dump(bank,z)


with open("config.json","r") as x:
    cfg = json.load(x)
#keep_alive()
bot.run(cfg["token"])
