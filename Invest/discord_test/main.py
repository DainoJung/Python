import os
from dotenv import load_dotenv
load_dotenv()
import discord
import asyncio
from discord.ext import commands, tasks
from datetime import datetime, time, timedelta

# setup
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# discord 설정
token = os.getenv("DISCORD_BOT_KEY")
channel_id = int(os.getenv("CHANER_ID"))
last_message_content ='스레드 테스트'

@bot.event
async def on_ready():
    print("봇이 온라인으로 전환되었습니다.")
    create_thread.start('잭팍', '성공')  # 봇이 준비되었을 때 작업 시작

@tasks.loop(hours=1)
async def create_thread(message, decision):
    now = datetime.now()

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