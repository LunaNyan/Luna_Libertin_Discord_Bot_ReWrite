#!/usr/bin/python3
import discord, asyncio, m_conf, m_log, luna_libertin_rewrite

client = discord.Client()

@client.event
async def on_ready():
    m_log.info('bot is ready.')
    m_log.info('name    : ' + str(client.user.name))
    m_log.info('id      : ' + str(client.user.id))
    m_log.info('version : ' + luna_libertin_rewrite.bot_ver)

def if_author_is_admin(message):
    if message.author.server_permissions.administrator:
        return True
    else:
        return False

@client.event
async def change_presence(text):
    try:
        await client.change_presence(game=discord.Game(name=text))
    except Exception as e:
        m_log.warn("failed to change persence : " + str(e))

@client.event
async def say(message, text):
    try:
        await client.send_message(message.channel, text)
    except Exception as e:
        m_log.warn("failed to say : " + str(e))

@client.event
async def say_somewhere(channel, text):
    try:
        await client.send_message(discord.Object(id=channel), text)
    except Exception as e:
        m_log.warn("failed to say somewhere : " + str(e))

@client.event
async def delete_message(message):
    try:
        await client.delete_message(message)
    except Exception as e:
        m_log.warn("failed to delete message : " + str(e))

@client.event
async def on_message(message):
    await luna_libertin_rewrite.MessageReceived(message)

try:
    token = m_conf.read("auth", "token")
    if token == '':
        m_log.warn("no token provided in configuration file.")
        m_log.warn("manually providing bot token.")
        token = input("input your bot token (leave empty to exit) : ")
        if token == '':
            luna_libertin_rewrite.giveup("no token provided.")
    client.run(token)
except Exception as e:
    luna_libertin_rewrite.giveup("failed to load bot : " + str(e))
