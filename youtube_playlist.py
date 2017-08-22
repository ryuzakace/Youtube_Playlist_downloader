import requests, sys, pyperclip, os
from bs4 import BeautifulSoup


#data-list-title     playlist-header-content

url = pyperclip.paste()

req = requests.get(url)

try:
    req.raise_for_status()
except Exception as exc:
    print('There was a problem:',exc)

soup = BeautifulSoup(req.text,"html.parser")

titl =[]

for divs in soup.findAll('div',attrs={'class':'playlist-header-content'}):
    if(divs.get('data-list-title')):
        titl.append(divs.get('data-list-title'))
lyr = str(titl[0]).replace(' ','_')
fname = lyr+'.txt'



i=soup.findAll('li')




dir_path = os.path.dirname(os.path.realpath(__file__))
folder = os.path.abspath(dir_path)

nowf = os.path.join(folder,fname)

indexx = 1

newfile = open(nowf,'w')
newfile.close()

fop = open(fname,'w')
fop.write('\t\t\t'+lyr.replace('_',' ')+'\n')
for o in i:
    if(o.get('data-video-title')):
        fop.write(str(indexx) +' '+ str(o.get('data-video-title')) + '\n')
        indexx = indexx + 1

fop.close()
