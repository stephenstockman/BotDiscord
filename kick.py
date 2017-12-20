import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

votes = []# list of any vote that was valid
votesfor = {}# dixtionary of people with votes against them<key> and the number of votes<value>
noBully = []
# vote class for distinguishing unique votes
class vote:
	author='';
	person='';
	
	def __init__(self,author,person):
		self.author = author;
		self.person=person;

	def __hash__(self):
       		return hash((self.author, self.person))

	def __eq__(self, other):
        	return (self.author, self.person) == (other.author, other.person)

	def __ne__(self, other):
        	return not(self == other)

# tally and anti-abuse for voting
async def votefor(client,message):
	author = message.author;
	person = message.content[6:];
	channel = message.channel;

	if person not in votesfor:# person has never beem voted for yet
		votes.append(vote(author,person));
		votesfor[person]=1;
		await client.send_message(channel, 'Started vote on: '+person+' 1/3');
		await nobully(client,message);
	else:
		if vote(author,person) not in votes:#person has been voted for but not by this author
			votesfor[person]+=1;
			votes.append(vote(author,person));
			await client.send_message(channel, 'Votes for: '+person+' now at '+str(votesfor[person])+'/3');
			await nobully(client,message);
		else:# author already voted for this person
			await client.send_message(channel, 'No voting for the same person more than once');
			await nobully(client,message);

# kick the person if conditions are met
async def kick(client,message):
	author = message.author;
	person = message.content[6:];
	channel = message.channel;
	if votesfor[person] >= 3:
		await client.send_message(channel, 'Kicked: '+person);
		await client.kick(person);

# akari no bully picture in response to abuse
async def nobully(client,message):
	author = message.author;
	channel = message.channel;
	noBully.append(author);
	if noBully.count(author) >= 5:
		await client.send_file(channel, 'images/nobully.jpg');
		noBully.clear();
		
