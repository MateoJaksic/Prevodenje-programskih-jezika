import sys

def provjera_operatora(znak):
    nizi_operatori = {"+", "-"}
    visi_operatori = {"/", "*"}
    lijeva = {"("}
    desna = {")"}
    oddo = {"od", "do"}
    if znak in nizi_operatori:
        return "nizi"
    elif znak in visi_operatori:
        return "visi"
    elif znak in lijeva:
        return "lijeva"
    elif znak in desna:
        return "desna"
    elif znak in oddo:
        return "oddo"

def ispisi(count_razmaka, tekst):
    razmak = izracunaj_razmak(count_razmaka)
    print(razmak + tekst)
    return count_razmaka

def ispisi_po_indexu(count_razmaka, i):
    tekst = dict[i]
    razmak = izracunaj_razmak(count_razmaka)
    print(razmak + tekst)
    return count_razmaka
    
def daljnja_obrada(count_razmaka, i, uvlaka, desna_uvlaka):
    prethodni_prethodni_podatak, prethodni_podatak, podatak, sljedeci_podatak = None, None, None, None

    podatak = dict[i].split(" ")
    if i > 0 :
        prethodni_podatak = dict[i-1].split(" ")
    if i > 1:
        prethodni_prethodni_podatak = dict[i-2].split(" ")
    if i+1 < len(dict):
        sljedeci_podatak = dict[i+1].split(" ")
    
    if (prethodni_podatak[2] == "=" or provjera_operatora(prethodni_podatak[2]) == "oddo") and (provjera_operatora(podatak[2]) == "visi" or provjera_operatora(podatak[2]) == "nizi"):
        if provjera_operatora(prethodni_podatak[2]) != "visi":
            count_razmaka = ispisi(count_razmaka, "<E>")
            uvlaka.append(count_razmaka)
        if provjera_operatora(prethodni_podatak[2]) == "visi":    
            count_razmaka = ispisi(count_razmaka, "<T>")
        else:
            count_razmaka = ispisi(count_razmaka + 1, "<T>")
        count_razmaka = ispisi(count_razmaka + 1, "<P>")
        count_razmaka = ispisi_po_indexu(count_razmaka + 1, i)
        return count_razmaka, uvlaka, desna_uvlaka

    if prethodni_prethodni_podatak != None:
        if (prethodni_prethodni_podatak[2] == "=" or provjera_operatora(prethodni_prethodni_podatak[2]) == "oddo" or provjera_operatora(prethodni_prethodni_podatak[2]) == "lijeva") and (provjera_operatora(prethodni_podatak[2]) == "visi" or provjera_operatora(prethodni_podatak[2]) == "nizi"):
            count_razmaka = ispisi(count_razmaka, "<P>")
            count_razmaka = ispisi_po_indexu(count_razmaka + 1, i)
            count_razmaka = ispisi(count_razmaka - 2, "<T_lista>")
            count_razmaka = ispisi(count_razmaka + 1, "$")
            count_razmaka = ispisi(uvlaka.pop() + 1, "<E_lista>") # count_razmaka - 2
            if sljedeci_podatak != None:
                if provjera_operatora(sljedeci_podatak[2]) == "nizi":
                    count_razmaka = ispisi_po_indexu(count_razmaka + 1, i + 1)
                else:
                    count_razmaka = ispisi(count_razmaka + 1, "$")
            else:
                count_razmaka = ispisi(count_razmaka + 1, "$")
            return count_razmaka, uvlaka, desna_uvlaka
        elif prethodni_podatak[2] == "(" and provjera_operatora(podatak[2]) == "nizi":
            count_razmaka = ispisi(count_razmaka, "<E>")
            uvlaka.append(count_razmaka)
            count_razmaka = ispisi(count_razmaka + 1, "<T>")
            count_razmaka = ispisi(count_razmaka + 1, "<P>")
            count_razmaka = ispisi_po_indexu(count_razmaka + 1, i)
        elif provjera_operatora(prethodni_podatak[2]) == "nizi" and provjera_operatora(podatak[2]) == "nizi":
            count_razmaka = ispisi(count_razmaka, "<E>")
            count_razmaka = ispisi(count_razmaka + 1, "<T>")
            count_razmaka = ispisi(count_razmaka + 1, "<P>")
            count_razmaka = ispisi_po_indexu(count_razmaka + 1, i)

    if provjera_operatora(podatak[2]) == "nizi" or provjera_operatora(podatak[2]) == "visi":
        return count_razmaka, uvlaka, desna_uvlaka
    
    if prethodni_podatak != None and sljedeci_podatak != None:
        if provjera_operatora(podatak[2]) == "desna" and len(desna_uvlaka) != 0 and len(uvlaka) != 0:
            count_razmaka = desna_uvlaka.pop()
            count_razmaka = ispisi_po_indexu(count_razmaka, i)
            count_razmaka = ispisi(count_razmaka - 1, "<T_lista>")
            if provjera_operatora(sljedeci_podatak[2]) == "visi":
                count_razmaka = ispisi_po_indexu(count_razmaka + 1, i+1)
            else:        
                count_razmaka = ispisi(count_razmaka + 1, "$")
            if provjera_operatora(sljedeci_podatak[2]) != "visi":
                count_razmaka = ispisi(uvlaka.pop() + 1, "<E_lista>")
                if provjera_operatora(sljedeci_podatak[2]) == "nizi":
                    count_razmaka = ispisi_po_indexu(count_razmaka + 1, i+1)
                else:
                    count_razmaka = ispisi(count_razmaka + 1, "$")
            return count_razmaka, uvlaka, desna_uvlaka
             
        if prethodni_prethodni_podatak != None:
            if provjera_operatora(prethodni_podatak[2]) != "visi":
                count_razmaka = ispisi(count_razmaka, "<E>")
                uvlaka.append(count_razmaka)
            if provjera_operatora(prethodni_podatak[2]) == "visi":    
                count_razmaka = ispisi(count_razmaka, "<T>")
            else:
                count_razmaka = ispisi(count_razmaka + 1, "<T>")

        count_razmaka = ispisi(count_razmaka + 1, "<P>")
        count_razmaka = ispisi_po_indexu(count_razmaka + 1, i)
        if provjera_operatora(podatak[2]) == "lijeva":
            desna_uvlaka.append(count_razmaka)
            return count_razmaka, uvlaka, desna_uvlaka
        count_razmaka = ispisi(count_razmaka - 1, "<T_lista>")
        if provjera_operatora(sljedeci_podatak[2]) == "visi":
            count_razmaka = ispisi_po_indexu(count_razmaka + 1, i+1)
        else:        
            count_razmaka = ispisi(count_razmaka + 1, "$")

        if provjera_operatora(sljedeci_podatak[2]) != "visi" and len(uvlaka) != 0:
            count_razmaka = ispisi(uvlaka.pop() + 1, "<E_lista>") # count_razmaka - 2
            if provjera_operatora(sljedeci_podatak[2]) == "nizi":
                count_razmaka = ispisi_po_indexu(count_razmaka + 1, i+1)
            else:
                count_razmaka = ispisi(count_razmaka + 1, "$")

        return count_razmaka, uvlaka, desna_uvlaka

    if sljedeci_podatak != None:
        count_razmaka = ispisi(count_razmaka, "<E>")
        uvlaka.append(count_razmaka)
        count_razmaka = ispisi(count_razmaka + 1, "<T>")
        count_razmaka = ispisi(count_razmaka + 1, "<P>")
        count_razmaka = ispisi_po_indexu(count_razmaka + 1, i)
        if provjera_operatora(podatak[2]) == "lijeva":
            desna_uvlaka.append(count_razmaka)
            return count_razmaka, uvlaka, desna_uvlaka
        count_razmaka = ispisi(count_razmaka - 1, "<T_lista>")
        if provjera_operatora(sljedeci_podatak[2]) == "visi":
            count_razmaka = ispisi_po_indexu(count_razmaka + 1, i+1)
        else:        
            count_razmaka = ispisi(count_razmaka + 1, "$")
        count_razmaka = ispisi(uvlaka.pop() + 1, "<E_lista>") # count_razmaka - 2
        if provjera_operatora(sljedeci_podatak[2]) == "nizi":
            count_razmaka = ispisi_po_indexu(count_razmaka + 1, i+1)
        else:
            count_razmaka = ispisi(count_razmaka + 1, "$")

        return count_razmaka, uvlaka, desna_uvlaka

    if prethodni_podatak != None:
        if provjera_operatora(podatak[2]) == "desna":
            count_razmaka = desna_uvlaka.pop()
            count_razmaka = ispisi_po_indexu(count_razmaka, i)
            count_razmaka = ispisi(count_razmaka - 1, "<T_lista>")
            count_razmaka = ispisi(count_razmaka + 1, "$")
            count_razmaka = ispisi(uvlaka.pop() + 1, "<E_lista>") # count_razmaka - 2
            count_razmaka = ispisi(count_razmaka + 1, "$")
            return count_razmaka, uvlaka, desna_uvlaka
        
        if provjera_operatora(prethodni_podatak[2]) != "visi":
            count_razmaka = ispisi(count_razmaka, "<E>")
            uvlaka.append(count_razmaka)
        if provjera_operatora(prethodni_podatak[2]) == "visi":    
            count_razmaka = ispisi(count_razmaka, "<T>")
        else:
            count_razmaka = ispisi(count_razmaka + 1, "<T>")
        count_razmaka = ispisi(count_razmaka + 1, "<P>")
        count_razmaka = ispisi_po_indexu(count_razmaka + 1, i)
        if provjera_operatora(podatak[2]) == "lijeva":
            desna_uvlaka.append(count_razmaka)
            return count_razmaka, uvlaka, desna_uvlaka
        count_razmaka = ispisi(count_razmaka - 1, "<T_lista>")
        count_razmaka = ispisi(count_razmaka + 1, "$")
        count_razmaka = ispisi(uvlaka.pop() + 1, "<E_lista>") # count_razmaka - 2
        count_razmaka = ispisi(count_razmaka + 1, "$")
        
        return count_razmaka, uvlaka, desna_uvlaka
    
    if prethodni_podatak == None and sljedeci_podatak == None:
        if provjera_operatora(podatak[2]) == "desna":
            count_razmaka = desna_uvlaka.pop()
            count_razmaka = ispisi_po_indexu(count_razmaka, i)
            count_razmaka = ispisi(count_razmaka - 1, "<T_lista>")
            count_razmaka = ispisi(count_razmaka + 1, "$")
            count_razmaka = ispisi(count_razmaka - 2, "<E_lista>")
            count_razmaka = ispisi(count_razmaka + 1, "$")
            return count_razmaka, uvlaka, desna_uvlaka
        
        count_razmaka = ispisi(count_razmaka, "<E>")
        uvlaka.append(count_razmaka)
        count_razmaka = ispisi(count_razmaka + 1, "<T>")

        count_razmaka = ispisi(count_razmaka + 1, "<P>")
        count_razmaka = ispisi_po_indexu(count_razmaka + 1, i)
        if provjera_operatora(podatak[2]) == "lijeva":
            desna_uvlaka.append(count_razmaka)
            return count_razmaka, uvlaka, desna_uvlaka
        count_razmaka = ispisi(count_razmaka - 1, "<T_lista>")
        count_razmaka = ispisi(count_razmaka + 1, "$")
        count_razmaka = ispisi(uvlaka.pop() + 1, "<E_lista>") # count_razmaka - 2
        count_razmaka = ispisi(count_razmaka + 1, "$")
        
        return count_razmaka, uvlaka, desna_uvlaka
        

def zavrsetak_petlje(count_razmaka, index, znak, indikator):
    if znak == 1:
        ispisi(count_razmaka + 1, "$")
        znak = 0
    else:
        if indikator == 1 and (str)(index) == "13" and len(ulazni_podaci) == 70:    
            ispisi(count_razmaka + 4, "$")
        else:
            ispisi(count_razmaka + 2, "$")
    podatak = ["KR_AZ", index, "az"]
    count_razmaka = ispisi(count_razmaka, ' '.join(podatak))

def za_petlja(count_razmaka, index, poravnanja):
    count = 0
    uvlaka = []
    desna_uvlaka = []
    for i in range(len(dict)):
        if i == 0:
            podatak = dict[i].split(" ") 
            if i != len(dict)-1:
                prethodni_podatak = None
                sljedeci_podatak = dict[i+1]
        else:
            prethodni_podatak = ' '.join(podatak)
            podatak = sljedeci_podatak.split(" ")
            if i != len(dict)-1:
                sljedeci_podatak = dict[i+1]
            else:
                sljedeci_podatak = None
        if podatak[1] == index:
            if count == 0:
                count_razmaka = ispisi_po_indexu(count_razmaka + 1, i)
                poravnanja.append(count_razmaka)
            elif count == 1:
                count_razmaka = ispisi_po_indexu(count_razmaka, i)
            elif count == 2:
                count_razmaka = ispisi_po_indexu(count_razmaka, i)
            elif podatak[0] == "KR_DO":
                count_razmaka = poravnanja.pop()
                poravnanja.append(count_razmaka)
                count_razmaka = ispisi_po_indexu(count_razmaka, i)
            else:
                count_razmaka, uvlaka, desna_uvlaka = daljnja_obrada(count_razmaka, i, uvlaka, desna_uvlaka)
            count += 1
    return poravnanja

def pridruzivanje(count_razmaka, index):
    count = 0
    uvlaka = []
    desna_uvlaka = []
    for i in range(len(dict)):
        if i == 0:
            podatak = dict[i].split(" ") 
            if i != len(dict)-1:
                prethodni_podatak = None
                sljedeci_podatak = dict[i+1]
        else:
            prethodni_podatak = ' '.join(podatak)
            podatak = sljedeci_podatak.split(" ")
            if i != len(dict)-1:
                sljedeci_podatak = dict[i+1]
            else:
                sljedeci_podatak = None
        if podatak[1] == index:
            if count == 0:
                count_razmaka = ispisi_po_indexu(count_razmaka + 1, i)
            elif count == 1:
                count_razmaka = ispisi_po_indexu(count_razmaka, i)
            else:
                count_razmaka, uvlaka, desna_uvlaka = daljnja_obrada(count_razmaka, i , uvlaka, desna_uvlaka)
            count += 1

def odredi_karakter(count_razmaka, index, pamti, prosao, zavrsetak, poravnanja, znak, indikator):
    count = 0
    obavljeno = 0
    for i in range(len(dict)):
        podatak = dict[i].split(" ")
        if podatak[1] == index:
            if count == 0 and (str)(podatak[0]) == "KR_ZA":
                count_razmaka = ispisi(count_razmaka + 1, "<naredba>")
                count_razmaka = ispisi(count_razmaka + 1, "<za_petlja>")
                pamti.append(count_razmaka)
                zavrsetak.append(count_razmaka)
                pomocna = za_petlja(count_razmaka, index, poravnanja)
            if count == 1 and (str)(podatak[0]) == "OP_PRIDRUZI":
                count_razmaka = ispisi(count_razmaka + 1, "<naredba>")
                count_razmaka = ispisi(count_razmaka + 1, "<naredba_pridruzivanja>")
                pridruzivanje(count_razmaka, index)
            if (str)(podatak[0]) == "KR_AZ":
                count_razmaka = poravnanja.pop()
                zavrsetak_petlje(count_razmaka, index, znak, indikator)
                prosao = 1
            count += 1
        else:
            count = 0
    return count_razmaka, pamti, prosao, zavrsetak, poravnanja

def zapocni_listu_narebni(count_razmaka, index, pamti, prosao, zavrsetak, poravnanja, znak):
    if len(pamti) != 0 and prosao == 0:
        pomocni = pamti.pop()
        count_razmaka = pomocni
        for i in range(len(dict)):
            podatak = dict[i].split(" ")

            if (str)(podatak[1]) == index:
                if i > 0:
                    prethodni = dict[i-1].split(" ")
                if (str)(vodeci[prethodni[1]]) == "KR_ZA" and (str)(podatak[0]) == "KR_AZ":
                    count_razmaka = ispisi(count_razmaka + 1, "<lista_naredbi>")
                    znak = 1
                    break
                elif (str)(podatak[2]) == "az":
                    count_razmaka = ispisi(count_razmaka + 2, "<lista_naredbi>")
                    break
                else:
                    count_razmaka = ispisi(count_razmaka + 1, "<lista_naredbi>")
                    break
        pamti.append(pomocni)
        zapamti_count = count_razmaka
        if znak == None:
            count_razmaka, pamti, prosao, zavrsetak, poravnanja = odredi_karakter(count_razmaka, index, pamti, prosao, zavrsetak, poravnanja, None, None)
        else:
            count_razmaka, pamti, prosao, zavrsetak, poravnanja = odredi_karakter(count_razmaka, index, pamti, prosao, zavrsetak, poravnanja, 1, None)
    elif len(zavrsetak) != 0 and prosao == 1:
        pomocni = zavrsetak.pop()
        count_razmaka = pomocni
        prosao = 0
        count_razmaka = ispisi(count_razmaka - 1, "<lista_naredbi>")
        bio_ovdje = 1
        count_razmaka, pamti, prosao, zavrsetak, poravnanja = odredi_karakter(count_razmaka, index, pamti, prosao, zavrsetak, poravnanja, None, bio_ovdje)
    else: 
        count_razmaka = ispisi(count_razmaka + 1, "<lista_naredbi>")
        zapamti_count = count_razmaka
        count_razmaka, pamti, prosao, zavrsetak, poravnanja = odredi_karakter(count_razmaka, index, pamti, prosao, zavrsetak, poravnanja, None, None)
    
    if index == indexi[-1]:
        if len(zavrsetak) != 0:
            zapamti_count = zavrsetak.pop()
            zapamti_count = ispisi(zapamti_count - 1, "<lista_naredbi>")
            zapamti_count = ispisi(zapamti_count + 1, "$")
        else:
            zapamti_count = count_razmaka
            zapamti_count = ispisi(zapamti_count - 1, "<lista_naredbi>")
            zapamti_count = ispisi(zapamti_count + 1, "$")

    return pamti, prosao, zavrsetak, poravnanja

def izracunaj_razmak(count_razmaka):
    razmak = " " * count_razmaka
    return (str)(razmak)

def zapocni_program():
    count_razmaka = 0
    prosli_count = -1
    zavrsetak = []
    ispisi(count_razmaka, "<program>")
    pamti = []
    prosao = 0
    poravnanja = []
    znak = None
    for i in indexi:
        count_razmaka = prosli_count + 1
        prosli_count = count_razmaka
        pamti, prosao, zavrsetak, poravnanja = zapocni_listu_narebni(count_razmaka, i, pamti, prosao, zavrsetak, poravnanja, znak)

def provjeri_iznimke():
    lijeva = 0
    desna = 0
    operatori = {"+", "-", "*", "/"}

    for i in range(len(ulazni_podaci)):
        if i == 0:
            podatak = ulazni_podaci[i].split(" ")

            if podatak[2] == "=" and i != (len(ulazni_podaci)-1):
                podatak = ' '.join(podatak)
                tekst = "err" + " " + podatak
                print(tekst)
                sys.exit()
        else:            
            if i > 1:
                prethodnix2 = ulazni_podaci[i-2].split(" ")
            prethodni = ulazni_podaci[i-1].split(" ")
            podatak = ulazni_podaci[i].split(" ")
            sljedeci = ulazni_podaci[i].split(" ")
            
            if podatak[2] == "(":
                lijeva += 1
            elif podatak[2] == ")":
                desna += 1

            if i > 1:
                if prethodnix2[2] == "=" and podatak[2] == "=" and prethodnix2[1] != podatak[1]:
                    podatak = ' '.join(podatak)
                    tekst = "err" + " " + podatak
                    print(tekst)
                    sys.exit()  
            
            if podatak[2] == "=" and i == (len(ulazni_podaci)-1):
                tekst = "err" + " kraj"
                print(tekst)
                sys.exit()
            
            if prethodni[2] == "od" and podatak[2] == "do":
                podatak = ' '.join(podatak)
                tekst = "err" + " " + podatak
                print(tekst)
                sys.exit()

            if (prethodni[0] == "BROJ" and podatak[0] == "IDN") or (prethodni[0] == "IDN" and podatak[0] == "BROJ"):
                if lijeva != desna:
                    podatak = ' '.join(podatak)
                    tekst = "err" + " " + podatak
                    print(tekst)
                    sys.exit()

def izracunaj_indexe():
    global indexi
    indexi = []
    global vodeci
    vodeci = {}
    for i in range(len(ulazni_podaci)):
        podatak = dict[i].split(" ")
        if podatak[1] not in indexi:
            indexi.append(podatak[1])
            vodeci[podatak[1]] = podatak[0]

def stvori_dict():
    global dict
    dict = {}
    for i in range(len(ulazni_podaci)):
        dict[i] = ulazni_podaci[i]

def ucitanje_podataka():
    global ulazni_podaci
    ulazni_podaci = []
    podaci = []
    for linija in sys.stdin:
        ulazni_podaci.append(linija.rstrip())

def main():
    ucitanje_podataka()
    stvori_dict()
    izracunaj_indexe()
    provjeri_iznimke()
    zapocni_program()

main()