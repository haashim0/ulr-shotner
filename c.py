import os

APP_ID = os.environ.get("APP_ID", "14505719")
API_HASH = os.environ.get("API_HASH", "620f0a2aa2cd1474a4953619b3e3643d")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5669306246:AAFlikdRsxxLFdYLgelQyqb0TklW_c6zWX0")
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Haashim:Haashim@mfile0.t9hxg.mongodb.net/?retryWrites=true&w=majority")

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
