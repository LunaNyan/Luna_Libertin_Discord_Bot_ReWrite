#!/usr/bin/python3

import m_api, m_conf

def on_message(message):
    if message.content.startswith("hello"):
        m_api.say(message, "hello there")

def on_message_delete(message):
    print(message.content)

def on_message_edit(before, after):
    print(after.content)
