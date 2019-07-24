#!/usr/bin/python3
import discord, asyncio, m_conf, m_log, m_version, sys

if sys.version_info[0] != 3 or sys.version_info[1] < 5:
    print("This script requires Python version 3.5")
    giveup("Machine is lack of requirements.")
else:
    m_log.info("Machine is fully satisfied requirements for running this bot.")

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith("루냥아"):
        # parsing command
        message_t = message.content.replace("루냥아 ", '')
        args = message_t.split(' ')
        cmd = args[0]
        params = args[1:]
        # reacting to command
        if cmd == "도와줘":
            await say(message, embed=m_version.help(client, params))
        elif cmd == "업데이트내역":
            await say(message, embed=m_version.updatelog())

@client.event
async def bgjob_change_playing():
    while True:
        members_sum = 0
        for s in client.servers:
            members_sum += len(s.members)
        presences_list = ["루냥아 도와줘 : 도움말" , "루냥아 업데이트내역 : 업데이트 내역 보기", str(len(client.servers)) + "개의 서버에서 귀여움받는 중", str(members_sum) + "명의 유저들에게 귀여움받는 중", "v" + bot_ver, "이 메시지는 10초 마다 바뀌어요!"]
        for v in presences_list:
            await asyncio.sleep(10)
            await client.change_presence(game=discord.Game(name=v))

@client.event
async def say(message, text):
    try:
        await client.send_message(message.channel, text)
    except Exception as e:
        m_log.warn("failed to say : " + str(e))

@client.event
async def delete_message(message):
    try:
        await client.delete_message(message)
    except Exception as e:
        m_log.warn("failed to delete message : " + str(e))

@client.event
async def on_ready():
    m_log.info('bot is ready.')
    m_log.info('name    : ' + str(client.user.name))
    m_log.info('id      : ' + str(client.user.id))
    m_log.info('version : ' + m_version.bot_ver)
    client.loop.create_task(bgjob_change_playing())

try:
    token = m_conf.BOT_TOKEN
    if token == '':
        m_log.warn("no token provided in configuration file.")
        m_log.warn("manually providing bot token.")
        token = input("input your bot token (leave empty to exit) : ")
        if token == '':
            m_log.giveup("no token provided.")
    client.run(token)
except Exception as e:
    m_log.giveup("failed to load bot : " + str(e))
