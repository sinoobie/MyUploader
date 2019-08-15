import requests,sys,argparse,click,os
from bs4 import BeautifulSoup as BS

os.system('clear')
class Main:
	def __init__(self):
		self.link='https://sfile.mobi/guest.php'

	def upload(self):
		print("\n[!] Uploading your files")
		try:
			_try=open(args['file'],'r').read()
			files=open(args['file'],'r')
		except:
			files=open(args['file'],'rb')
		req=requests.post(self.link,data={'cat':'4'},files={'file1':files},headers={'x-requested-with':'XMLHttpRequest'})
		bs=BS(req.text,'html.parser')
		if 'error' in req.text:
			er=bs.find('div',{'class':'error'})
			print(f"[Err] {er.text[:-7]}")
		else:
			su=bs.find('input')
			print(f"[OK] URL: {su['value']}")
			ans=input("[?] do you want open link on browser (y/n) ")
			if ans.lower() == 'y':
				click.launch(su['value'])

def _help():
	global args
	parser = argparse.ArgumentParser()
	parser.add_argument('--up')
	parser.add_argument('-f','--file', help='Path to file (lokasi filenya)', required=True)
	args = vars(parser.parse_args())

print("""
`````.:::///+osyyyyyyyyyysoo++//:-.`````
`````.-:/+yyhhhhhhhhhhhhhhhhyyo/:-.`````
``````/shhhhhhhhhhhhhhhhhhhhhhhhs/``````
````-yhhhhhhhhhhhhhhhhhhhhhhhhhhhhy-````
.`-/hhhhhhhhhhhhs/----/shhhhhhhhhhhh/.`.
-:ohhhhhhhhhhhhdo-    -odhhhhhhhhhhhho:.
-oyhhhhhhhhhhhhdo-    -odhhhhhhhhhhhhyo-
+yhhhhhhhhhhs/-:-`    `.:-:ohhhhhhhhhhy+
shhhhhhhhhhhhs/`         :shhhhhhhhhhhhs
yhhhhhhhhhhhhddo.      .+ddhhhhhhhhhhhhy
yhhhhhhs/---..-hh+.  .+yh:...--/shhhhhhy
shhhhhho- .+ssoyhhs::shhyoss+. .ohhhhhhy
+yhhhhho- .shhhhhhhhhhhhhhhhy- .ohhhhhy+
:oyhhhho- .shyyyyyyyyyyyyyyhs- .ohhhhhs-
.:ohhhho- `..................` .ohhhhs/.
.`./hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh+-`.
````-yhhhhhhhhhhhhhhhhhhhhhhhhhhhhy:```.
`````.+shhhhhhhhhhhhhhhhhhhhhhhhs+.`````
`````.:/+oyyhhhhhhhhhhhhhhhhyyo/:-.`````
`````.:////+oosyyyyyhhyyyss+//::::.`````
""")
_help()
try:
	run=Main()
	run.upload()
except Exceptiona as Err:
	print("[Err] %s"%(Err))