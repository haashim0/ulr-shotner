import os

APP_ID = os.environ.get("APP_ID", "14505719")
API_HASH = os.environ.get("API_HASH", "620f0a2aa2cd1474a4953619b3e3643d")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5669306246:AAFlikdRsxxLFdYLgelQyqb0TklW_c6zWX0")
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Kd:Kd@cluster0.95kbq.mongodb.net/?retryWrites=true&w=majority")

from f import *
start_message = """<b>
Hey There, {}
🔀 I Can Convert Link To ShortLink
💬 Send Me Any Message With Links
🔗 I Will Shorten All Links In It 
🔂 Convert to <a href="https://shorturllink.in/member/tools/bookmarklet">ShortUrlLink</a> & <a href="https://playdisk.xyz/member/tools/bookmarklet">PlayDisk</a>

©️Powered By @A2z_tech
</b>"""

start_button = [[Button.url("Join Channel ♥️", "t.me/A2z_tech"), Button.inline("About Bot 🤖", "abt")],
                [Button.inline("Connect To Shortner 🔗", 'api')]]

api_message = """
<b>Which Shortner Do u Want to Connect To:</b>
"""
api_button = [[Button.url("Shorturllink.in", "https://shorturllink.in/member/tools/bookmarklet")],
              [Button.url("Playdisk.xyz", "https://playdisk.xyz/member/tools/bookmarklet")]]

about_text = """<b>



🤖 Name :  Shorurllink Link Convertor

🔠 Language : Python3
📚 Library     : Telethon
🧑🏻‍💻 Developer : @Ziko_0000

©️Powered By @A2z_tech
</b>"""
