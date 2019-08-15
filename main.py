import argparse,sys,os,shutil

#remove cache
try:
	shutil.rmtree("src/__pycache__")
except: pass

os.system('clear')
def example():
	print("""
Name Menu 	Description
-----------------------------
openload	max size:20GB & unlimited bandwidth
sfile		max size:100MB & can't upload audio
pastebin	maz size:Unknow & only for text file formats
""")
	print(f"Example: {sys.argv[0]} -f test.txt --up openload")

def help_():
	global args
	parser = argparse.ArgumentParser(description=example())
	parser.add_argument('-f','--file', help='path to File',required=True)
	parser.add_argument('--up',dest='name menu', help='uploading your file',required=True)
	args = vars(parser.parse_args())

print("""
   _   _   _   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
 ( M ( Y ( U ( P ( L ( O ( A ( D ( E ( R )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
                  / \ / \                 
                 ( B ( Y )                
   _   _   _   _  \_/ \_/  _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
 ( K ( A ( N ( G ( N ( E ( W ( B ( I ( E )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
  """)
help_()
try:
	if args['name menu'].lower() == 'sfile':
		import src.upsfile
	elif args['name menu'].lower() == 'openload':
		import src.upload
	elif args['name menu'].lower() == 'pastebin':
		import src.upaste
	else:
		example()
except: pass