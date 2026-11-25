
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔗 دریافت لینک ساب", callback_data="get_sub")],
        [InlineKeyboardButton("📡 وضعیت منابع", callback_data="status")],
        [InlineKeyboardButton("ℹ️ راهنما", callback_data="help")],
    ]

    await update.message.reply_text(
        "سلام! 👋 به V2SubFinder خوش آمدی.\n\n"
        "اینجا می‌توانی لینک‌های اشتراک رایگان VPN را پیدا کنی.\n\n"
        "یکی از گزینه‌ها را انتخاب کن:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "get_sub":
        message = "⏳ بخش دریافت ساب در حال آماده‌سازی است."
    elif query.data == "status":
        message = "📡 اتصال به منابع هنوز راه‌اندازی نشده است."
    else:
        message = "برای دریافت لینک، گزینه دریافت لینک ساب را انتخاب کن."

    await query.message.reply_text(message)


def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN تنظیم نشده است")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    app.run_polling()


if __name__ == "__main__":
    main()
