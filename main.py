import feladat


print()
print("1.feladat")
feladat.feladat1()


print()
print("2.feladat")
feladat.feladat2(1)


print()
print("3.feladat")
feladat.feladat3("Péntek", "programozás")


print()
print("4.feladat")
feladat.feladat4()


print()
print("5.feladat")
feladat.feladat5()


print()
lista = feladat.feladat6_szamgeneralas()
print(f"6.feladat listája - lista = ",lista)

feladat.feladat6_poz_neg(lista)
pozitiv, negativ = feladat.feladat6_poz_neg(lista)
print(f"A listában {pozitiv} pozítiv szám van.")
print(f"A listában {negativ} negatív szám van.")

paros_ossz, paratlan_ossz = feladat.feladat6_osszeg(lista)
print("A páros számok összege:", paros_ossz)
#print("A páratlan számok összege:", paratlan_ossz)

#nagyobb = feladat.feladat6_naggobb(paros_ossz, paratlan_ossz) # main-ben is összelehetne hasónlítani
nagyobb, nagyszam = feladat.feladat6_naggobb(lista)
print(f"A {nagyobb} számoké a nagyobb {nagyszam} db.")

atlag = feladat.feladat6_atlag(lista)
print(f"A számok átlaga: {atlag}")

max = feladat.feladat6_maximum(lista)
print(f"A listában a legnagyobb szám: {max}\n")


print()
print(f"7.feladat\nA '@'-jel a program vége")
nevek, db = feladat.feladat7()
#print(nevek) # ki iratni szépen az listában lévő neveket
print(f"{db} nevet adoott meg.", nevek)

abetu = feladat.feladat7_Abetus(nevek)
print(f"{abetu} darab A-val kezdödő név van.")

leghosszabb = feladat.feladat7_leghosszabb(nevek)
print("A leghosszabb név:", leghosszabb)


print()
print("8.feladat")
f_db, max_f_sorozat = feladat.feladat8()
print(f"A beadott f betűk száma: {f_db}")
print(f"A leghosszabb f - sorozat: {max_f_sorozat}")


print()
print(f"9.feladat\nA 10-es szorzó tábla:\n{"=" * 15}")
feladat.feladat9()


print()
print("10.feladat")
feladat.feladat10(1234)


print()
print("11.feladat")
feladat.feladat11(324)


print()
print("12.feladat")
feladat.feladat12()


print()
print("13.feladat")
oszto = feladat.feladat13(12, 18)
print(f"A legnagyobb közös osztója: {oszto}")


print()
print("legkisebb.feladat")
szam = feladat.legkisebb(6, 5)
print("A legkisebb közös többszörös:",szam)


print()
print("Természettel  Vadászati és Természeti Világkiállítás.feladat")
feladat.feladat_vilagkiallitas()
print()
