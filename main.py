#!/usr/bin/python3

import m_api, m_conf, discord, asyncio

async def on_message(message):
    if message.content.startswith("루냥아"):
        # parsing command
        message_t = message.content.replace("루냥아 ", '')
        args = message_t.split(' ')
        cmd = args[0]
        params = args[1:]
        # reacting to command
        await m_api.say(message, "message_t : " + message_t + "\nargs : " + str(args) + "\ncmd : " + str(cmd) + "\nparams : " + str(params))
