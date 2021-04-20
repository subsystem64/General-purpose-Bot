import discord
import os
import json
import re
from discord.ext import commands
from discord.ext.commands import NotOwner
#from alive import alive

#===GET-PREFIX-FUNCTION===


def get_prefix(bot, message):
	try:
		with open('prefixes.json', 'r') as f:
			prefixes = json.load(f)
		return prefixes[str(message.guild.id)]
	except KeyError:  # if the code above failed and raise KeyError code below will executed
		#insert the data to json, and the return the default prefix
		with open('prefixes.json', 'r') as f:
			prefixes = json.load(f)

		prefixes[str(message.guild.id)] = '&'

		with open('prefixes.json', 'w') as f:
			json.dump(prefixes, f, indent=4)
		return "&"  # or you can repeat the process of getting the prefix


bot = commands.Bot(command_prefix=get_prefix)
bot.remove_command('help')

#===DISCORD-STATUS===


@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="&help 🦜"))
	print("logged in")

#===SEND-PREFIX-ON-PING===

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        with open("prefixes.json", "r") as f:
            data = json.loads(f.read())
            guildID = str(message.guild.id)
            prefix = data[guildID]
        author = message.author
        await message.channel.send(author.mention + " You can type **&help** for more info")
        await message.channel.send(f"My prefix for this server is: {prefix}")
        
    await bot.process_commands(message)


#===MANIPULATE-PREFIXES.JSON===

@bot.event
async def on_guild_join(guild):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)

	prefixes[str(guild.id)] = '&'

	with open('prefixes.json', 'w') as f:
		json.dump(prefixes, f, indent=4)

	with open('bannedwords.json', 'r') as f:
		words = json.load(f)

	words[str(guild.id)] = []

	with open('bannedwords.json', 'w') as f:
		json.dump(words, f, indent=4)



@bot.event
async def on_guild_remove(guild):
	with open('prefixes.json', 'r') as f:
		prefixes = json.load(f)

	prefixes.pop(str(guild.id))

	with open('prefixes.json', 'w') as f:
		json.dump(prefixes, f, indent=4)

	with open('bannedwords.json', 'r') as f:
		words = json.load(f)

	words.pop(str(guild.id))

	with open('bannedwords.json', 'w') as f:
		json.dump(words, f, indent=4)


#===COG-CONTROLS===


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


#===PERMISSION-ERROR-HANDLER===


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

#===KEEP-ALIVE===

#alive()

#===RUN-TOKEN===

bot.run("Nzg5MzkxMzAyMzU3ODExMjAw.X9xX8A.POdgbzvNOMdFdsNPrfChOvGjNlk")
