#--coding:utf8;--
#qpy:3
#qpy:console

#imports
import json, requests, urllib, os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    art = urllib.parse.quote(input('Artist: '))
    mus = urllib.parse.quote(input('Song: '))

    url = f"http://api.vagalume.com.br/search.php?apikey=660a4395f992ff67786584e238f501aa&art={art}&mus={mus}"

    response = requests.get(url)

    data = json.loads(response.text)
    
    if data["type"] == "notfound":
        input('Artist not found')
    elif data["type"] == "song_notfound":
        input('Song not found.')
    else:
        versao = int(input('Choose:\n0. Original\n1. Translated in Portuguese'))
        song = data["mus"][0]
        version = ('Original','Translated')[versao == 1]
        liryc = (song["text"], song['translate'][0]['text']) [versao == 1]
        artist = data["art"]["name"]
        music = song["name"]
        print(f'''
------------------------------
  ARTIST: {artist}\n
  SONG: {music}\n
  VERSION: {version}\n
  LYRIC:\n
------------------------------
{liryc}
        	''')
        	
        print(('-'*10) + '\n')
        input('see more...')
