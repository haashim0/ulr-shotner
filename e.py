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
back_button = [Button.inline("⏪ Back", "back")]
