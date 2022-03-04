import discord 
import json


# open a connection with discord 
client = discord.Client()

# print a statment in the chat that the bot is logged in as this person 
@client.event 
async def on_ready():
    print('I have logged in as {0.user}'.format(client))


# if a user in the channel types hellow the bot will pick up detected the hello and reply its own hello
# This is how the bot will display our message 
# So anything we want the bot to display in the channel chat is gonna be here  
@Client.event 
async def on_message(message):
    if message.author == client.user:
        return 
    if message.content.startwith('$hello'):
        await message.channel.send('Hello!')


# client.run('what ever our token will be')
# this will run the codes when we have everything setup 

# this will ope na json file 
with open ('.//Yahoo_Json','r') as f:
    outfile = open('.//Test_file.txt', 'w') # use for test
    line = f.readline()
    count_line = 0
    while line:
        data = json.loads(line)
        outfile.write() # test if our parseing are what we need

