import time
import random
import telebot
from telebot.types import Message

users = {}


shrifts1 = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890",
"ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ１２３４５６７８９０")
shrifts2 = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890",
"𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘")
shrifts3 = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890",
"𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘")
shrifts4 = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890",
"𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘")
shrifts5 = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890",
"𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵𝟬")
shrifts6 = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890",
"🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩➊➋➌➍➎➏➐➑➒⓿")
shrifts7 = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890",
"🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘")
shrifts8 = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890",
"ꓯꓭↃꓷƎℲ⅁ɥıᒋꓘ⅂WuOꓒÒꓤSꓕꓵ𐌡MX⅄ZɐqɔpǝɟƃɥıɾʞןɯuodbɹsʇnʌʍxʎzƖ↊↋Һꞔ9∠860")
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789qwertyuiopasdfghjklzxcvbnm"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
bot = telebot.TeleBot("7425642007:AAGoPFp2HRfaIJ144E48EgvV4rF7LWcveRs")

@bot.message_handler(commands=["start"])
def start_cmd(message:Message):
    bot.send_message(message.chat.id,"и тебе привет")


@bot.message_handler(commands=["about"])
def about_cmd(message:Message):
    bot.send_message(message.chat.id,"Этот бот создан Габриэлем:)")

@bot.message_handler(commands=["passwordgenerator"])
def password(message:Message):
    bot.send_message(message.chat.id,f"my random password: {gen_pass(10)}")

@bot.message_handler(commands=["randomnumber"])
def rn_cmd(message:Message):
    bot.send_message(message.chat.id,f"my random number: {random.randint(1,6)}")


@bot.message_handler(commands=["coin"])
def coin_cmd(message:Message):
    coin = random.randint(1,2)
    if coin == 1:
        bot.send_message(message.chat.id,f"орел👍😶")
    else:
        bot.send_message(message.chat.id,f"решка👍😶")

@bot.message_handler(commands=["spam"])
def spam_cmd(message:Message):
    for _ in range(0,20):
        bot.send_message(message.chat.id,f"spaming")

@bot.message_handler(commands=["time"])
def time_cmd(message:Message):
    bot.send_message(message.chat.id,f"your zone time:{time.asctime()}")

@bot.message_handler(commands=["userinfo"])
def super_cmd(message:Message):
    user = message.from_user
    reg_info = users.get(message.chat.id)
    user_info = (f"👤 User Info:\n"
                    f"🆔 ID: {user.id}\n"
                    f"👤 Name: {user.first_name} {user.last_name or ''}\n"
                    f"📛 Username: @{user.username if user.username else 'None'}\n"
                    f"🌐 Language: {user.language_code}\n"
                    f"🤖 Is Bot: {user.is_bot}")
    if reg_info:
        user_info += f"🌆 City: {reg_info.get('city')}\n" + f"🟩 Color: {reg_info.get('fcolor')}\n" + f"9️⃣ Age: {reg_info.get('old')}"

    bot.send_message(message.chat.id,f"user info:{user_info}")
    
@bot.message_handler(commands=["register"])
def register_cmd(message:Message):
    bot.send_message(message.chat.id,"where you live?")
    bot.register_next_step_handler(message,getcity)

def getcity(message:Message):
    city = message.text
    bot.send_message(message.chat.id,f"hello {message.from_user.first_name} and you live in {city}")
    bot.send_message(message.chat.id,f"what is your age")
    bot.register_next_step_handler(message,getold,city)

def getold(message:Message,city):
    old = message.text
    bot.send_message(message.chat.id,f"your old: {old}")
    bot.send_message(message.chat.id,f"what is your favorite color")
    bot.register_next_step_handler(message,getfcolor,city,old)

def getfcolor(message:Message,city,old):
    fcolor = message.text
    bot.send_message(message.chat.id,f"{message.from_user.first_name.lower()} live in {city} and your age: {old} and your favorite color is {fcolor}")
    users[message.chat.id] = {
        'city': city,
        'fcolor': fcolor,
        'old':old
    }

@bot.message_handler(commands=["shrifts"])
def shrifts_cmd(message:Message):
    bot.register_next_step_handler(message,shrifts_cmd1)
def shrifts_cmd1(message:Message):
    bot.send_message(message.chat.id,f"{message.text.translate(shrifts1)}\n {message.text.translate(shrifts2)}\n {message.text.translate(shrifts3)}\n {message.text.translate(shrifts4)}\n {message.text.translate(shrifts5)}\n {message.text.translate(shrifts6)}\n {message.text.translate(shrifts7)}\n {message.text.translate(shrifts8)}\n")
    
@bot.message_handler(commands=['echo'])
def send_welcome(message:Message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message:Message):
    bot.reply_to(message, message.text)








bot.infinity_polling()
