import discord
import os
import json
from discord import Intents
from discord.ext import commands
from discord.ext.commands import NotOwner

#===GET PREFIX FUNCTION===


def get_prefix(bot, message):
	try:
		with open('./configs/prefixes.json', 'r') as f:
			prefixes = json.load(f)
		return prefixes[str(message.guild.id)]
	except KeyError:  #If KeyError is returned (Unable to find matching entry in json)
		#insert the data to json and return the default prefix
		with open('prefixes.json', 'r') as f:
			prefixes = json.load(f)

		prefixes[str(message.guild.id)] = '&'

		with open('prefixes.json', 'w') as f:
			json.dump(prefixes, f, indent=4)
		return "&" 

#===Intents===

intents = Intents.all()

bot = commands.Bot(command_prefix=get_prefix, intents = intents)
bot.remove_command('help')

#===DISCORD STATUS===

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="&help 🦜"))
	print("logged in")

#===SENDs PREFIX ON PING===

@bot.event
async def on_message(message):
    if message.mention_everyone:
        return
    if bot.user.mentioned_in(message):
        with open("./configs/prefixes.json", "r") as f:
            data = json.loads(f.read())
            guildID = str(message.guild.id)
            prefix = data[guildID]
        author = message.author
        await message.channel.send(author.mention + " You can type **&help** for more info")
        await message.channel.send(f"My prefix for this server is: {prefix}")
        
    await bot.process_commands(message)


#===ADDS GUILD ENTRY TO JSON===

@bot.event
async def on_guild_join(guild):
    #creates default prefix entry
	with open('./configs/prefixes.json', 'r') as f:
		prefixes = json.load(f)

	prefixes[str(guild.id)] = '&'

	with open('./configs/prefixes.json', 'w') as f:
		json.dump(prefixes, f, indent=4)
    #creates empty word filter entry
	with open('./configs/bannedwords.json', 'r') as f:
		words = json.load(f)

	words[str(guild.id)] = []

	with open('./configs/bannedwords.json', 'w') as f:
		json.dump(words, f, indent=4)
    #creates default autowelcome entry
	with open('./configs/autowelcome.json', 'r') as f:
		words = json.load(f)

	words[str(guild.id)] = "false"

	with open('./configs/autowelcome.json', 'w') as f:
		json.dump(words, f, indent=4)
    #creates empty autorole entry
	with open('./configs/autorole.json', 'r') as f:
		words = json.load(f)

	words[str(guild.id)] = []

	with open('./configs/autorole.json', 'w') as f:
		json.dump(words, f, indent=4)

#===REMOVES GUILD ENTRY IN JSON===

@bot.event
async def on_guild_remove(guild):
    #removes prefix setting
	with open('./configs/prefixes.json', 'r') as f:
		prefixes = json.load(f)

	prefixes.pop(str(guild.id))

	with open('./configs/prefixes.json', 'w') as f:
		json.dump(prefixes, f, indent=4)

    #removes word filter setting
	with open('./configs/bannedwords.json', 'r') as f:
		words = json.load(f)

	words.pop(str(guild.id))

	with open('./configs/bannedwords.json', 'w') as f:
		json.dump(words, f, indent=4)

    #removes autowelcome setting
	with open('./configs/autowelcome.json', 'r') as f:
		words = json.load(f)

	words.pop(str(guild.id))

	with open('./configs/autowelcome.json', 'w') as f:
		json.dump(words, f, indent=4)
    #removes autorole setting
	with open('./configs/autorole.json', 'r') as f:
		words = json.load(f)

	words.pop(str(guild.id))

	with open('./configs/autorole.json', 'w') as f:
		json.dump(words, f, indent=4)


#===COG CONTROLS===


@bot.command()
@commands.is_owner()
async def load(ctx, extension):
	bot.load_extension(f'cogs.{extension}')
	await ctx.send(f'cogs.{extension} has loaded.')


@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
	bot.unload_extension(f'cogs.{extension}')
	await ctx.send(f'cogs.{extension} has unloaded.')


@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
	bot.unload_extension(f'cogs.{extension}')
	bot.load_extension(f'cogs.{extension}')
	await ctx.send(f'cogs.{extension} has reloaded.')


#===COG CONTROL PERMISSION ERROR HANDLER===


@load.error
async def load_error(ctx, error):
	if isinstance(error, NotOwner):
		await ctx.send(":x: Insufficient permissions. You do not own this bot")


@unload.error
async def unload_error(ctx, error):
	if isinstance(error, NotOwner):
		await ctx.send(":x: Insufficient permissions. You do not own this bot")


@reload.error
async def reload_error(ctx, error):
	if isinstance(error, NotOwner):
		await ctx.send(":x: Insufficient permissions. You do not own this bot")


for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')

#===KEEP ALIVE===

#alive()

#===BOT TOKEN===

bot.run("")
