from telethon import TelegramClient, events
import os

api_id = 18850670
api_hash = 'e103ecbcc371550b5e699a8e2f207369'

client = TelegramClient('Deals', api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    chatid=event.chat_id    
    print("chatid")
    print(chatid)
    print("event")
    print(event)
    
    # path = await client.download_media(event.media, "./photo")
    # print('File saved to', path)
    if chatid==732565199:#(GrowDeals)
       msg=event.raw_text
       await client.send_message(732565199,msg)
         
    if chatid==-1001160797877:#(Price Histry detail)
        msg=event.raw_text
        await client.send_message(5739096966,msg)

    if chatid==-1001293749899:#(GrowDeals)
        msg=event.raw_text
        await client.send_message(5739096966,msg)

    if chatid==997904331:#(GrowDeals)
        msg=event.raw_text
        await client.send_message(5739096966,msg)

    if chatid==-1001450755585:#(TrindingDeals)
        msg=event.raw_text
        await client.send_message(5739096966,msg)

    if chatid==-1001420742409:#(TrueGrabbers)
        msg=event.raw_text
        await client.send_message(5739096966,msg)



client.start()
client.run_until_disconnected()