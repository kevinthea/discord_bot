# bot.py
import discord
from pathlib import Path

# Needed to load env
import os
from dotenv import load_dotenv
load_dotenv()

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
	# ignore your own output as input
    if message.author == client.user:
        return
    if message.content.startswith('-welcome'):
    	embed_msg = discord.Embed(
    		color=discord.Color.green(),
        	title = "Welcome!",
        	description="Introduce yourself and enjoy your stay" + "\n" + "...",
    	)
    	## This works fine
    	# embed_msg.set_image(url="https://c.tenor.com/xLkmU4JRI7oAAAAC/wave-snorlax.gif")
    	##
    	#assets_path = os.path.join(__file__, 'wave-snorlax.gif')
    	#print(assets_path)
    	#file = discord.File(assets_path, filename="wave-snorlax.gif")
    	#embed_msg.set_image(url="attachment://wave-snorlax.gif")
    	#script_dir = Path(__file__)
    	#asset_path = os.path.join(dir,"assets")
    	##print(dir)
    	#rel_dir = "assets/wave-snorlax.gif"
    	#abs_dir = os.path.join (script_dir, rel_dir)
    	await client.get_channel(CHANNEL_ID).send(embed=embed_msg)

@client.event
async def on_member_join(member):
	channel = client.get_channel(CHANNEL_ID)
	await channel.send('Welcome to ' + GUILD + ', ' + member.name + '!')

client.run(TOKEN)