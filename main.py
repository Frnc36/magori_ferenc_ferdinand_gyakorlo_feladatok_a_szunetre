import feladat


print()
print("1.feladat")
feladat.intervallum_200_920_közt()


print()
print("2.feladat")
feladat.csoport1_napja(1)


print()
print("3.feladat")
feladat.marti_algoritmus("Péntek", "programozás")


print()
print("4.feladat")
feladat.valosszam_gyok()


print()
print("5.feladat")
feladat.teglalap_szamitas()


print()
lista = feladat.veletlen13_szamgeneralas()
print(f"6.feladat listája - lista = ",lista)

feladat.veletlen13_poz_neg(lista)
pozitiv, negativ = feladat.veletlen13_poz_neg(lista)
print(f"A listában {pozitiv} pozítiv szám van.")
print(f"A listában {negativ} negatív szám van.")

paros_ossz, paratlan_ossz = feladat.veletlen13_osszeg(lista)
print("A páros számok összege:", paros_ossz)
#print("A páratlan számok összege:", paratlan_ossz)

#nagyobb = feladat.feladat6_naggobb(paros_ossz, paratlan_ossz) # main-ben is összelehetne hasónlítani
nagyobb, nagyszam = feladat.veletlen13_naggobb(lista)
print(f"A {nagyobb} számoké a nagyobb {nagyszam} db.")

atlag = feladat.veletlen13_atlag(lista)
print(f"A számok átlaga: {atlag}")

max = feladat.veletlen13_maximum(lista)
print(f"A listában a legnagyobb szám: {max}\n")


print()
print(f"7.feladat\nA '@'-jel a program vége")
nevek, db = feladat.nevek_lista()
#print(nevek) # ki iratni szépen az listában lévő neveket
print(f"{db} nevet adoott meg.", nevek)

abetu = feladat.nevek_Abetus(nevek)
print(f"{abetu} darab A-val kezdödő név van.")

leghosszabb = feladat.nevek_leghosszabb(nevek)
print("A leghosszabb név:", leghosszabb)


print()
print("8.feladat")
f_db, max_f_sorozat = feladat.erme_dobas()
print(f"A beadott f betűk száma: {f_db}")
print(f"A leghosszabb f - sorozat: {max_f_sorozat}")


print()
print(f"9.feladat\nA 10-es szorzó tábla:\n{"=" * 15}")
feladat.tiz_X_tiz()


print()
print("10.feladat")
feladat.helyiertek(1234)


print()
print("11.feladat")
feladat.szamjegyek_osszeg(324)


print()
print("12.feladat")
feladat.tokeletes_szam()


print()
print("13.feladat")
oszto = feladat.legnagyobb(12, 18)
print(f"A legnagyobb közös osztója: {oszto}")


print()
print("Legkisebb közös többszörös.feladat")
szam = feladat.legkisebb(6, 5)
print("A legkisebb közös többszörös:",szam)


print()
print("Természettel  Vadászati és Természeti Világkiállítás.feladat")
feladat.feladat_vilagkiallitas()
print()
