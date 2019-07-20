#!/usr/bin/python3
import discord, asyncio, main, m_conf

client = discord.Client()

@client.event
async def on_ready():
    print('name : ' + str(client.user.name))
    print('id   : ' + str(client.user.id))

def if_author_is_admin(message):
    if message.author.server_permissions.administrator:
        return True
    else:
        return False

@client.event
async def change_presence(text):
    await client.change_presence(game=discord.Game(name=text))

@client.event
async def say(message, text):
    await client.send_message(message.channel, text)

@client.event
async def say_somewhere(channel, text):
    await client.send_message(discord.Object(id=channel), text)

@client.event
async def delete_message(message):
    await client.delete_message(message)

@client.event
async def on_message(message):
    await main.on_message(message)

@client.event
async def on_message_delete(message):
    if message.author == client.user:
        return
    elif message.author.bot:
        return
#    main.on_message_delete(message)

@client.event
async def on_message_edit(before, after):
    if before.author == client.user:
        return
    elif before.author.bot:
        return
#    main.on_message_edit(before, after)


client.run(m_conf.read("auth", "token"))
