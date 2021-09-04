import os
import telebot


bot = telebot.TeleBot("")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm VndGroup Chat Bot")

PM_START_TEXT = """
𝙃𝙚𝙡𝙡𝙤 𝙩𝙝𝙚𝙧𝙚, 𝙄'𝙢 [VndGroup](t.me/vndgroupbotchannle) 🔥
𝙄'𝙢 𝙖 𝙋𝙤𝙬𝙚𝙧𝙛𝙪𝙡 𝙜𝙧𝙤𝙪𝙥 𝙢𝙖𝙣𝙖𝙜𝙚𝙧 𝙗𝙤𝙩 𝙒𝙞𝙩𝙝 𝘾𝙤𝙤𝙡 𝙈𝙤𝙙𝙪𝙡𝙚𝙨. 𝙈𝙖𝙙𝙚 𝙗𝙮 [Team VndGroup](t.me/vndgroupbotchannle)
𝙃𝙞𝙩 /help 𝙩𝙤 𝙛𝙞𝙣𝙙 𝙢𝙮 𝙡𝙞𝙨𝙩 𝙤𝙛 𝙖𝙫𝙖𝙞𝙡𝙖𝙗𝙡𝙚 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨 🕹
 
"""

buttons = [
    [
        InlineKeyboardButton(text="📌ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="https://t.me/vndgroupbotchannle"),
        InlineKeyboardButton(text="🖲 ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="https://t.me/vndgroupbotchannle"),
    ],
    [
        InlineKeyboardButton(text="📜 owner", url="https://t.me/Venuja_Sadew"),
        InlineKeyboardButton(text="❔ ʜᴇʟᴘ", url="https://t.me/vndgroupbotchannle"),
    ],
    [
        InlineKeyboardButton(
            text="➕ ᴀᴅᴅ VndGroup Bot ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url="t.me/TheAnkiVectorbot?startgroup=true"
        ),
    ],
]

ANKIVECTOR_IMG = "https://telegra.ph/file/75579c20520fc79f5b68d.jpg"

HELP_STRINGS = f"""
*Main Commands :* [🤖](https://telegra.ph/file/e10a45d0433a1ab6fed7b.jpg)
✪ /start: Starts me! You've probably already used this.
✪ /help: Click this, I'll let you know about myself!
✪ /donate: You can support my creater using this command.
✪ /settings: 
   ✪ in PM: will send you your settings for all supported modules.
   ✪ in a Group: will redirect you to pm, with all that chat's settings.
""".format(
    dispatcher.bot.first_name,
    "" if not ALLOW_EXCL else "\nAll commands can either be used with / or !.\n",
)

@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "")



bot.polling()