import asyncio
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
import json

def getpub():
    with open("data/public.json","r") as f:
        e = json.load(f)
    return e

def writepub(e):
    with open("data/public.json","w") as f:
        json.dump(e,f)

def openpub(user):
    pub = getpub()
    pub["users"][str(user.id)] = {}
    pub["users"][str(user.id)]["avatar"] = user.avatar_url
    pub["users"][str(user.id)]["name"] = user.name
    pub["users"][str(user.id)]["description"] = "no description."
    pub["users"][str(user.id)]["clans"] = []
    pub["users"][str(user.id)]["featured"] = {}
    pub["users"][str(user.id)]["featured"]["1"] = "."
    pub["users"][str(user.id)]["featured"]["2"] = "."
    pub["users"][str(user.id)]["featured"]["3"] = "."
    pub["users"][str(user.id)]["featured"]["4"] = "."
    pub["users"][str(user.id)]["featured"]["5"] = "."

async def get_main(ctx,editer,pages):
    if editer != None:
        main = editer
        await main.edit(content=None,embed=pages[0])
    else:
	    main = await ctx.send(embed=pages[0])
    return main
async def paginate(ctx,pages,bot,editer=None):
    main = await get_main(ctx,editer,pages)
    await main.add_reaction('⏮')
    await main.add_reaction('⏪')
    await main.add_reaction('⏹')
    await main.add_reaction('⏩')
    await main.add_reaction('⏭')
    current_page = 0
    for i in range(50):
    	def check(reaction, user):
    		return user == ctx.author
    	try:
    		reaction, user = await bot.wait_for('reaction_add', check = check, timeout = 10)
    		await main.remove_reaction(reaction, user)
    		if str(reaction) == '⏮':
    			await main.edit(embed=pages[0])
    		elif str(reaction) == '⏭':
    			await main.edit(embed=pages[len(pages)-1])
    			current_page = len(pages)-1
    		elif str(reaction) == '⏩':
    			page = current_page+1
    			current_page = page
    			try:
    				await main.edit(embed=pages[page])
    			except:
    				pass
    		elif str(reaction) == '⏪':
    			page = current_page-1
    			current_page = page
    			try:
    				await main.edit(embed=pages[page])
    			except:
    				pass
    		elif str(reaction) == '⏹':
    			current_page = 0
    			await main.clear_reactions()


    	except asyncio.TimeoutError:
    		await main.clear_reactions()
