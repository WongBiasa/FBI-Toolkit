import os
import requests 
import json
import sys
import getpass
import hashlib

def baliho():
  print '[+]FBI Tookit'
  try:
    token =open('token.txt','r').read()
    r = requests.get('https://graph.facebook.com/me?/acces_token=' + token)
    a = json.loads(r.text)
    name = a['name']
    n.append(a['name'])

    print '''
                            ,--.
                           {    }
                           K,   }
                          /  `Y`
                     _   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /     -[FBI Toolkit]-
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~%%',
   (                     %  Y                          info
  {                      %% I                  -----------------------
 {      -                 %  `.                  Author   :WhoMHW
 |       ',                %  )                  Telegram :@Hedy2
 |        |   ,..__      __. Y                   Youtube  :CatatanNewbie
 |    .,_./  Y ' / ^Y   J   )|                   Team     :WongNdesoTeam
 \           |' /   |   |   ||                   Instagram:www.instagram.com/siapa_namasaya23/
  \          L_/    . _ (_,.'(                   Tanggal  :20210121
   \,   ,      ^^""' / |      )                  Versi    :0.02
     \_  \          /,L]     /
       '-_`-,       ` `   ./`
          `-(_            )
              ^^\..___,.--`'''

  except:
    print '''
      Informasi FacebooK[FBI]


                            ,--.
                           {    }
                           K,   }
                          /  `Y`
                     _   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /     -[FBI Toolkit]-
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~%%',
   (                     %  Y                          info
  {                      %% I                  -----------------------
 {      -                 %  `.                  Author   :WhoMHW
 |       ',                %  )                  Telegram :@Hedy2
 |        |   ,..__      __. Y                   Youtube  :CatatanNewbie
 |    .,_./  Y ' / ^Y   J   )|                   Team     :WongNdesoTeam
 \           |' /   |   |   ||                   Instagram:www.instagram.com/siapa_namasaya23/
  \          L_/    . _ (_,.'(                   Tanggal  :20210121
   \,   ,      ^^""' / |      )                  Versi    :0.02
     \_  \          /,L]     /
       '-_`-,       ` `   ./`
          `-(_            )
              ^^\..___,.--`


                 --[Telegram:@Hedy2]--
                 --[Email:mbiasa736@gmail.com]--

    
          '''


reload (sys)
sys.setdefaultencoding ( 'utf8' )
n = []

def main():
  print 
  print '\t\t[--FBI [Facebook Informasi] (Version 0.01)--]'
  print '\t\t[--Author   : WhoMHw            --]'
  print ''' 

Informasi FacebooK[FBI]


                            ,--.
                           {    }
                           K,   }
                          /  `Y`
                     _   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /     -[FBI Toolkit]-
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~%%',
   (                     %  Y                          info
  {                      %% I                  -----------------------
 {      -                 %  `.                  Author   :WhoMHW
 |       ',                %  )                  Telegram :@Hedy2
 |        |   ,..__      __. Y                   Youtube  :CatatanNewbie
 |    .,_./  Y ' / ^Y   J   )|                   Team     :WongNdesoTeam
 \           |' /   |   |   ||                   Instagram:www.instagram.com/siapa_namasaya23/
  \          L_/    . _ (_,.'(                   Tanggal  :20210121
   \,   ,      ^^""' / |      )                  Versi    :0.02
     \_  \          /,L]     /
       '-_`-,       ` `   ./`
          `-(_            )
              ^^\..___,.--`


                 --[Telegram:@Hedy2]--
                 --[Email:mbiasa736@gmail.com]--

    
    '''

def perintah():
  print '''\tPerintah          Catatan
       ___________        _________

       buka_nomor        Untuk Mengetahui nomor teman
       buka_id           Untuk Mengetahui id teman
       buka_email        Untuk Mengetahui email teman

       lihat_id          Untuk Melihat Id teman kamu
       lihat_email       Untuk Melihat Email teman kamu
       
       token             Untuk Membuat token
       cat_token         Untuk Mengetahui token anda
       nano_token        Untuk anda yang sudah mempunyai token

       help              Untuk Mengetahui keterangan tools
       exit              Untuk keluar
       clear             clear terminal

'''

try:
        import requests
except ImportError:
       print ''' 

TRacking Informasi FacebooK


                            ,--.
                           {    }
                           K,   }
                          /  `Y`
                     _   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /     -[FBI Toolkit]-
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~%%',
   (                     %  Y                          info
  {                      %% I                  -----------------------
 {      -                 %  `.                  Author   :WhoMHW
 |       ',                %  )                  Telegram :@Hedy2
 |        |   ,..__      __. Y                   Youtube  :CatatanNewbie
 |    .,_./  Y ' / ^Y   J   )|                   Team     :WongNdesoTeam
 \           |' /   |   |   ||                   Instagram:www.instagram.com/siapa_namasaya23/
  \          L_/    . _ (_,.'(                   Tanggal  :20210121
   \,   ,      ^^""' / |      )                  Versi    :0.02
     \_  \          /,L]     /
       '-_`-,       ` `   ./`
          `-(_            )
              ^^\..___,.--`

      [Kamu belum Install pip2 requests]'''
       sys.exit()

def hedy():
  cek = raw_input('FBI Toolkit>>')

  if cek == 'token':
    token()

  elif cek == 'nano_token':
    nano_token()

  elif cek == 'cat_token':
    cat_token()

  elif cek == 'buka_id':
    buka_id()

  elif cek == 'help':
    help()

  elif cek == 'clear':
    clear()

  elif cek == 'keterangan':
     keterangan()
   
  elif cek == 'buka_email':
    buka_email()

  elif cek == 'buka_nomor':
     buka_nomor()

  elif cek == 'exit':
    exit()

  elif cek == 'keluar':
    exit()
  
  elif cek == 'lihat_id':
    lihat_id()

  elif cek == 'lihat_email':
    nomor()

  elif cek == 'lihat_nomor':
    mail()

  else:
    print '[?]Perintah tidak ditemukan'
    print '[?]Jika tidak mengerti hubungi admin'
    hedy()

               

def exit():
  print '[*]Terimakasih telah menggunakan.!'
  sys.exit()

def clear():
  print '[?]Mencoba membersihkan layar'
  try:
    print '[*]clear terminal'
    os.system('clear')
    baliho()
    hedy()

  except:
    print '[?]Kamu memakai CMD'
    baliho()
    hedy()


def help():
  print '''
    +-------------------------------------------+
    |_________________Keterangan________________|
    | Tools ini mungkin tidak seratus persen    |
    |               Berhasil                    |
    +-------------------------------------------+
  '''
  baliho()
  hedy()

def keterangan():
  print '''
    +-------------------------------------------+
    |_________________Keterangan________________|
    | Tools ini mungkin tidak seratus persen    |
    |               Berhasil                    |
    +-------------------------------------------+'''
  baliho()
  hedy()


def buka_nomor():
  print '[*]Strating Token'

  try:
    token = open('token.txt','r').read()
    print '[+]Mendapatkan token'

  except IOError:
    print '[-]Gagal mendapatkan token'
    print '[-]Jika tidak mengerti hubungi admin'
    hedy()

  try:
    os.mkdir('hasil')

  except OSError:
    pass

  try:
    r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
    a = json.loads(r.text)

    out = open('_phone.txt','w' )

    for i in a['data']:
           x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
           z = json.loads

           try:
            out.write( z['mobile_phone'])

           except KeyError:
             pass


    out.close()
    print '[*]Sukses mengembail nomor teman'
    print '[*] Disave : _phone.txt'
    baliho()
    hedy()
          
  except KeyboardInterrupt:
      print '[!] Stopped' 

def buka_email():
  print '[*]Strating token'

  try:
    token = open('token.txt','r').read()
    print '[*]Mendapatkan token'

  except IOError:
    print '[-]Gagal mendapatkan Token'
    print '[-]Jika tidak mengerti hubungi admin'
    hedy()

  try:
    os.mkdir('hasil')

  except OSError:
    pass

  try:
    print '[*]Mencari Email teman'
    r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
    a = json.loads(r.text)

    out = open('_mail.txt','w')

    for i in a['data']:
            x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
            z = json.loads(x.text)

            try:
              out.write( z['name'] + ':' + z['email'])
            
            except KeyError:
              pass
            
 
    out.close
    print '[+]Sukses Mengambil email teman'
    print '[*] Disave : _mail.txt'
    sys.exit()

  except KeyboardInterrupt:
		  print '\r[!] Stopped'
		  hedy()

def buka_id():

  print '[*]Strating token'


  try:
    token = open('token.txt','r').read()
    print '[+]Mendapatkan token'

  except IOError:
    print '[-]Gagal mendapatkan token'
    print '[-]Jika tidak mengerti hubungi pembuat'
    hedy()

  try:
    os.mkdir('hasil')
  
  except OSError:
    pass

  try:
      r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
      a = json.loads(r.text)

      out = open('_id.txt','w')


      for i in a['data']:
			        out.write(i['name'] + ':' + i['id'])
		  
      out.close()
      print i['name'] + ':' + i['id']
      print '\r[*] sukses mengambil id teman'
		  
      print '[*] Disave : _id.txt'
      sys.exit()

  except KeyboardInterrupt:
		  print '\r[!] Stopped'
		  hedy()



def cat_token():
  try:
    wibi = open('token.txt','r').read()
    print '[*] Token Kamu !!\n\n' + wibi + '\n'

  except:
    print '[-]Anda belum login'
    print '[?]Hubungi admin jika tidak mengerti'
    hedy()

def lihat_id():
  try:
    id = open('_id.txt','r').read()
    print '[+]Mendapatkan ID'
    print '[*]ID temanmu.!!\n' + id + '\n'
    hedy() 

  except:
    print '[-]ID tidak ditemukan'
    print '[-]Jika tidak mengerti hubungi admin'
    hedy()
   
def nomor():
  try:
    nomor = open('_mail.txt','r').read()
    print '[*]Mendapatkan email'
    hedy()

  except:
    print '[-]Email tidak ditemukan'
    print '[-]Jika tidak mengerti hubungi admin'
    hedy()

def mail():
   try:
    nomor = open('_phone.txt','r').read()
    print '[*]Mendapatkan email'
    hedy()

   except:
    print '[-]Nomor tidak ditemukan'
    print '[-]Jika tidak mengerti hubungi admin'
    hedy()


def nano_token():
  print '[*]Jika tidak mengerti hubungi admin'

  try:
    print '[*]Masukkan token anda'
    token = raw_input('[?]Token:')
    teks = open('token.txt', 'w')
    teks.write(token)

  except:
    print '[-}Masukkan token'
    hedy()
        
def token():
	print '[*] login aku fb        ';id = raw_input('[?] Username : ');pwd = getpass.getpass('[?] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	x = hashlib.new('md5')
        x.update(sig)

	data.update({'sig':x.hexdigest()})
        get(data)

def get(data):
	print '[*] Membuat token'

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('token.txt','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] success memperoleh token'
		print '[*] Tokenmu tersimpan Di token.txt'
		exit()
	except KeyError:
		print '[!] Gagal mengambil token'
		print '[!] tolong cek nomor sama password'
		os.remove('token.txt')
		sys.exit()



main()
perintah()
hedy()
