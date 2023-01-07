import discord

client = discord.Client()

@client.event
async def on_message(message):
    content = message.content
    author = message.author

    if content.startswith('!ping'):
        await message.channel.send("{0.author.mention}: pong!".format(message))

client.run('YOUR_TOKEN_HERE', bot=False) 
