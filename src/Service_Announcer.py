# -*- coding: utf-8 -*-
import socket# kütüphanemizi kullanmak üzere içeri aktarıyoruz
import os
import time
while (True):
    s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("10.255.255.255", 1))
    IP = s.getsockname()[0] #Local İpmizi IP değişkenine kaydettik
    server=socket.socket() # bir socket nesnesi oluşturuyoruz
    host=IP
    port=9000 # bağlantıyı kabul edeceğimiz port numarası 
    server.bind((host,port)) # bağlantıyı kuruyoruz
    server.listen(10) # 10 misafir dinlemek istediğimizi belirtiyoruz

    print("Bağlantı bekleniyor...")
    makine,bilgi=server.accept() # burada bir mesaj gönderen bekliyoruz ve bilgileri sol tarafa aktarıyoruz
    print("Bir bağlantı kabul edildi")
    # bilgi, mesajın geldiği makinenin bilgilerini tutar
    # makine değişkeni ise, mesaj gönderen adresi temsil eder. Bunu kullanarak geri mesaj göndeririz
    mesaj=makine.recv(1024) # gelen mesajı alıyoruz
    mesaj=mesaj.decode("utf-8", "ignore") # gelen mesajı utf-8 olarak decode edip ignore ile fazla bytelardan kurtuluyoruyz
    print(mesaj)#ekrana yazdırıyoruz
    
    
    

 
