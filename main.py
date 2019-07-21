#!/usr/bin/python3

import sys, m_log

if sys.version_info[0] != 3 or sys.version_info[1] < 5:
    print("This script requires Python version 3.5")
    m_log.error("Machine is lack of requirements. Giving up.")
    sys.exit()
else:
    m_log.info("Machine's Python version is 3.5+.")

import discord, asyncio
import m_api, m_conf

async def on_message(message):
    if message.content.startswith("루냥아"):
        # parsing command
        message_t = message.content.replace("루냥아 ", '')
        args = message_t.split(' ')
        cmd = args[0]
        params = args[1:]
        # reacting to command
        await m_api.say(message, "message_t : " + message_t + "\nargs : " + str(args) + "\ncmd : " + str(cmd) + "\nparams : " + str(params))
