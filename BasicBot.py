import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

# init
client = Bot(description="KickBot", command_prefix="!", pm_help = True);
votes = []
memUsedVotes=[]
noBully=[]

# on init
@client.event
async def on_ready():
	servers = client.servers
	for serv in servers:
		server = serv;
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+server.name+'| Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))

canVote=1;

@client.event
async def on_message(message):
	global canVote
	if message.content.startswith('!kick'):
		if [message.author,message.content[6:]] not in memUsedVotes:
			memUsedVotes.append([message.author,message.content[6:]]);
			canVote=1;
			noBully.append(message.author);
			if noBully.count(message.author) >= 3:
				await client.send_file(message.channel, 'images/nobully.jpg');
				noBully.clear();
		else:
			canVote=0;
		print(memUsedVotes);
	
	await client.process_commands(message)


@client.command()
async def kick(*name):
	global canVote
	if canVote == 1:
		servers = client.servers
		for serv in servers:
			server = serv;
		present = 0;
		for ind in enumerate(votes):
			if ind[1][0] == name:
				present = 1;

		if present == 0:
			votes.append([name,1]);
		else:
			for ind in enumerate(votes):
				if ind[1][0] == name:
					ind[1][1]=ind[1][1]+1;
				if (ind[1][1] > 1):
					kickme = server.get_member_named(name[0])
					print('kicking: '+kickme.name)
					await client.kick(kickme);
	print(votes)
	
		

# start	
client.run('ENTER TOKEN HERE')

#TODO short help for in channel message, long help via PM
#TODO restrict to certain channels with helpers and permissions
#TODO put it on github so others can contribute
#TODO set up AWS
#TODO bananaboat chat, kick users, delete it, send everyone a pm with who and new invite
#TODO umich API for clas notification and dining
#TODO order into modules and classes for each operation
#TODO implement database or just use pickle
#TODO fix looping and list stuff in kick so its not dumb




