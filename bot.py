import telebot
from telebot import types

# ضع التوكن الخاص بك هنا
API_TOKEN = '8777007515:AAG6bzq6ha1OPo19zcABu2ydaz5dbMBlsqE'

bot = telebot.TeleBot(API_TOKEN)

# رابط الموقع الذي قمت برفعه (يجب أن يكون https)
# ملاحظة: قم بتغيير هذا الرابط بعد رفع ملف index.html إلى استضافة
WEB_APP_URL = "https://your-hosting-url.com/index.html" 

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # إضافة زر لفتح الويب آب
    web_app = types.WebAppInfo(WEB_APP_URL)
    button = types.KeyboardButton(text="فتح دليل الأوامر 🤖", web_app=web_app)
    markup.add(button)
    
    welcome_text = (
        f"مرحباً بك يا {message.from_user.first_name} في بوت تون! 🌟\n\n"
        "يمكنك الآن استخدام دليل الأوامر الذكي لإدارة مجموعتك بسهولة.\n"
        "اضغط على الزر بالأسفل لفتح القائمة."
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    # استقبال الأمر المرسل من الموقع
    command_text = message.web_app_data.data
    
    # الرد على المستخدم لتأكيد استلام الأمر
    bot.reply_to(message, f"✅ جاري تنفيذ الأمر: **{command_text}**")
    
    # هنا يمكنك إضافة المنطق الخاص ببوتك لتنفيذ الأمر فعلياً
    # مثال: if command_text == "قفل الروابط": ...

print("البوت يعمل الآن... اضغط Ctrl+C للإيقاف")
bot.infinity_polling()