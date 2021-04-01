import socket  
from datetime import datetime
while True:
   port = 65000                    
   s = socket.socket()             # socket yarattık
   host = ''     # local makine bilgisini aldık
   s.bind((host, port))            # porta bağlandık
   s.listen(10)                     #bağlantı dinliyoruz 

   print ('Server listening....')


   conn, addr = s.accept()     # indiriciden gelen bağlantıyı onayladık
   print ('Got connection from', addr)#indirici bilgilerni ekrana yazdık
   filename = conn.recv(1024)#gelen dosya ismini aldık
   filename.decode("utf-8","ignore")#dosya ismini utf-8 e çevirdik gereksiz byteları ignore ettik

     
         
   f = open(filename,'rb')
   l = f.read(1024)
   while (l):
      conn.send(l)
         
      l = f.read(1024)
   f.close()
   #dosyayı 1024 lük parçalara bölüp gönderdik

   print('Done sending')
      
   conn.close()#bağlantıyı kapadık
   s.close()#socketi kapadık
   dosya=open("ServerLog.txt","a")#server log için dosya açtık
   now=datetime.now()
   timeStamp=now.strftime("%m/%d/%Y, %H:%M:%S")
   newFileName=str(filename, 'utf-8')
   newAdress =  ''.join(str(addr))
   #gerekli bilgileri stringe çeviridk
   dosya.write(timeStamp+newFileName+newAdress+"\n")#bilgileri log soyasına yazdık
   dosya.close()#dosyayı kapadık


