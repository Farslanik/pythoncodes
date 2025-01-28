import sys
import random

resim = [["╔", "═", "═", "═", "═", "═", "═","═","═", "═", "═", "═", "╗"],
         ["║", " ", " ", " ", " ", " ", " "," "," ", " ", " ", " ", "║"],
         ["║", " ", "┌", "─", "─", "─", "┐"," "," ", " ", " ", " ", "║"],
         ["║", " ", "│", " ", " ", " ", "│"," "," ", " ", " ", " ", "║"],
         ["║", " ", "│", " ", " ", " ", " "," "," ", " ", " ", " ", "║"],
         ["║", " ", "│", " ", " ", " ", " "," "," ", " ", " ", " ", "║"],
         ["║", " ", "│", " ", " ", " ", " "," "," ", " ", " ", " ", "║"],
         ["║", " ", "│", " ", " ", " ", " "," "," ", " ", " ", " ", "║"],
         ["║", " ", "│", " ", " ", " ", " "," "," ", " ", " ", " ", "║"],
         ["║", " ", "│", " ", " ", " ", " "," "," ", " ", " ", " ", "║"],
         ["║", " ", "│", " ", " ", " ", " "," "," ", " ", " ", " ", "║"],
         ["║", " ", "│", " ", " ", " ", " "," "," ", " ", " ", " ", "║"],
         ["╚", "═", "═", "═", "═", "═", "═","═","═", "═", "═", "═", "╝"]]
         


def ekranyazdırma():
    global resim
    for i in range(len(resim)):
        for a in range(len(resim)):
            print(resim[i][a], end="")
        print("")

adamasmaca = []
adamasmacaekranı = []

def girdialma():
    global adamasmaca, adamasmacaekranı, oyunbitişsayısı
    oyunbitişsayısı = 0
    print("YARKIN ASMACA'ya hoş geldiniz!")
    while True:
        print("Lütfen bir girdide bulununuz")
        while True :
            girdi = input()
            print(f"Sorulacak ifade şudur : {girdi} , Devam etmek ister misiniz?")
            while True :
                devammı = input("e -> Evet , h -> Hayır ")
                if devammı == "e" :
                    devam = 1
                    break
                elif devammı == "h" :
                    devam = 0
                    break
                else :
                    print("Lütfen geçerli bir girdide bulununuz")
            if devam == 1 :
                break
            elif devam == 0 :
                break
        if devam == 1 :
            devam = 1
            break
        elif devam == 0 :
            continue
            
    adamasmaca += girdi
    adamasmacaekranı += girdi
    for i in range(len(adamasmaca)):
        if adamasmaca[i] == " ":
            adamasmacaekranı[i] = "/"
        else :
            adamasmacaekranı[i] = "_"
    print(adamasmacaekranı)

def harftahmini():
    global hatasayısı
    print("Harf tahmininde bulununuz.")
    harftahmin = input()
    uzunluk = 0
    for i in range(len(adamasmaca)) :
        if harftahmin == adamasmaca[i]:
            adamasmacaekranı[i] = harftahmin
        else :
            uzunluk+=1
    if uzunluk == len(adamasmaca):
        hatasayısı+=1
        adamıasmak()
        ekranyazdırma()
        print("Belirtiğiniz harf listede yoktur!")
    else :
        ekranyazdırma()
        print(harftahmin, "listede bulunuyor!")
    print(adamasmacaekranı)
            
            
            
def adamıasmak():
    global hatasayısı, oyunbitişsayısı
    if hatasayısı == 1:
        resim[4][6] = "☻"
        
    elif hatasayısı == 2:
        resim[5][6] = "┼"
        resim[6][6] = "│"
        resim[7][6] = "│"
        
    elif hatasayısı == 3:
        resim[5][7] = "┐"
        resim[6][7] = "│"
        
    elif hatasayısı == 4:
        resim[5][5] = "┌"
        resim[6][5] = "│"
        
    elif hatasayısı == 5:
        resim[8][5] = "/"
        resim[9][4] = "/"

    elif hatasayısı == 6:
        resim[8][7] = "\\"
        resim[9][8] = "\\"
        oyunbitişsayısı = 1
        

    if adamasmacaekranı == adamasmaca :
        oyunbitişsayısı = 1
        







def oyundöngüsü():
    global hatasayısı
    girdialma()
    ekranyazdırma()
    hatasayısı = 0
    galibiyetekranı = ""
    while True :
        harftahmini()
        if hatasayısı == 6 and oyunbitişsayısı == 1 :
            print("Oyun sonlandı, Yarkın vefat etti...")
            for i in range(len(adamasmaca)) :
                galibiyetekranı += adamasmaca[i]
            print("Doğru kelime =", galibiyetekranı, end ="")
            break
        elif hatasayısı < 6 and oyunbitişsayısı == 1 :
            print("Oyunu kazandın, Yarkın kurtuldu! Artık Farslan onu öldürebilir...")
            for i in range(len(adamasmaca)) :
                galibiyetekranı += adamasmaca[i]
            print("Doğru kelime =", galibiyetekranı, end ="")
            break
            
    
        
        


oyundöngüsü()















            
