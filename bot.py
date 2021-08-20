# bot.py
import discord
from random import randrange
from pathlib import Path

# Needed to load env
import os
from dotenv import load_dotenv
load_dotenv()

# bot token, actual value shouldn't be exposed
TOKEN = os.getenv('DISCORD_TOKEN')

# server name
GUILD = os.getenv('DISCORD_GUILD')

# .getenv returns a string
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL'))

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	print('Working in channel id: ' + str(CHANNEL_ID))
	print('Working in channel: ' + str(client.get_channel(CHANNEL_ID)))

@client.event
async def on_message(message):
	channel = client.get_channel(CHANNEL_ID)
	# ignore your own output as input
	if message.author == client.user:
		return

	# welcome a user by typing "-welcome" into the channel
	if message.content.startswith('-welcome'):
		embed_msg = discord.Embed(
			color=discord.Color.green(),
			title = "Welcome!",
			description="Introduce yourself and enjoy your stay" + "\n" + "...",
		)
		####################################################
		## TODO : Use local assets instead of online URLS ##
		####################################################
		## This works fine
		# embed_msg.set_image(url="https://c.tenor.com/xLkmU4JRI7oAAAAC/wave-snorlax.gif")
		##
		#assets_path = Path(__file__)
		#assets_path = assets_path / "assets"
		#print(assets_path)
		#print(type(assets_path))
		#p = assets_path.glob('**/*')
		#files = [x for x in p if x.is_file()]
		#print(files)
		#os.listdir(assets_path)
		#file = discord.File(assets_path, filename="wave-snorlax.gif")
		#embed_msg.set_image(url="attachment://wave-snorlax.gif")

		await channel.send(embed=embed_msg)

	# dice roll
	if message.content.startswith('-roll'):
		args = message.content.split()[1:]
		if(len(args)!=2):
			await channel.send("Invalid input; use -roll <number of dice> <number of sides the dice has>")
			return
		num_of_dice = int(args[0])
		num_of_sides = int(args[1])
		if(int(args[0]) <= 0 or int(args[1]) <= 0):
			await channel.send("Invalid input; use -roll <number of dice> <number of sides the dice has>")
			return
		# args[0] = number of dice to roll
		# args[1] = number of sides on dice
		await channel.send('Rolling ' + args[0] + " dice with " + args[1] + " sides!")
		result = []
		for x in range(num_of_dice):
			roll = str(randrange(1,num_of_sides+1)) + "/" + str(num_of_sides)
			result.insert(x, roll)
		await channel.send(result)
		

@client.event
async def on_member_join(member):
	channel = client.get_channel(CHANNEL_ID)
	await channel.send('Welcome to ' + GUILD + ', ' + member.name + '!')

client.run(TOKEN)