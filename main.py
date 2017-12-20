import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
from kick import *

# init
client = Bot(description="KickBot", command_prefix="!", pm_help = True);


# on init
@client.event
async def on_ready():
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))


# wait for each message
@client.event
async def on_message(message):
	if message.content.startswith('!kick '):
		await votefor(client,message);
		await kick(client,message);

	if message.content.startswith('!help'):
		await client.send_message(message.channel,'Current available commands: !kick <name>,...');
		await client.send_message(message.channel,'Use !help for this message and !pmhelp for a private more thorough message');

	if message.content.startswith('!pmhelp'):
		await client.send_message(message.author,'--------');
		await client.send_message(message.author,'1.) !kick <person>:');
		await client.send_message(message.author,'Can be used to vote to kick someone. One can only vote for the someone once, repeatedly voting to kick someone results in an Akari no bully picture.');
 		
		await client.send_message(message.author,'Examples !kick Blake, !kick jake#0007, !kick vince');
		await client.send_message(message.author,'--------');

		await client.send_message(message.author,'2.) !help:');
		await client.send_message(message.author,'Sends a short command list in the channel its requested');
		await client.send_message(message.author,'--------');

		await client.send_message(message.author,'3.) !pmhelp:');
		await client.send_message(message.author,'Sends a private message to the requestor outlining the specifics for each command'); 

		await client.send_message(message.channel,'More help has been pmed to you');


	
	
# start	
client.run('INSERT TOKEN HERE')

#TODO restrict to certain channels with helpers and permissions
#TODO put it on github so others can contribute
#TODO set up AWS
#TODO umich API for clas notification and dining
#TODO implement database or just use pickle
#TODO updates on voting and timer based stuff
#TODO customize variables and options in KickBot
#TODO fun things like chatting with Kickbot(swear at it and itll kick/ban you)
#TODO implement banning
#TODO get token from another file





