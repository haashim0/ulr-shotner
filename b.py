from f import *
from a import *
from c import *
from e import *

DB_URI = os.environ.get("DB_URI")
client = TelegramClient('ShortUrlLink', APP_ID, API_HASH).start(
    bot_token=BOT_TOKEN)

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
<b>Which Shortner Do u Want to Connect To:</b>
"""
api_button = [Button.url("MetaUrls.in", "https://du-link.in/member/tools/bookmarklet"]

about_text = """<b>



🤖 Name :  Shorurllink Link Convertor

🔠 Language : Python3
📚 Library     : Telethon
🧑🏻‍💻 Developer : @MetaUrls_Owner

©️Powered By @MetaUrlsOfficial
</b>"""
