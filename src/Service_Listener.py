# -*- coding: utf-8 -*-
import socket
import time
import os
import pickle

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("10.255.255.255", 1))#kullanılmayan bir ip ye socketle bağlandık
IP = s.getsockname()[0]#bağlandığımız socketle yerel ip mizi öğrendik



name = input("Please enter your name: ")#kullanıcı admızı giriyoruz
name=name.upper()#adımızı büyük harfe çevirdik
name=name+" with IP adress "
bytesToSend = str.encode(name)#adımızı byte a çevirdik
bytesToSend2=str.encode(IP)#ip mizi byte a çevirdik



def repeatFunc():
    cwd=os.getcwd()#programı çalıştığı directory i aldık
    x=os.listdir(cwd)# x in içine directory deki dosyaları kaydettik
    newX=pickle.dumps(x)#directory deki dosyaların listesini byte a çevirdik
    newX=newX+bytesToSend+bytesToSend2    #diğer bilgileri üstüne ekleyerek son mesjaı oluşturduk
    client=socket.socket() # bir socket nesnesi oluşturuyoruz
    host="192.168.1.132" # bağlanacağımız server ın adresi adres(Not: herkes canlı yayın yapıyor ama bu canlı yayını sadece server olarak belirlenen makine alabiliyor tüm kullanıcılara gitmiyor maalesef)
    port=9000 # bağlanacağımız kapı
    client.connect((host,port)) # bağlantı yapılıyor
    print("Bağlantı yapıldı")
    client.send(newX) # mesaj gönderiyoruz
    
    
    time.sleep(60)#
    while True:
        repeatFunc()
    
repeatFunc()