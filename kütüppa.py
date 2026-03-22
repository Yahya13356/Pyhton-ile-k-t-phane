import time
from time import sleep
import webbrowser
import cv2
menü = """
    ----  🎉ÜVEYSİN KÜTÜPHANE UYGULAMSI ÇIKTI 1.0 VERSİON 😱🎉 ---
    1)kitap ekle 🎁
    2)kitap al 🛒
    3)kitapları göster👀
    Q)çıkış🚪
"""
liste = list()
def web(url:str):
    webbrowser.open(url,new=2)

def kitap_ekle(kitap:tuple,liste:list):
    liste.append(kitap)
    print("kitap başarılı şekilde eklendi")
    web(url="file:///C:/Users/uveys/OneDrive/Masa%C3%BCst%C3%BC/Yeni%20klas%C3%B6r%20(4)/Yeni%20klas%C3%B6r%20(6)/te%C5%9Fekk%C3%BCr.html")
    resim = cv2.imread('depositphotos_189561858-stock-illustration-cartoon-of-happy-smiling-man.jpg')
    cv2.imshow("pencere",resim)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def kontrol(kitap:tuple,liste:list):
    if kitap in liste:
        return True
    else:
        return False

def kitap_al(kitap:tuple,liste:list):
    if kontrol(kitap,liste):
        liste.remove(kitap)
        print("kitap artık sizin")
        web(url="file:///C:/Users/uveys/OneDrive/Masa%C3%BCst%C3%BC/Yeni%20klas%C3%B6r%20(4)/Yeni%20klas%C3%B6r%20(6)/okuyun.html")
        resim = cv2.imread('kitaplar.jpg')
        cv2.imshow("pencere", resim)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("bizde öyle bişey yok bacım")


def kitapları_göster(liste:list):
    for a in liste:
        print("kitabın adı: {}📖  kitabın yazarı {}🖊️".format(a[0],a[1]))

def çıkış():
    web(url="file:///C:/Users/uveys/OneDrive/Masa%C3%BCst%C3%BC/Yeni%20klas%C3%B6r%20(4)/Yeni%20klas%C3%B6r%20(6)/%C3%A7%C4%B1k%C4%B1%C5%9F.html")
    resim = cv2.imread('kedi.jpg')
    cv2.imshow("pencere", resim)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    quit()
while True:
    print(menü)
    secim = input("ne yapmak istersin?")
    if secim =="1":
        kitap_adı = input("kitabın ismi nedir dost: ")
        kitap_yazarı = input("ktiabın yazarı neydi ya of: ")
        kitap = (kitap_adı,kitap_yazarı)
        kitap_ekle(kitap,liste)
        sleep(1)
    elif secim =="2":
        kitap_adı = input("kitabın ismi nedir dost: ")
        kitap_yazarı = input("ktiabın yazarı neydi ya of: ")
        kitap = (kitap_adı, kitap_yazarı)
        kitap_al(kitap,liste)
    elif secim =="3":
        if liste==True:
            kitapları_göster(liste)
        else:
            print("elimizde kitap kalmadı ya🤲")
            sleep(1)
    elif secim =="Q" or secim =="q":
        çıkış()
    else:
        print("sayın abonemiz eksik veya yanlış tuşlama yaptınız")



