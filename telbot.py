# from asyncio.windows_events import NULL
from telethon import TelegramClient, events
import os

api_id = 18850670
api_hash = 'e103ecbcc371550b5e699a8e2f207369'

client = TelegramClient('Deals', api_id, api_hash)


@client.on(events.NewMessage)
async def handler(event):
    # chat = await event.get_chat()
    chatid = event.chat_id
    print("chatid")
    print(chatid)
    print("event")
    print(event)
    print()
    # print(chat)
    path = await client.download_media(event.media, "./photo")
    print('File saved to', path)  # printed after download is done
    rawdata = event.raw_text
    
    if "amzn" in rawdata:
     if (path):
        if chatid == 997904331:  # (Price Histry detail)7#997904331:#(me)
         msg = event.raw_text
        #    await client.send_message(5739096966,msg)
         await client.send_file(5739096966,path,caption=msg)
        if chatid == -1001160797877:  # (Price Histry detail)7#997904331:#(me)
         msg = event.raw_text
         await client.send_file(5739096966,path,caption=msg)
        if chatid == 732565199:  # (test)7#997904331:#(me)
         msg = event.raw_text
        #  try:
         sender = await event.get_sender()
         print(sender)
         await client.send_file(5739096966,path,caption=msg)
        #  except e:
        #      print(e)
        if chatid == -1001293749899:  # (GrowDeals)7#997904331:#(me)
         msg = event.raw_text
         await client.send_file(5739096966,path,caption=msg)
        if chatid == -1001450755585:  # (TrindingDeals)7#997904331:#(me)
         msg = event.raw_text
         await client.send_file(5739096966,path,caption=msg)
        if chatid == -1001420742409:  # (TrueGrabbers)7#997904331:#(me)
         msg = event.raw_text
         await client.send_file(5739096966,path,caption=msg)
     else:
        if chatid == 997904331:  # (Price Histry detail)7#997904331:#(me)
         msg = event.raw_text
        #    await client.send_message(5739096966,msg)
         await client.send_message(5739096966, msg)
        if chatid == -1001160797877:  # (Price Histry detail)7#997904331:#(me)
         msg = event.raw_text
         await client.send_message(5739096966, msg)
        if chatid == 732565199:  # (test)7#997904331:#(me)
         msg = event.raw_text
         await client.send_message(5739096966, msg)
        if chatid == -1001293749899:  # (GrowDeals)7#997904331:#(me)
         msg = event.raw_text
         await client.send_message(5739096966, msg)
        if chatid == -1001450755585:  # (TrindingDeals)7#997904331:#(me)
         msg = event.raw_text
         await client.send_message(5739096966, msg)
        if chatid == -1001420742409:  # (TrueGrabbers)7#997904331:#(me)
         msg = event.raw_text
         await client.send_message(5739096966, msg)
         
    else:
         if (path):
          if chatid == 997904331:  # (Price Histry detail)7#997904331:#(me)
           msg = event.raw_text
          #    await client.send_message(5739096966,msg)
           await client.send_file(1485109749,path,caption=msg)
          if chatid == -1001160797877:  # (Price Histry detail)7#997904331:#(me)
           msg = event.raw_text
           await client.send_file(1485109749,path,caption=msg)
          if chatid == 732565199:  # (test)7#997904331:#(me)
           msg = event.raw_text
           await client.send_file(1485109749,path,caption=msg)
          if chatid == -1001293749899:  # (GrowDeals)7#997904331:#(me)
           msg = event.raw_text
           await client.send_file(1485109749,path,caption=msg)
          if chatid == -1001450755585:  # (TrindingDeals)7#997904331:#(me)
           msg = event.raw_text
           await client.send_file(1485109749,path,caption=msg)
          if chatid == -1001420742409:  # (TrueGrabbers)7#997904331:#(me)
           msg = event.raw_text
           await client.send_file(1485109749,path,caption=msg)
         else:
          if chatid == 997904331:  # (Price Histry detail)7#997904331:#(me)
           msg = event.raw_text
          #    await client.send_message(5739096966,msg)
           await client.send_message(1485109749, msg)
          if chatid == -1001160797877:  # (Price Histry detail)7#997904331:#(me)
           msg = event.raw_text
           await client.send_message(1485109749, msg)
          if chatid == 732565199:  # (test)7#997904331:#(me)
           msg = event.raw_text
           print(msg)
           await client.send_message(1485109749, msg)
          if chatid == -1001293749899:  # (GrowDeals)7#997904331:#(me)
           msg = event.raw_text
           await client.send_message(1485109749, msg)
          if chatid == -1001450755585:  # (TrindingDeals)7#997904331:#(me)
           msg = event.raw_text
           await client.send_message(1485109749, msg)
          if chatid == -1001420742409:  # (TrueGrabbers)7#997904331:#(me)
           msg = event.raw_text
           await client.send_message(1485109749, msg)
            
        
        
       
       
    # if chatid==-1001160797877 or -1001293749899 or -1001450755585 or -1001420742409:
    #             #(Price Histry detail) or (GrowDeals) or (TrindingDeals) or (TrueGrabbers)
    #     msg=event.raw_text
    #     # try:
    #     await client.send_message(5739096966,msg)
    #     # except e :
    #     #     print(e)

client.start()
client.run_until_disconnected()
