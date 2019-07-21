#!/usr/bin/python3

bot_ver = "0.0.1"

import sys, m_log, m_help, m_api, m_conf, discord, asyncio

def giveup(text):
    m_log.error("Giving Up. Reason : " + text)
    sys.exit()

if sys.version_info[0] != 3 or sys.version_info[1] < 5:
    print("This script requires Python version 3.5")
    giveup("Machine is lack of requirements.")
else:
    m_log.info("Machine's Python version is 3.5+.")

async def MessageReceived(message):
    if message.content.startswith("루냥아"):
        # parsing command
        message_t = message.content.replace("루냥아 ", '')
        args = message_t.split(' ')
        cmd = args[0]
        params = args[1:]
        # reacting to command
        await m_api.say(message, 'success')
#        if cmd == "도와줘":
#            await m_api.say(message, embed=m_help.help(params))
#        elif cmd == "업데이트내역":
#            await m_api.say(message, embed=m_help.updatelog())
