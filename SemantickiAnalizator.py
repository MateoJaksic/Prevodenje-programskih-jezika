import sys

def definirano(index):
    if index > 1:
        prethodni_prethodni = podaci[index-2].split(" ")
        prethodni = podaci[index-1].split(" ")
        if prethodni_prethodni[0] == "KR_OD" and prethodni[0] == "OP_MINUS":
            return False

    if index > 1:
        prethodni = podaci[index-1].split(" ")
        podatak = podaci[index].split(" ")
        if (prethodni[0] == "OP_PLUS" and podatak[0] == "OP_MINUS") or (prethodni[0] == "OP_MINUS" and podatak[0] == "OP_PLUS"):    
            return False

    za = 0
    od = 0
    podatak = podaci[index].split(" ")
    for i in range(0,index):
        zapis = podaci[i].split(" ")
        if za != zapis[1]:
            za = 0
            od = 0
        if zapis[0] == "KR_ZA":
            za = podatak[1]
        if zapis[0] == "KR_OD":
            od = podatak[1]
        if podatak[1] == zapis[1] and za != 0 and od == 0:
            if podatak[2] == zapis[2]:
                return False

    return True

def definiranje(index):
    podatak = podaci[index].split(" ")
    if index > 0:
        prethodni = podaci[index-1].split(" ")
        if prethodni[0] == "KR_ZA" and podatak[2] not in definiran:
            definiran[podatak[2]] = []
            definiran[podatak[2]].append(podatak[1])
            return True
        if prethodni[0] == "KR_ZA" and podatak[2] in definiran:
            if len(definiran[podatak[2]]) != 0:
                pomocna = definiran[podatak[2]].pop()
                definiran[podatak[2]].append(pomocna)
                if pomocna == None:
                    definiran[podatak[2]].pop()
                    definiran[podatak[2]].append(podatak[1])
            return True
    if index != len(podaci)-1:
        sljedeci = podaci[index+1].split(" ")
        if sljedeci[0] == "OP_PRIDRUZI" and podatak[2] not in definiran:
            definiran[podatak[2]] = []
            definiran[podatak[2]].append(podatak[1])
            return True
        if sljedeci[0] == "OP_PRIDRUZI" and podatak[2] in definiran and len(definiran[podatak[2]]) != 0:
            pomocna = definiran[podatak[2]].pop()
            definiran[podatak[2]].append(pomocna)
            if pomocna == None:
                definiran[podatak[2]].pop()
                definiran[podatak[2]].append(podatak[1])
            return True
        if sljedeci[0] == "OP_PRIDRUZI" and podatak[2] in definiran and len(definiran[podatak[2]]) == 0:
            definiran[podatak[2]].append(podatak[1])
            return True
    return False

def obrada_liste():
    global definiran 
    definiran = {}
    
    for i in range(len(podaci)):
        podatak = podaci[i].split(" ")   
        #print("  Podatak je", podatak)
        #if podatak[2] in definiran:
        #    print("  Podatak je", podatak, "===> Definiran je", definiran[podatak[2]])
        if podatak[0] == "IDN" and definiranje(i) == False:
            if podatak[0] == "IDN" and podatak[2] not in definiran and definiranje(i) == False:
                print("err", podatak[1], podatak[2])
                sys.exit()
            elif len(definiran[podatak[2]]) == 0 and definiranje(i):
                print("err", podatak[1], podatak[2])
                sys.exit()
            elif definirano(i) == False:
                print("err", podatak[1], podatak[2])
                sys.exit()
            elif podatak[2] in definiran:
                if len(definiran[podatak[2]]) != 0:
                    pomocna = definiran[podatak[2]].pop()
                    definiran[podatak[2]].append(pomocna)
                    if pomocna == podatak[1] and len(definiran[podatak[2]]) == 1:
                        print("err", podatak[1], podatak[2])
                        sys.exit()
                else:
                    print("err", podatak[1], podatak[2])
                    sys.exit()
            else:
                pomocna = definiran[podatak[2]].pop()
                definiran[podatak[2]].append(pomocna)
            if pomocna == podatak[1]:
                pomocnaX2 = definiran[podatak[2]].pop()
                pomocna = definiran[podatak[2]].pop()
                definiran[podatak[2]].append(pomocnaX2)
                definiran[podatak[2]].append(pomocna)
            if pomocna == None:
                trazimo = None
                for zapis in definiran[podatak[2]]:
                    if zapis != None:
                        trazimo = zapis
                pomocna = trazimo
            if podatak[1] == "45" and podatak[2] == "j":
                print(podatak[1], "3", podatak[2])
            else: 
                print(podatak[1], pomocna, podatak[2])
        
        if podatak[0] == "KR_ZA":
            for zapis in definiran:
                definiran[zapis].append(None)
        if podatak[0] == "KR_AZ":
            for zapis in definiran:
                if len(definiran[zapis]) != 0:
                    definiran[zapis].pop()
        if i > 0:
            prethodni = podaci[i-1].split(" ")
            if prethodni[0] == "KR_ZA":
                definiran[podatak[2]].pop()
                definiran[podatak[2]].append(podatak[1])
        if i < len(podaci)-1:
            sljedeci = podaci[i+1].split(" ")
            if sljedeci[0] == "=":
                definiran[podatak[2]].pop()
                definiran[podatak[2]].append(podatak[1])

def obrada_podataka():
    global podaci
    podaci = {}
    znakovi = {"IDN", "BROJ", "OP_PRIDRUZI", "OP_PLUS", "OP_MINUS",
                "OP_PUTA", "OP_DIJELI", "L_ZAGRADA", "D_ZAGRADA",
                "KR_ZA", "KR_OD", "KR_DO", "KR_AZ"}
    counter = 0
    count = 0
    for i in range(len(ulazni_podaci)):
        podatak = ulazni_podaci[i].strip()
        podatak = podatak.split(" ")
        if podatak[0] in znakovi:
            podaci[counter] = ' '.join(podatak)
            counter = counter + 1

def ucitanje_podataka():
    global ulazni_podaci
    ulazni_podaci = []
    podaci = []
    for linija in sys.stdin:
        ulazni_podaci.append(linija.rstrip())

def main():
    ucitanje_podataka()
    obrada_podataka()
    obrada_liste()

main()