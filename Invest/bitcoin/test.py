# import discord
# from discord.ext import tasks, commands
# from datetime import datetime, time, timedelta
# import asyncio
# import os

# # 봇 설정
# intents = discord.Intents.default()
# intents.messages = True
# bot = commands.Bot(command_prefix='!', intents=intents)

# # 메시지 저장 변수
# last_message_content = "기본 메시지"

# # 채널 ID 설정
# channel_id = 1137952406517317713

# @bot.event
# async def on_ready():
#     print("봇이 온라인으로 전환되었습니다.")
#     create_thread.start()

# @bot.event
# async def on_message(message):
#     global last_message_content
#     if message.author == bot.user:
#         return

#     if message.channel.id == channel_id:
#         last_message_content = message.content
#     await bot.process_commands(message)

# @tasks.loop(hours=1)
# async def create_thread():
#     now = datetime.now()

#     channel = bot.get_channel(channel_id)
#     if channel:
#         thread_name = now.strftime('%Y-%m-%d %H:%M') + " 스레드"
#         thread = await channel.create_thread(
#             name=thread_name,
#             auto_archive_duration=60  # 1시간 후 자동 아카이브
#         )

#         await thread.send(f"{last_message_content}")

# # 환경 변수에서 DISCORD_BOT_TOKEN을 가져와서 봇을 실행합니다.
# bot.run(os.getenv("DISCORD_BOT_TOKEN"))
