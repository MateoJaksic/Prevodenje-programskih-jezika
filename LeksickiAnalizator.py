import sys

ulazni_podaci = []

for linija in sys.stdin:
    ulazni_podaci.append(linija.rstrip())

relevatni_znakovi = {"*", "/", "+", "-", "=", "(", ")"}

counter = 1
for zapis in ulazni_podaci:
    if len(zapis) > 1:
        if zapis[0] == "/" and zapis[1] == "/":
            counter = counter + 1
            continue

    rijeci = [""] * len(zapis)
    count = 0
    usao = 0

    for znak in zapis:
        if znak == "\t":
            continue
        elif znak != " " and znak not in relevatni_znakovi:
            rijeci[count] = rijeci[count] + znak
        elif (str)(znak) in relevatni_znakovi:
            if rijeci[count] != "":
                count = count + 1          
            rijeci[count] = znak
            count = count + 1 
        elif rijeci[count] in relevatni_znakovi:
            count = count + 1
            rijeci[count] = znak
            count = count + 1
        elif (str)(znak) in relevatni_znakovi and count == 0:
            rijeci[count] = znak
            count = count + 1 
        elif rijeci[count] == "//":
            rijeci.pop(count)
            break
        else: 
            count = count + 1

    for i in range(len(rijeci)):
        checker1 = 0
        checker2 = 0

        if rijeci[i] == "":
            continue

        for j in range(len(rijeci[i])):
            if rijeci[i] != "za" and rijeci[i] != "od" and rijeci[i] != "do" and rijeci[i] != "az":
                if j == 0:
                    if j != len(rijeci[i])-1:
                        if rijeci[i][0].isnumeric() and rijeci[i][1].isnumeric() == False:
                            checker2 = 1
                            print("BROJ", counter, rijeci[i][0])
                            rijeci[i] = rijeci[i][1:]
                        elif rijeci[i][0].isnumeric() and rijeci[i][1].isnumeric():
                            checker2 = 1
                            continue
                    else:
                        if rijeci[i][0].isnumeric():
                            checker2 = 1
                            print("BROJ", counter, rijeci[i][0])
                            rijeci[i] = rijeci[i][1:]
                else:
                    if rijeci[i].isnumeric() and rijeci[i][j].isnumeric():
                        if j != len(rijeci[i])-1:
                            if rijeci[i][j+1].isnumeric() == False:
                                print("BROJ", counter, rijeci[i][:j])
                            else:
                                continue
                        
                if checker2 != 1 and j != len(rijeci[i])-1:
                    if rijeci[i][j] >= 'a' and rijeci[i][j] <= 'z' or rijeci[i][j] >= '0' and rijeci[i][j] <= '9':
                        if j == len(rijeci[i])-1:
                            checker1 = 1
                            rijeci[i] = rijeci[i][0:]
                            print("IDN", counter, rijeci[i])
                elif checker2 != 1 and j == len(rijeci[i])-1:
                    if rijeci[i][j] >= 'a' and rijeci[i][j] <= 'z' or rijeci[i][j] >= '0' and rijeci[i][j] <= '9':
                        if j == len(rijeci[i])-1:
                            checker1 = 1
                            rijeci[i] = rijeci[i][0:]
                            print("IDN", counter, rijeci[i])
                else:
                    break
            else:
                break

        
        if i <= len(rijeci)-1:
            if rijeci[i].isnumeric():
                print("BROJ", counter, rijeci[i])
            elif rijeci[i] == "=":
                print("OP_PRIDRUZI", counter, rijeci[i])
            elif rijeci[i] == "+":
                print("OP_PLUS", counter, rijeci[i])
            elif rijeci[i] == "-":
                print("OP_MINUS", counter, rijeci[i])    
            elif i < len(rijeci) and rijeci[i] == "/":
                if i < len(rijeci)-1:
                    if rijeci[i] == "/" and rijeci[i+1] != "/":
                        print("OP_DIJELI", counter, rijeci[i])
                    elif rijeci[i] == "/" and rijeci[i+1] == "/":
                        rijeci[i+1] = "//"
                elif i == len(rijeci)-1 and rijeci[i] == "/":
                    print("OP_DIJELI", counter, rijeci[i])
            elif rijeci[i] == "//":
                rijeci.pop(i)
                break
            elif rijeci[i] == "*":
                print("OP_PUTA", counter, rijeci[i])
            elif rijeci[i] == "(":
                print("L_ZAGRADA", counter, rijeci[i])
            elif rijeci[i] == ")":
                print("D_ZAGRADA", counter, rijeci[i])
            elif rijeci[i] == "za":
                print("KR_ZA", counter, rijeci[i])
            elif rijeci[i] == "od":
                print("KR_OD", counter, rijeci[i])
            elif rijeci[i] == "do":
                print("KR_DO", counter, rijeci[i])
            elif rijeci[i] == "az":
                print("KR_AZ", counter, rijeci[i])
            else:
                if checker1 != 1:
                    rijeci[i] = rijeci[i].split("*")
                    for k in range(len(rijeci[i])):
                        if k == len(rijeci[i])-1 and rijeci[i][k] != "":
                            print("IDN", counter, rijeci[i][k])
                        else:
                            if rijeci[i][k] != "":
                                print("IDN", counter, rijeci[i][k])
                                print("OP_PUTA", counter, "*")
    
    counter = counter + 1    