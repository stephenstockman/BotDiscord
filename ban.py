from vote import *
# tally and anti-abuse for voting
votesBan = {}
banBound = 5;
async def voteBan(client,message):
	author = message.author;
	person = message.content[5:];
	channel = message.channel;

	if person not in votesBan:# person has never beem voted for yet
		votes.append(vote(author,person));
		votesBan[person]=1;
		await client.send_message(channel, 'Started vote on: '+person+' 1/'+str(banBound));
		await nobully(client,message);
	else:
		if vote(author,person) not in votes:#person has been voted for but not by this author
			votesBan[person]+=1;
			votes.append(vote(author,person));
			await client.send_message(channel, 'Votes for: '+person+' now at '+str(votesBan[person])+'/'+str(banBound));
			await nobully(client,message);
		else:# author already voted for this person
			await client.send_message(channel, 'No voting for the same person more than once');
			await nobully(client,message);


# ban the person if conditions are met
async def ban(client,message):
	author = message.author;
	person = message.content[5:];
	channel = message.channel;
	server = message.server;
	if votesBan[person] >= banBound:
		votesBan[person]=0;
		invite = await client.create_invite(channel);
		await client.send_message(server.get_member_named(person),invite.url);
		
		await client.send_message(channel, 'Banned: '+person);
		await client.ban(server.get_member_named(person),1);# 1 day is the curent min

# currently banning is free-ie anyone can unban with one vote
async def unban(client,message):
	author = message.author;
	person = message.content[7:];
	channel = message.channel;
	server = message.server;
	banned = await client.get_bans(server);
	for us in banned:
		if us.name == person:
			user = us
	await client.send_message(channel, 'Unbanned: '+person);
	await client.unban(server,user);
	

