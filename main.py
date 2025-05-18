import os
import discord
from discord.ext import commands
from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/discord-bot")
def discord_bot_status():
    return "Discord Bot is online!"

@app.route("/health")
def health_check():
    return "Health Check: OK", 200

def run_flask():
    app.run(host="0.0.0.0", port=5000)

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

cog_directories = [
    "cogs",
    "events"
]

for cog_dir in cog_directories:
    for filename in os.listdir(cog_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            extension = f"{cog_dir}.{filename[:-3]}"
            try:
                bot.load_extension(extension)
                print(f"✅ Loaded extension: {extension}")
            except Exception as e:
                print(f"❌ Failed to load extension {extension}: {e}")

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    bot.run(os.getenv("NEW_BOT_TOKEN"))
