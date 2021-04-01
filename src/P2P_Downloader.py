# client.py
import socket    
from datetime import datetime
while True:
    
    
    
    s = socket.socket()            #socket yarattık
    host = input("sender local ip:")     # göndericinin landaki ipsini istedik
    port = 65000                    

    s.connect((host, port))#göndericiye bağlantı açtık
    filename=input('Name:')#indirilecek dosyanın adını girdik
    s.send(filename.encode())#dosya ismini byte a çevirip göndericiye gönderdik


    with open(filename, 'wb') as f: #local directoryde girilen dosya ismi ile bir dosya oluşturduk
        print ('file opened')
        while True:
            
            data = s.recv(1024)#göndericiden datayı aldık 
            
            if not data:
                break
            # datayı açtığımız dosyaya yazdık
            f.write(data)

    f.close()#dosyayı kapadık
    print('Successfully get the file')
    s.close()#socketi kapadık
    dosya=open("DownloadLog.txt","a")#download logu için dosya açtık
    now = datetime.now()#şu anki zamanı aldık
    timeStamp=now.strftime("%m/%d/%Y, %H:%M:%S")#zaman verisinib stringer çevirdik
    dosya.write(timeStamp+filename+host+"\n")#gerekli bilgileri dosyaya yazdık
    dosya.close()#dosyayı kapadık

