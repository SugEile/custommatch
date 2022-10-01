import asyncio
import discord
import selectMap
import decideTeam

# 自分のBotのアクセストークン
TOKEN = 'aaaaa'

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
            # マップ選択メソッドを呼び出す
            map = selectMap.selectMap
            await message.channel.send(map + 'が選ばれました。')

        # コマンド：/team
        if message.content == '/team':
            await channel.send('参加するメンバーを半角カンマ区切り(,)で入力してください。 例: メンバー1,メンバー2,メンバー3')
            # 入力待ち
            try:
                msg = await client.wait_for('message', timeout = 600)
            except asyncio.TimeoutError:
                await channel.send('入力タイムアウトエラーです。再度最初から操作を行ってください。')
            
            # チーム決めメソッドを呼び出す
            team = decideTeam.decideTeam(msg)
            await message.channel.send('')
            
        


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
