import math
import random


""" majd minden hol a main-be legyen a kiíratás """
""" Baj-e hogy 2 érték van a returnnél?"""


def feladat1():
    szam:int = int(input("Adj meg egy számot 200 és 920 között: "))
    if szam >= 200 and szam <= 920: #zárt vagy nyitott
        while szam >= 10:
            szam = szam // 10
        print("Az első számjegy:", szam)
    else:
        print("Hiba!")
    

    """ While """    
    # szam:int = int(input("Adj meg egy számot 200 és 920 között: "))
    
    # while szam >= 200 and szam <= 920:
    #     print("Hiba")
    #     szam:int = int(input("Adj meg egy számot 200 és 920 között: "))
    # while szam >= 10: # ha if lenne a while helyett akkor csakegy szer futna le és a 120-nál 12, de while-lal addig fut amíg 10-nél kissebb lesz
    #     szam = szam // 10
    # print("Az első számjegy:", szam)


def feladat2(a):
    if a == 1:
        print(" Még 90% on vagyunk!")
        #print(f"{a}.óra = Még 90% on vagyunk!")
    elif a == 2 or a == 3:
        print("Még bírjuk (60%)")
    elif a == 4 or a == 5 or a == 6 or a == 7:
        print("Progit tanulunk, töltődünk! 70%")
    elif a == 8 or a == 9:
        print("Lassan nem bírjuk tovább! 50%")
    elif a >= 10:
        print("Ez már tényleg túlzás.")
    else: # a == 0
        print("Be se jövök!")
        
        
        
def feladat3(nap, ora):
    nap = nap.lower()
    ora = ora.lower()

    if nap == "hétfő": #a
        print(f"{nap.title()} = Márti alszik.")
    elif nap == "kedd" and ora == "hittan": #b
        print(f"{nap.title()} = Márti figyel.")
    elif nap == "kedd" and (not ora == "hittan"): #b
        print(f"{nap.title()} = Márti alszik.")
    elif nap == "szerda" and ora == "programozás": #c
        print(f"{nap.title()} = Márti dolgozik.")
    elif nap == "szerda" and not(ora == "programozás"): #c
        print(f"{nap.title()} = Nincs info.")
    elif nap == "csütörtök": #d
        print(f"{nap.title()} = Márti figyel.")
    else:
        print(f"{nap.title()} = Márti félig van jelen.")
        
    
        
def feladat4():
    szam = float(input("Adj meg egy valós számot: "))
    
    if szam > 0:
        gyok = math.sqrt(szam)
        print(f"A {szam} gyöke:",gyok)
        
    else:
        print("Hiba! Negatív számból nem lehet négyzetgyököt vonni.")
    
    
    """ While """
    # szam = int(input("Adj meg egy valós számot: "))
    
    # while szam < 0:
    #     print("Hiba! Negatív számból nem lehet négyzetgyököt vonni.")
    #     szam = float(input("Adj meg egy valós számot: "))
        
    # gyok = math.sqrt(szam)
    # print(f"A {szam} gyöke: ",gyok)
    
    
def feladat5():
    a = float(input(f"Téglalap A oldala: "))
    b = float(input(f"Téglalap B oldala: "))
    
    while a < 0 or b < 0:
        print("Hiba: a téglalap oldalai nem pozitívak!")
        a = float(input(f"Téglalap A oldala: "))
        b = float(input(f"Téglalap B oldala: "))
    t = a * b
    k = 2*(a + b)
    print(f"A téglalap kerülete: {k:.2f} cm")    
    print(f"A téglalap területe: {t:.2f} cm²")    
    

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
        if len(lista) > 0 and lista[i].title() == "A":
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


def feladat8():
    cv = 0
    f_db = 0
    f_sorozat = 0
    max_f_sorozat = 0
    
    while cv < 10:
        dobas = input(f"Kérem a(z) {cv + 1}. érmedobást (f/i): ").lower()
        if dobas == "f" or dobas == "i":
            if dobas == "f":
                f_db += 1
                f_sorozat += 1
                if f_sorozat > max_f_sorozat:
                    max_f_sorozat = f_sorozat
            else:
                f_sorozat = 0
            cv += 1
        else:
            print("Hibás! Vagy f vagy i!")
    return f_db, max_f_sorozat


def feladat9():
    cv = 0
    
    while cv <=10:
        szorzat = cv * 10
        print(f"10 x {cv:2d} = {szorzat:3d}")
        cv += 1
        
        
def feladat10(szam):
    helyiertek = 1
    
    print(f"A(z) {szam} számjegyei helyiértékenként:")
    while szam > 0:
        szamjegy = szam % 10
        print(f"{helyiertek}-es: {szamjegy}")
        szam = szam // 10
        helyiertek = helyiertek * 10
        
        
        
        
        
        
def legkisebb(a, b):
    szam = max(a, b)
    
    while szam % a != 0 or szam % b != 0:
        szam += 1
    
    return szam
        
 
def feladat_vilagkiallitas():
    szektor = str(input("Adjon meg egy szektort A-H-ig: "))
    
    while szektor == ""or szektor == " " or szektor.isdigit(): # ellenőrzi, hogy csak számjegyekből áll-e a szöveg
        print("HIBA: Adjon meg egy betűt A-H-ig! és forduljon a pénztárhoz.")
        szektor = str(input("Adjon meg egy szektort A-H-ig: "))
    if szektor.upper() == "A":
        print(f"Szektor {szektor.upper()} = Nemzetközi Csarnok, World Conservation Forum 2021")
    elif szektor.upper() == "B" or szektor == "E":
        print(f"Szektor {szektor.upper()} = Kereskedelmi Csarnok")
    elif szektor.upper() == "C":
        print(f"Szektor {szektor.upper()} = Konferencia-központ Innovációs Showroom")
    elif szektor.upper() == "D":
        print(f"Szektor {szektor.upper()} = Hagyományos Vadászati Módok Csarnoka")
    elif szektor.upper() == "G":
        print(f"Szektor {szektor.upper()} = Hazai és nemzetközi Trófeakiállítás, 12. Nyílt Európai Taxiderma-bajnokság, Vadászat 21.században kiállítás")
    elif szektor.upper() == "H":
        print(f"Szektor {szektor.upper()} = Központi Magyar Kiállítás")