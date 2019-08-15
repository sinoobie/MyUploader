import requests,argparse,click,os

os.system('clear')
print("""
	#####################
	# PASTEBIN UPLOADER #
	#         BY        #
	#     KANG-NEWBIE   #
	#####################
""")

parser = argparse.ArgumentParser()
parser.add_argument('--up')
parser.add_argument('-f','--file', help='Path to file (lokasi filenya)', required=True)
args = vars(parser.parse_args())

dev_key="2bc4f0b150bcd8abc2eb08851b558299"
user_key="" #input your user key to upload file in your account
paste_code=open(args['file'],'r').read()
paste_format=input("[?] format file: ")
paste_name=input("[?] paste name: ")

print("\n[!] Uploading your file")
req=requests.post('https://pastebin.com/api/api_post.php',data={'api_paste_format':paste_format,'api_option':'paste','api_user_key':user_key,'api_paste_private':'0','api_paste_name':paste_name,'api_paste_expire_date':'N','api_dev_key':dev_key,'api_paste_code':paste_code})
print(f"[Result] {req.text}")
ans=input("[?] do you want open link on browser (y/n) ")
if ans.lower() == 'y':
	click.launch(req.text)