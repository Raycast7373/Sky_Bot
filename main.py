from flask import Flask, redirect
import discord
import discord.ext
import subprocess
import os
import sys
BadID = 'NONE'
ClusterID = os.getenv('Cluster_ID')
DiscordToken = os.getenv('Discord_Token')
RevoltToken = os.getenv('Revolt_Token')

LOWID = '0'
HIGHID = '16'

print("ClusterID: ",ClusterID)
print("DiscordToken: ",DiscordToken)
print("RevoltToken: ",RevoltToken)

try:
    int(ClusterID)
    print("ID is a number!")
    IsClusterIDNum = 'TRUE'
    if LOWID <= ClusterID <= HIGHID:
        print("Number is Valid!")
        IDVALID = 'TRUE'
    else:
        print("Number isn't Valid!!! ERROR")
        IDVALID = 'FALSE'
except ValueError:
    print("Error! Invalid ID detected,ID is not a number! terminating...")
    IsClusterIDNum = 'FALSE'

#if ClusterID == BadID:
#    print("Error! Invalid ID detected, terminating...")
#    ERROR = 'TRUE'
#else:
#    print("No ClusterID error found! Starting...")
#    ERROR = 'FALSE'

app = Flask(__name__)
D1 = 'ClusterID: ' + ClusterID
D2 = '\nDiscordToken: ' + DiscordToken
D3 = '\nRevoltToken: ' + RevoltToken
D4 = '\nIsClusterIDNum: ' + IsClusterIDNum
D5 = '\nIDVALID: ' + IDVALID
T = [D1, D2, D3, D4, D5]
DATA = '\n'.join(T)
print(DATA)

@app.route('/')
def hello_world():
    return DATA


@app.route('/UPDATE/')
def UPDATE():
    subprocess.run(["bash", "/usr/src/app/src/update.sh"])
    return redirect("/")
    exit()


client = discord.AutoShardedClient(shard_count=1)
    
SHARD = 'Shard ' + ClusterID

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



activity = discord.Activity(type=discord.ActivityType.watching, name=SHARD)
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", activity=activity, status=discord.Status.idle)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('token')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

