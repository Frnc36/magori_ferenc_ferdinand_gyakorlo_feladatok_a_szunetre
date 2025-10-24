import feladat

#feladat.feladat1()


#feladat.feladat4()


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
print(f"A listában a legnagyobb szám: {max}")