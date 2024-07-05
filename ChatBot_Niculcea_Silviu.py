import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

API_TOKEN = "6767465605:AAFiX1kcFbCTKzfuZdPwzomPUdfe9qQzNuY"


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! My name is SilviuPpBot. Type /help to see the list of available commands.")

async def help_command(update: Update, context: CallbackContext) -> None:
    help_text = (
        "Commands:\n"
        "/start\n"
        "/info\n"
        "/help\n"
        
        "/temperature - Temperature in Bucharest"
    )
    await update.message.reply_text(help_text)

async def info(update: Update, context: CallbackContext) -> None:
    bot_info = (
        f"Bot Name: {context.bot.name}\n"
        f"Username: {context.bot.username}\n"
        f"ID: {context.bot.id}"
    )
    await update.message.reply_text(bot_info)

async def get_temperature(update: Update, context: CallbackContext) -> None:
    city = "Bucharest"
    url = f"http://wttr.in/{city.replace(' ', '+')}?format=%t"

    try:
        response = requests.get(url)
        response.raise_for_status()  
        temperature = response.text.strip()
        await update.message.reply_text(f"The temperature in {city} is {temperature}.")
    except requests.RequestException:
        await update.message.reply_text("Sorry, unavailable the temperature at the moment.")

def main() -> None:
 
    application = Application.builder().token(API_TOKEN).build()

    application.add_handler(CommandHandler("temperature", get_temperature))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("help", help_command))
   
    application.run_polling()

if __name__ == '__main__':
    main()

