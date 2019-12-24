#!/usr/bin/python3

import sys
import discord, asyncio
import configparser

sys.path.append('./modules/')
import m_db
sys.path.append('../')

conf = configparser.ConfigParser()

try:
    conf_path = "config.ini"
    conf = configparser.ConfigParser()
    conf.read(conf_path)
    print("INFO    : Configuration file loaded")
except Exception as e:
    print("FATAL   : Couldn't load configuration file : " + str(e))
    sys.exit(1)

client = discord.Client()

@client.event
async def count_reset():
    while True:
        await asyncio.sleep(1800)
        m_db.purge_counts()

@client.event
async def on_ready():
    print('INFO    : Bot is ready to use.')
    print("INFO    : Account : " + str(client.user.name) + "(" + str(client.user.id) + ")")
    client.loop.create_task(count_reset())

@client.event
async def on_message(message):
    try:
        u_count = m_db.user_count(message)
        g_count = m_db.guild_count(message)

print("INFO    : connecting to Discord. Please Wait..")
client.run(conf.get("config", "bot_token"))