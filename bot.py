import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import os
import random

# สร้างแอป Flask
app = Flask(__name__)

# กำหนดบอท
bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

# คำสั่ง !buy ที่จะให้บอทขาย Key
keys = ["KEY-001", "KEY-002", "KEY-003", "KEY-004"]  # กำหนด Key ที่จะขาย

@bot.command()
async def buy(ctx):
    if keys:
        purchased_key = random.choice(keys)
        keys.remove(purchased_key)
        await ctx.send(f"คุณได้รับ Key: {purchased_key}")
    else:
        await ctx.send("ไม่มี Key ให้ขายแล้ว")

# สร้าง Route สำหรับ Flask
@app.route('/')
def home():
    return "Server is running!"

# ฟังก์ชันสำหรับรัน Flask
def run():
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 10000)))

# ฟังก์ชันที่ใช้สำหรับให้ Flask ทำงานบน Thread
def server_on():
    t = Thread(target=run)
    t.start()

# ฟังก์ชันที่รันบอท Discord และ Flask
def start_bot():
    server_on()
    bot.run(os.getenv('DISCORD_TOKEN'))

if __name__ == "__main__":
    start_bot()
