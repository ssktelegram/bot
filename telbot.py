from telethon import TelegramClient, events
import os

api_id = 18850670
api_hash = 'e103ecbcc371550b5e699a8e2f207369'

client = TelegramClient('Deals', api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    chat = await event.get_chat()
    chatid=event.chat_id    
    print("chatid")
    print(chatid)
    print("event")
    print(event)
    print()
    print(chat)


    if chatid==732565199:#(GrowDeals)
       msg=event.raw_text
       await client.send_message(997904331,msg)
         
    if chatid==-1001160797877 or -1001293749899 or -1001450755585 or -1001420742409:
                #(Price Histry detail) or (GrowDeals) or (TrindingDeals) or (TrueGrabbers)
        msg=event.raw_text
        # try:
        await client.send_message(5739096966,msg)
        # except e :
        #     print(e)

    # if chatid==-1001293749899:#(GrowDeals)
    #     msg=event.raw_text
    #     try:
    #      await client.send_message(5739096966,msg)
    #     except ValueError:
    #         print(ValueError)

    # if chatid==997904331:#(GrowDeals)
    #     msg=event.raw_text
    #     try:
    #      await client.send_message(5739096966,msg)
    #     except ValueError:
    #         print(ValueError)
            
    # if chatid==-1001450755585:#(TrindingDeals)
    #     msg=event.raw_text
    #     try:
    #      await client.send_message(5739096966,msg)
    #     except ValueError:
    #         print(ValueError)
            
    # if chatid==-1001420742409:#(TrueGrabbers)
    #     msg=event.raw_text
    #     try:
    #      await client.send_message(5739096966,msg)
    #     except ValueError:
    #         print(ValueError)


client.start()
client.run_until_disconnected()