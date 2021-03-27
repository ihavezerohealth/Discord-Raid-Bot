import asyncio
import discord
import yaml
import pathlib
import os
import random

## How to use:
## Follow the instructions lower down, then once you've checked the bot is logging in with your account(s) correctly:
## Send any message, or wait for someone else to send a message. This will trigger your account(s) to start spamming the server!

## This is intended to be used with multiple accounts - the real killer for the mods is having to mute/kick/ban LOADS of accounts.

class Raid:
    def __init__(self, token, channel_id:int):
        self.client = discord.Client()
        self.token = token
        self.channel_id = channel_id
        self.client.on_ready = self.client.event(self.on_ready)
        self.client.on_message = self.client.event(self.on_message)

    async def run(self):
        await self.client.start(self.token, bot=False)

    async def on_ready(self):
        print(f'Logged in as {self.client.user.name}')
        
    async def on_message(self, message):
        while True:
            await message.channel.send(message_you_want_to_spam)
            await asyncio.sleep(random.randrange(0,1.79))

#======================================
print("Starting bots:")

## These are the only parts that you change
message_you_want_to_spam = "WHAT A CRAPPY SERVER"

TOKENS = {
    ## Token goes here in double quotes "like this"               ## Channelid goes here  WITHOUT DOUBLE QUOTES
    "LIKE THIS":LIKETHIS,

}

loop = asyncio.get_event_loop()
tasks = []
for token in TOKENS.keys():
    miner = Raid(token, TOKENS[token])
    tasks.append(loop.create_task(miner.run()))

gathered = asyncio.gather(*tasks, loop=loop)
loop.run_until_complete(gathered)
