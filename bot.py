from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "ВСТАВЬ_СЮДА_ТОКЕН_ОТ_BOTFATHER"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("на месте")


async def promo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("нету")


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("promo", promo))
    app.run_polling()


if __name__ == "__main__":
    main()
