import requests,os,json,argparse,click

os.system('clear')
class Main:
	def __init__(self):
		self.link='https://openload.cc/api/upload'

	def up(self):
		print("[!] Uploading your file")
		try:
			_try=open(args['file'],'r').read()
			files=open(args['file'],'r')
		except:
			files=open(args['file'],'rb')
		req=requests.post(self.link,files={'file':files},headers={'x-requested-with':'XMLHttpRequest'})
		jsn=json.loads(req.text)
		if 'true' in req.text:
			print("[OK] Success")
			print("\n[URL]",jsn['data']['file']['url']['short'])
			print("[SIZE]",jsn['data']['file']['metadata']['size']['readable'])
			tanya=input("\n[?] do you want open link on browser (y/n) ")
			if tanya.lower() == 'y':
				click.launch(jsn['data']['file']['url']['short'])
		else:
			print("[!!]",jsn['error']['code']+":",jsn['error']['message'])
		files.close()

def _help():
	global args
	parser = argparse.ArgumentParser()
	parser.add_argument('--up')
	parser.add_argument('-f','--file', help='Path to file (lokasi filenya)', required=True)
	args = vars(parser.parse_args())
#	print(args)

print("""%s
   `.-//////`         `+/:/://:`   
 `:+o++++++++:/-`   `:/++++++++/-` 
`+++o:..---++++s:.::////.....-////`
+++o/.      ---.-/+///-       .+///	%sOPENLOOAD UPLOADER%s
o++o-        `-/++//-`        -+///	%sBY: KANG-NEWBIE%s
o++o:.      -/+++:/+/:.       .+//+
`+o+++:...-/+++o: ./////..../+////`
 `:/+++++++++:/-`   .:/+++++++++-` 
    ``-////``         ``//:/-```   
%s    """%('\033[96m','\033[94m','\033[96m','\033[92m','\033[96m','\033[97m'))
_help()
try:
	run=Main()
	run.up()
except Exception as Err:
	print("ERR: %s"%(Err))