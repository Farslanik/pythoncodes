import random
import sys

puanlistesi = []

hareketlistesi =[]
ateşlistesi = []
satır = 9
sütun = 14
hareketpuanı = 0
kazanılanpuan = 0

puanlistesi = []

def yaratıküretme():
    global toplamcanavar
    while True:
        try :
            while True :
                canavarkontrol = 0
                print("Kaç yaratıkla mücadele etmek istersiniz")
                toplamcanavar = int(input())
                if toplamcanavar <= 130 :
                    while canavarkontrol < toplamcanavar:
                        yaratıksatırı = random.randint(1,5)
                        yaratıksütunu = random.randint(2,27)
                        if oyunekranı[yaratıksatırı][yaratıksütunu] == "O":
                            canavarkontrol-=1
                        else :
                            oyunekranı[yaratıksatırı][yaratıksütunu] = "O"
                        canavarkontrol+=1
                    break
                else :
                    print("En fazla 130 canavarla mücadele edebilirsiniz")
                    continue
                break
            break                    
        except ValueError :
            print("Lütfen geçerli bir girdide bulununuz")


def ekranyansıtma():
    global hareketlistesi, satır, sütun, hareketpuanı
    for a in range(0,11):
        for b in range(0,30):
            print(oyunekranı[a][b], end ="")
        print("")
        

def karakterihareketettirme():
    global hareketlistesi, satır, sütun, hareketpuanı
    while True:
        hareketlistesi += input()
        ekrandeğişim = 0
        for c in hareketlistesi:
            if sütun > 27 or sütun < 2 :
                hareketlistesi = []
                if sütun > 27:
                    for temizlik in range(1,29):
                        oyunekranı[satır][temizlik] = " "
                    sütun = 27
                    oyunekranı[satır][sütun] = "A"
                if sütun < 2 :
                    for temizlik in range(1,29):
                        oyunekranı[satır][temizlik] = " "
                    sütun = 2
                    oyunekranı[satır][sütun] = "A"
                break
            if c == "a":
                oyunekranı[satır][sütun] = " "
                sütun-=1
                oyunekranı[satır][sütun] = "A"
                ekrandeğişim = 1
                hareketpuanı+=1
            elif c =="d":
                oyunekranı[satır][sütun] = " "
                sütun+=1
                oyunekranı[satır][sütun] = "A"
                ekrandeğişim = 1
                hareketpuanı+=1
            else :
                break
            hareketlistesi = []
        if ekrandeğişim == 1:
            ekranyansıtma()
        break

def ateşetme():
    global hareketlistesi, satır, sütun, hareketpuanı, yaratıksayısı, ateşlistesi
    while True:
        ateşlistesi += input()
        atışanimasyonu = 0
        for ateş in range(len(ateşlistesi)):
            for mermi in range(9,0,-1):
                if oyunekranı[mermi][sütun]== "O":
                    if oyunekranı[mermi][sütun] != "X":
                        if atışanimasyonu == 0:
                            oyunekranı[int(9-mermi/2)][sütun] = "↑"
                            ekranyansıtma()
                            oyunekranı[int(9-mermi/2)][sütun] = " "
                            atışanimasyonu+=1
                        oyunekranı[mermi][sütun] = "X"                
                        hareketpuanı+=1
                        yaratıksayısı-=1
                        break
                    else :
                        oyunekranı[mermi][sütun] = "X"
                        hareketpuanı+=1
                        yaratıksayısı-=1
                        break
        ekranyansıtma()
        ateşlistesi = []
        break
            
def oyunsunumu():
    global hareketlistesi, satır, sütun, hareketpuanı
    print("Yarkın Avlama'ya Hoş Geldiniz!")
    print("Sağa hareket = a","Sola hareket = d", "Ateş etme = i", sep = "\n" )
    print("Başlamak İçin Yalnızca -Enter- Tuşuna Basınız")
    while True:
        başlamakomudu = input()
        if başlamakomudu == "":
            break
        else :
            print("Lütfen geçerli bir girdide bulununuz.")
    
def oyundöngüsü():
    global hareketlistesi, satır, sütun, hareketpuanı, yaratıksayısı
    yaratıküretme()
    ekranyansıtma()
    yaratıksayısı = toplamcanavar
    while True :
        if yaratıksayısı == 0:
            break
        else :
            print("Kalan yaratık sayısı :",yaratıksayısı)
        karakterihareketettirme()
        ateşetme()
        
def oyunsonu():
    global hareketlistesi, satır, sütun, hareketpuanı
    print("Tebrikler, tüm Yarkın'ları başarıyla avladınız!")
    kazanılanpuan = toplamcanavar*2000-hareketpuanı*200
    print("Kazandığınız puan =", kazanılanpuan)
    puanlistesi.append(kazanılanpuan)
    puanlistesi.sort()
    print("En yüksek skor =",puanlistesi[-1])

def devamkomudu() :
    global hareketlistesi, satır, sütun, hareketpuanı
    print("Devam etmek ister misiniz?","e -> Evet","h -> Hayır", sep="\n")
    while True :
        devamsorusu = input()
        if devamsorusu == "e":
            break
        elif devamsorusu == "h":
            print("Oynadığınız için teşekkürler!")
            sys.exit()
        else :
            print("Lütfen geçerli bir girdide bulununuz")

while True:
    hareketlistesi =[]
    ateşlistesi = []
    satır = 9
    sütun = 14
    hareketpuanı = 0
    kazanılanpuan = 0
    oyunekranı = [["╔","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","╗"],
              ["║"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","║"],
              ["║"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","║"],
              ["║"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","║"],
              ["║"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","║"],
              ["║"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","║"],
              ["║"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","║"],
              ["║"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","║"],
              ["║"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","║"],
              ["║"," "," "," "," "," "," "," "," "," "," "," "," "," ","A"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","║"],
              ["╚","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","═","╝"]]
    kazanılanpuan = 0
    hareketpuanı = 0
    toplamcanavar = 0
    oyunsunumu()
    oyundöngüsü()
    oyunsonu()
    devamkomudu()

          
            
    
    
    

