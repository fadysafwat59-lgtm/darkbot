import urllib.request, urllib.parse, os, random
TOKEN = os.environ["BOT_TOKEN"]
TARGET = "@Dark_Stoem"
POSTS = ["🔥 بوت WEKA بلس مجانا 👇 @Dark_Stoem", "💎 شرح التفعيل في @Dark_Stoem", "🚀 اقوي بوت 2026 في @Dark_Stoem"]
text = random.choice(POSTS)
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = urllib.parse.urlencode({"chat_id": TARGET, "text": text}).encode()
urllib.request.urlopen(url, data)
