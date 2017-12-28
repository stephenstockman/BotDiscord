
votes = []# list of any vote that was valid
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

# akari no bully picture in response to abuse
async def nobully(client,message):
	author = message.author;
	channel = message.channel;
	noBully.append(author);
	if noBully.count(author) >= 5:
		await client.send_file(channel, 'images/nobully.jpg');
		noBully.clear();
