
import requests,sys, os, shutil, sys

from bs4 import BeautifulSoup

url = "http://www.songlyrics.com"

artist = input("Enter the name of the artist - ")
song = input("Enter the song's name - ")

url = url + '/' + artist + '/' + song + '-lyrics/'

url = url.replace(' ','_')

req = requests.get(url)
#print(url)
try:
    req.raise_for_status()
except Exception:
    print('Check the spellings')

dir_path = os.path.dirname(os.path.realpath(__file__))
folder = os.path.abspath(dir_path)
naya = os.path.join(folder,'ryuz_lyrics')

if not os.path.exists(naya):
    os.makedirs(naya)

csong = str((song + '_by_' + artist + '.txt')).replace(" ",'_')

temp = os.path.join(folder,csong)

uu = open(temp,'w')
uu.close()

emma = open(csong,'w')



soup = BeautifulSoup(req.text, "html.parser")

i= soup.find('p',attrs={'id':'songLyricsDiv'}).getText()
emma.write(i)
emma.close()
shutil.move(temp, naya)
