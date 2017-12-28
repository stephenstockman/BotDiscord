import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
from kick import *
from ban import *


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
		await voteKick(client,message);
		await kick(client,message);

	if message.content.startswith('!ban '):
		await voteBan(client,message);
		await ban(client,message);

	if message.content.startswith('!unban '):
		await unban(client,message);

	if message.content.startswith('!help'):
		await client.send_message(message.channel,'Current available commands: !kick <name>, !ban <name>,!unban <name>...');
		await client.send_message(message.channel,'Use !help for this message and !pmhelp for a private more thorough message');

	if message.content.startswith('!pmhelp'):
		await client.send_message(message.author,'--------');
		await client.send_message(message.author,'1.) !kick <person>:');
		await client.send_message(message.author,'Can be used to vote to kick someone. One can only vote for the someone once, repeatedly voting to kickban someone results in an Akari no bully picture. User kikced is sent an invite so this is really just for memes rather than actual use.');
 		
		await client.send_message(message.author,'Examples !kick Blake, !kick jake#0007, !kick vince');
		await client.send_message(message.author,'--------');

		await client.send_message(message.author,'3.) !ban <person>:');
		await client.send_message(message.author,'Can be used to vote to ban someone. One can only vote for the someone once, repeatedly voting to kick/ban someone results in an Akari no bully picture. Once ban passes the user is banned and sent an invite, which cant be used until after 1 day or until they are manually unbanned');
 		
		await client.send_message(message.author,'--------');
		await client.send_message(message.author,'4.) !unban <person>:');
		await client.send_message(message.author,'Unbans the person no voting needed');

		await client.send_message(message.author,'Examples !uban Blake, !uban jake#0007, !uban vince');
		await client.send_message(message.author,'--------');


		await client.send_message(message.author,'5.) !help:');
		await client.send_message(message.author,'Sends a short command list in the channel its requested');
		await client.send_message(message.author,'--------');

		await client.send_message(message.author,'6.) !pmhelp:');
		await client.send_message(message.author,'Sends a private message to the requestor outlining the specifics for each command'); 

		await client.send_message(message.channel,'More help has been pmed to you');


	
	
# start	
client.run('')

#TODO restrict to certain channels with helpers and permissions
#TODO umich API for class notification and dining
#TODO implement database or just use pickle
#TODO updates on voting and timer based stuff
#TODO customize variables and options in KickBot
#TODO auto unban after a period of time specified as seperate argument
#TODO get token from another file
#TODO move help stuff to seperate file





