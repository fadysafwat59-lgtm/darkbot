import urllib.request, urllib.parse, os, random
TOKEN = os.environ["BOT_TOKEN"]
TARGET = "@Dark_Stoem"
POSTS = ["""👑 مش أي بروموكود وخلاص.. ده weka123
الكود ده معمول للناس التقيلة بس
💥 بونص 200% على اول ايداع
💥 سحب سريع بدون ما يطلبوا منك ورق كتير
💥 دعم خاص لما تكلمهم قولهم انك تبع كود weka123 هيخلصوك بسرعة
💥 مكافآت اسبوعية بتنزلك انت بس
فيه اكواد كتير.. بس كود واحد بيخليك VIP من اول يوم
weka123 - جربه وشوف الفرق بنفسك
👇 قناتنا:
https://t.me/Dark_Stoem""",
"""ليه تسجل عادي وانت ممكن تسجل مميز؟ 🔥
سجل بالبروموكود weka123
هتاخد ضعف رصيدك + عروض مش بتظهر لاي حد
الكود ده هو مفتاح الـ VIP 🔑
https://t.me/Dark_Stoem""",
"""جرب تسجل بدون كود.. هتاخد حساب عادي
جرب تسجل بـ weka123.. هتاخد حساب طاير 💸🚀
الفرق بينهم هو البونص والمميزات اللي هتخليك تلعب وانت مرتاح
الكود القوي بيتكلم عن نفسه
weka123"""]
text = random.choice(POSTS)
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = urllib.parse.urlencode({"chat_id": TARGET, "text": text}).encode()
urllib.request.urlopen(url, data)
