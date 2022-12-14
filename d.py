from pymongo import MongoClient
from c import *

myclient = MongoClient(DB_URI)
db = myclient['mydb']
apiDB = db['api']


async def info_taker(chat):
    data = apiDB.find_one({"chat": chat})
    if data is None:
        return False, False
    print(data)
    api = data['api']

    stype = int(data["type"])
    return api, stype

from f import *
start_message = """<b>
Hey There, {}
๐ I Can Convert Link To ShortLink
๐ฌ Send Me Any Message With Links
๐ I Will Shorten All Links In It 
๐ Convert to <a href="https://metaurls.in/member/tools/bookmarklet">MetaUrls</a>
ยฉ๏ธPowered By @MetaUrlsOfficial 
</b>"""

start_button = [[Button.url("Join Channel โฅ๏ธ", "t.me/MetaUrlsOfficial"), Button.inline("About Bot ๐ค", "abt")],
                [Button.inline("Connect To Shortner ๐", 'api')]]

api_message = """
<b> Click the button Connect To:</b>
"""
api_button = [Button.url("MetaUrls.in", "https://metaurls.in/member/tools/bookmarklet")]

about_text = """<b>
๐ค Name :  MetaUrls.in Link Convertor
๐  Language : Python3
๐ Library     : Telethon
๐ง๐ปโ๐ป Developer : @MetaUrls_owner
ยฉ๏ธPowered By @MetaUrlsOfficial
</b>"""
async def api_logger(chat, api, stype):
    data = apiDB.find_one({"chat": chat})

    if data is None:
        apiDB.insert_one({"chat": chat, "api": api, "type": stype})
    else:
        apiDB.delete_one(data)
        apiDB.insert_one({"chat": chat, "api": api, "type": stype})
