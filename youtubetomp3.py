
from __future__ import unicode_literals
import youtube_dl, shutil
import requests, sys, pyperclip, os
from bs4 import BeautifulSoup

#url = "https://www.youtube.com/watch?v=foE1mO2yM04&list=RDfoE1mO2yM04#t=6"

what = int(input('''                Select one of the options:
                    1. Download single file
                    2. Entire Playlist\n'''))

url = pyperclip.paste()

req = requests.get(url)
print(url)
try:
    req.raise_for_status()
except Exception as exc:
    print('There was a problem:',exc)

youman = 'https://www.youtube.com'

dir_path = os.path.dirname(os.path.realpath(__file__))
folder = os.path.abspath(dir_path)
naya = os.path.join(folder,'ryuz_single')
if not os.path.exists(naya):
    os.makedirs(naya)
print(naya)
for tat,ti,fil in os.walk(folder):
    #print(fil)
    for gu in fil:
    #    print(gu)
        if(str(gu).endswith('.mp3')):
            print('mp3----',gu)
            #try-
            #shutil.move(os.path.join(folder,str(gu)), naya)

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

if(what == 1):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
else:

    print("Downloading the entire playlist")

    soup = BeautifulSoup(req.text,"html.parser")
    atgs = soup.find_all('a')


    for i in atgs:
        if(i.get('href')):
            dd = i.get('href')
            dx = dd[0:6]
            if(dx=='/watch'):
                dx = youman+dd
            #print(dx)
            #try-catch here-----~~~~
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([dx])
