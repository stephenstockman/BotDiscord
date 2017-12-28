from vote import *
from ban import *
# tally and anti-abuse for voting
votesKick = {}
kickBound = 1;
async def voteKick(client,message):
	author = message.author;
	person = message.content[6:];
	channel = message.channel;

	if person not in votesKick:# person has never beem voted for yet
		votes.append(vote(author,person));
		votesKick[person]=1;
		await client.send_message(channel, 'Started kick vote on: '+person+' 1/'+str(kickBound));
		await nobully(client,message);
	else:
		if vote(author,person) not in votes:#person has been voted for but not by this author
			votesKick[person]+=1;
			votes.append(vote(author,person));
			await client.send_message(channel, 'Kick votes for: '+person+' now at '+str(votesKick[person])+'/'+str(kickBound));
			await nobully(client,message);
		else:# author already voted for this person
			await client.send_message(channel, 'No voting for the same person more than once');
			await nobully(client,message);

# kick the person if conditions are met
async def kick(client,message):
	author = message.author;
	person = message.content[6:];
	channel = message.channel;
	server = message.server;
	if votesKick[person] >= kickBound:
		invite = await client.create_invite(channel);
		await client.send_message(server.get_member_named(person),invite.url);

		await client.send_message(channel, 'Kicked: '+person);
		await client.kick(server.get_member_named(person));
		votesKick[person]=0;



		
