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
