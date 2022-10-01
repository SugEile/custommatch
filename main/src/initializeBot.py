import discord
import selectMap

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'MTAyNTYxMzQ3NjMxNzY0Mjc1Mg.GO2jHd.m1SQRflNm655Lsl-oT8yKmwj6nLBg4LFLd4UFk'

# 接続に必要なオブジェクトを生成
client = discord.Client(intents = discord.Intents.all())

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

@client.event
async def on_message(message):
    if not message.author.bot:
        channel = client.get_channel('コマンドを受け付けるチャンネルのチャンネルID')

        # コマンド：/map
        if message.content == '/map':
            map = selectMap.selectMap
            await message.channel.send(map + 'が選ばれました。')

        # コマンド：/team
        if message.content == '/team':
            await message.channel.send('')
        


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
