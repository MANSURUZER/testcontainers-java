print("merhabalar koronavirus testine gitmek ister misiniz?")
karar=str(input("karar (evet ya da hayır)   :"))

if karar == ("evet"):
    print(" sizde bulunanları arada bir boşluk bırakarak sırasıyla girin lütfen   ")
    print("   1-  BAŞ DÖNMESİ   ")
    print("   2-  YÜKSEK ATEŞ   ")
    print("   3-  KURU ÖKSÜRÜK VEYA ÖKSÜRÜK   ")
    print("   4-  YORGUNLUK  ")
    print("   5-  BURUN AKINTISI   ")
    print("   6-  GÖZDE SULANMA   ")
    print("   7-  HAPŞIRMA  ")
    print("   8-  BURUN TIKANIKLIĞI   ")
    print("   9-  BOĞAZ AĞRISI   ")
    print("   10- İSHAL   ")
    print("   11- AĞRI   ")
    seçim= str(input("SİZDE BULUNANLARI ARADA BOŞLUK BIRAKMADAN SIRASIYLA GİRİN   ÖRN:'1467'      :   "))
    if seçim==("234510"):
        print ("    MAALESEF KORONSASIN   ")
    elif seçim==("2345"):
        print("KORONA OLMA İHTİMALİN  '%80' !!")
    elif seçim==("234"):
        print("KORONA OLMA İHTİMALİN  '%60' !!")
    elif seçim==("23"):
        print("KORONA OLMA İHTİMALİN  '%40' !!")
    elif seçim==("2"):
        print("KORONA OLMA İHTİMALİN  '%20' !!")
    elif seçim==("3"):
        print("KORONA OLMA İHTİMALİN  '%25' !!")
    elif seçim==("4"):
        print("KORONA OLMA İHTİMALİN  '%20' !!")
    elif seçim==("5"):
        print("KORONA OLMA İHTİMALİN  '%10' !!")
    elif seçim==("10"):
        print("KORONA OLMA İHTİMALİN  '%10' !!")
    else:
        print(" KORONA DEĞİLSİN  ")

else:
    print("teste girmediniz tekrar denemek ister misiniz?")
    karar2=input("  TESTE TEKRAR GİRMEK İSTER MİSİN ? ")
    if karar2== ("hayır") and ("HAYIR"):
        print("  GİRMİYORSAN GİRME BANANE  ")
    if karar2== ("evet") and ("EVET"):
        print("  HAKKINI KAYBETTİN KOÇUM  ")
        
