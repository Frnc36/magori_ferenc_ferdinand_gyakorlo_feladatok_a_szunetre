import math
import random


""" majd minden hol a main-be legyen a kiíratás """

def feladat1():
    szam:int = int(input("Adj meg egy számot 200 és 920 között: "))
    if szam >= 200 and szam <= 920: #zárt vagy nyitott
            print("Hiba!")
    else:
        while szam >= 10:
                szam = szam // 10
        print("Az első számjegy:", szam)
    
    
    """ While """    
    # szam:int = int(input("Adj meg egy számot 200 és 920 között: "))
    
    # while szam >= 200 and szam <= 920:
    #     print("Hiba")
    #     szam:int = int(input("Adj meg egy számot 200 és 920 között: "))
    # while szam >= 10: # ha if lenne a while helyett akkor csakegy szer futna le és a 120-nál 12, de while-lal addig fut amíg 10-nél kissebb lesz
    #     szam = szam // 10
    # print("Az első számjegy:", szam)


def feladat4():
    szam = float(input("Adj meg egy valós számot: "))
    
    if szam > 0:
        gyok = math.sqrt(szam)
        print(gyok)
        
    else:
        print("Hiba! Negatív számból nem lehet négyzetgyököt vonni.")
    
    
    """ While """
    # szam = int(input("Adj meg egy valós számot: "))
    
    # while szam < 0:
    #     print("Hiba! Negatív számból nem lehet négyzetgyököt vonni.")
    #     szam = float(input("Adj meg egy valós számot: "))
        
    # gyok = math.sqrt(szam)
    # print(f"A {szam} gyöke: ",gyok)
    

def feladat6_szamgeneralas():
    lista = []
    cv = 0
    
    while cv < 13:
        velszam = random.randint(-5,12)
        lista.append(velszam)
        cv += 1
    return lista


def feladat6_poz_neg(lista = []):
    cv = 0
    """ 0 sem pozítiv, sem negatív """
    null = 0
    pozitiv = 0
    negativ = 0
    
    while cv < len(lista):
        if lista[cv] == 0:
            null += 1
        elif lista[cv] > 0:
            pozitiv += 1
        else:
            lista[cv] < 0
            negativ += 1
        cv += 1
    return pozitiv, negativ
  

def feladat6_osszeg(lista = []):
    cv = 0 
    paros_ossz = 0
    paratlan_ossz = 0
    
    while cv < len(lista):
        if lista[cv] % 2 == 0:
            paros_ossz += lista[cv]
        elif lista[cv] % 2 == 1:
            paratlan_ossz += lista[cv]
        cv += 1
    return paros_ossz, paratlan_ossz

def feladat6_naggobb(lista):
    cv = 0
    null = 0
    paros = 0
    paratlan = 0
    
    while cv < len(lista):
        if lista[cv] == 0:
            null += 1
        elif lista[cv] % 2 == 0:
            paros += 1
        else:
            paratlan += 1
        cv += 1
    # if paros > paratlan: # ha 6db paros vagy 6db paratlan van akkor egyenlo lenne
    #     return "páros", paros
    # elif paratlan > paros:
    #     return "páratlan", paratlan
    # else:
    #     return "egyenlő", paros
    if paros > paratlan:
        return "páros", paros
    else:
        return "páratlan", paratlan

def feladat6_atlag(lista):
    i = 0
    cv = 0
    osszesen=0
    
    while cv < len(lista):
        osszesen+=lista[i]
        cv+=1
        i+=1
    atlag=osszesen//len(lista)
    
    return atlag


def feladat6_maximum(lista):
    cv = 1
    max = lista[0]  # Kezdeti maximum az első elem
    
    while cv < len(lista):
        if lista[cv] > max:
            max = lista[cv] #Összehasonlítjuk: ha találunk nagyobbat, mint a jelenlegi maximum. Frissítjük: max_ertek = lista[cv] - az új maximum érték
        cv += 1
    
    return max


def feladat7():
    lista = []
    db = 0
    
    nev = str(input("Név: "))
    while nev != "@":
        lista.append(nev)
        nev = str(input("Név: "))
        db += 1
    # if lista == []:
    #     print("Üres a lista")
    
    return lista, db

def feladat7_Abetus(lista = []):
    abetu = 0
    i = 0
    
    while i < len(lista):
        if len(lista) > 0 and lista[i][0].upper() == "A":
            abetu += 1
        i += 1
            
    return abetu

def feladat7_leghosszabb(lista = []):
    leghosszabb = lista[0] # a lista nulladik eleme a leghosszabb elsőnek
    i = 1 # ezért 1-ről indulunk
    
    while i < len(lista):
        if len(lista[i]) > len(leghosszabb):
            leghosszabb = lista[i]
        i += 1
        
    return leghosszabb