import urllib.request, urllib.parse, os, random

TOKEN = os.environ["BOT_TOKEN"]
TARGET = "@Dark_Stoem"

POSTS = [
"""👑 weka مش اي بروموكود وخلاص.. ده
الكود ده معمول للناس التقيلة بس
💥 بونص 200% على اول ايداع
💥 سحب سريع بدون ما يطلبوا منك ورق كتير
💥 دعم خاص لما تكلمهم قولهم انك تبع كود weka123 سرعة
💥 مكافآت اسبوعية بتنزلك انت بس
من اول يوم VIP فيه اكواد كتير.. بس كود واحد بيخليك
جربه وشوف الفرق بنفسك - weka123
👇 قناتنا:
https://t.me/Dark_Stoem""",

"""🔥 ليه تسجل عادي وانت ممكن تسجل مميز؟
سجل بالبروموكود weka123
هتاخد ضعف رصيدك + عروض مش بتظهر لاي حد
https://t.me/Dark_Stoem""",

"""💣 بتسجل من غير كود؟ انت بترمي فلوسك
الكود الرسمي بتاعنا weka123
بيضاعف رصيدك 3 اضعاف
https://t.me/Dark_Stoem""",

"""🚀 عايز تبدأ بـ 5000 بدل 2500؟
اكتب وانت بتسجل weka123
https://t.me/Dark_Stoem"""
]

msg = random.choice(POSTS)
data = urllib.parse.urlencode({"chat_id": TARGET, "text": msg}).encode()
urllib.request.urlopen(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data=data)
