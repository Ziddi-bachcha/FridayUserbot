#Copyright (C) 2020 The Sonia Roy company LLC.



#

#Img Module For Userbots ..... Designed And Developed By Phantom....NFX GANG

# Licensed under theSonia Roy Public License, Version 1.d (the "License");

# you may not use this file except in compliance with the License.
"""Download & Upload Images on Telegram\n
Syntax: `.img <Name>` or `.img (replied message)`
\n Upgraded and Google Image Error Fixed
"""

from userbot.google_imgs import googleimagesdownload
import os
import shutil
from re import findall
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="img ?(.*)"))
async def img_sampler(event):
    await event.edit("`Tham jaa horha hai download....bs thoda sabar rakh...`")
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply:
        query = reply.message
    else:
    	await event.edit("`aaha. Us msg ke reply me .img command do jisko tumhe google search karna hai samjhe...ghusa kuch khaki khopdi me ? ;_;`")
    	return
        
    lim = findall(r"lim=\d+", query)
    # lim = event.pattern_match.group(1)
    try:
        lim = lim[0]
        lim = lim.replace("lim=", "")
        query = query.replace("lim=" + lim[0], "")
    except IndexError:
        lim = 5
    response = googleimagesdownload()

    # creating list of arguments
    arguments = {
        "keywords": query,
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory"
    }

    # passing the arguments to the function
    paths = response.download (arguments)
    lst = paths[0][query]
    await event.client.send_file(await event.client.get_input_entity(event.chat_id), lst)
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    await event.delete()
