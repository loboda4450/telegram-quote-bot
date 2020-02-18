import random
from telethon import TelegramClient, events

with open("cfg.txt", "r") as config:
    cfg = [line.rstrip() for line in config]

client = TelegramClient('bot', cfg[0], cfg[1]).start(bot_token=cfg[2])

with open("responses.txt", "r") as f:
    responses = [response.rstrip() for response in f]


@client.on(events.InlineQuery)
async def querylist(event):
    builder = event.builder
    picked = random.choice(responses)
    ans = builder.article(picked, text=picked)

    await event.answer([ans])


@client.on(events.NewMessage)
async def answer(event):
    await event.reply(random.choice(responses))


client.start()
client.run_until_disconnected()
