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
🔀 I Can Convert Link To ShortLink
💬 Send Me Any Message With Links
🔗 I Will Shorten All Links In It 
🔂 Convert to <a href="https://metaurls.in/member/tools/bookmarklet">MetaUrls</a>
©️Powered By @MetaUrlsOfficial 
</b>"""

start_button = [[Button.url("Join Channel ♥️", "t.me/MetaUrlsOfficial"), Button.inline("About Bot 🤖", "abt")],
                [Button.inline("Connect To Shortner 🔗", 'api')]]

api_message = """
<b> Click the button Connect To:</b>
"""
api_button = [Button.url("MetaUrls.in", "https://metaurls.in/member/tools/bookmarklet")]

about_text = """<b>
🤖 Name :  MetaUrls.in Link Convertor
🔠 Language : Python3
📚 Library     : Telethon
🧑🏻‍💻 Developer : @MetaUrls_owner
©️Powered By @MetaUrlsOfficial
</b>"""
async def api_logger(chat, api, stype):
    data = apiDB.find_one({"chat": chat})

    if data is None:
        apiDB.insert_one({"chat": chat, "api": api, "type": stype})
    else:
        apiDB.delete_one(data)
        apiDB.insert_one({"chat": chat, "api": api, "type": stype})
