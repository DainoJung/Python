import os
from dotenv import load_dotenv
load_dotenv()
import discord
import asyncio
import schedule
from discord.ext import commands, tasks
from datetime import datetime, timedelta
import time

# setup
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# discord 설정
token = os.getenv("DISCORD_BOT_KEY")
channel_id = int(os.getenv("CHANER_ID"))
global_decision = ""
global_message = ""

@bot.event
async def on_ready():
    print("봇이 온라인으로 전환되었습니다.")
    make_decision_and_execute()  # 봇이 준비되었을 때 작업 시작

@tasks.loop(hours=1)
async def create_thread(message, decision):
    now = datetime.now()
    global global_decision, global_message

    channel = bot.get_channel(channel_id)
    if channel:
        thread_name = now.strftime('%Y-%m-%d %H:%M') + f"{decision} 결정!"
        thread = await channel.create_thread(
            name=thread_name,
            auto_archive_duration=1440  # 1시간 후 자동 아카이브
        )
        
        thread_link = thread.jump_url  # 생성된 쓰레드의 링크
        
        await thread.send(message)
        await channel.send(f"{now.strftime('%m')}월 {now.strftime('%d')}일 {now.strftime('%H')}시 API 업데이트 성공!\n{thread_link}")
        
# 봇 구동
bot.run(token)

async def make_decision_and_execute():
    print("Making decision and executing...")
    global global_decision, global_message
    global_decision = "왕"
    global_message = "KING"
    try:
        asyncio.create_task(create_thread())
    except Exception as e:
        print(f"Failed to parse the advice as JSON: {e}")

if __name__ == "__main__":
    schedule.every().hour.at(':37').do(make_decision_and_execute)
    schedule.every().hour.at(':53').do(make_decision_and_execute)

    while True:
        schedule.run_pending()
        time.sleep(1)