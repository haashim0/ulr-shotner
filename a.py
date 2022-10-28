import aiohttp
import re
from b import *
from c import *
from d import *
from e import *

# GLOBAL-VAR
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}


# WEB-ZONE

async def request(url):
    async with aiohttp.ClientSession() as s:
        async with s.get(url, headers=header, timeout=20) as r:
            return await r.json()

from f import *
start_message = """<b>
Hey There, {}
🔀 I Can Convert Link To ShortLink
💬 Send Me Any Message With Links
🔗 I Will Shorten All Links In It 
🔂 Convert to <a href="https://MetaUrls.in/member/tools/bookmarklet">ShortUrlLink</a>

©️Powered By @MetaUrlsOfficial
</b>"""
start_button = [[Button.url("Join Channel ♥️", "t.me/MetaUrlsOfficial"), Button.inline("About Bot 🤖", "abt")],
                [Button.inline("Connect To Shortner 🔗", 'api')]]

api_message = """
<b>Which Shortner Do u Want to Connect To:</b>
"""
api_button = [Button.url("MetaUrls.in", "https://MetaUrls.in/member/tools/bookmarklet")]

about_text = """<b>



🤖 Name :  MetaUrls.in Link Convertor

🔠 Language : Python3
📚 Library     : Telethon
🧑🏻‍💻 Developer : @MetaUrls_owner

©️Powered By @MetaUrlsOfficial
</b>"""

async def get_json(url, api, stype=1):
    url = f"https://MetaUrls.in/api?api={api}&url={url}"
    if stype != 1:
        url = f"https://MetaUrls.in/api?api={api}&url={url}"
    print(url)
    async with aiohttp.ClientSession() as s:
        for i in range(3):
            try:
                async with s.get(url, headers=header, timeout=20) as res:
                    res = await res.json()
                    print(res)
                    return res
            except Exception as e:
                print(e)
        return False


async def shortner(links, api, stype):
    nlist = []
    for i in range(len(links)):
        if re.search(r"t\.me|yout|yt\.", links[i]):
            nlist.append(links[i])
            continue
        link = await get_json(links[i], api, stype)
        try:
            link = link["shortenedUrl"]
        except Exception as e:
            print(e)
            link = ""
        nlist.append(link)
    return nlist


# API_ZONE

async def api_checker(api):
    url = f"https://metaurls.in/api?api={api}&url=https://www.google.com"
    r = await request(url)
    print(r)
    if r["status"] != "error":
        return 1, "sucess"


# TEXT-CHANGER-ZONE
async def link_replacer(c, links, nlinks):
    for i in range(len(links)):
        c = c.replace(links[i], nlinks[i])
    return c


async def username_check(c):
    if re.search('@[^\s]+', c):
        return True
    else:
        return False


async def remove_username(c, username):
    c = re.sub('@[^\s]+', username, c)
    return c


async def link_extractor(c):
    links = re.findall("(?P<url>https?://[^\s]+)", c)
    return links


async def bolder(c):
    return "<b> " + c + "</b>"


# EVENT HANDLERS
async def get_type(e):
    if e.file is None and e.media is None and e.photo is None:
        mtype = "text"
    else:
        mtype = "file"
    return mtype
