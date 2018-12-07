falkonSay1000 = falkonSay250=falkonSay500=0
aylıkFalkonSay250 =aylıkFalkonSay500=aylıkFalkonSay1000=0
hemoASay=hemoBSay=0#hemofili a  ve b hastalarının sayısı
topHastaSay=0#Toplam hasta sayısı
agırHastaSay=ortaHastaSay=hafifHastaSay=0
inhibitorASay=inhibitorBSay=0#inhibitör olmayan hasta sayıları
proOrtaHastaSay=0
proAplazmaHastaSay=proArekombinantHastaSay=0#profilaksi uygılanan hemofili A hastalarında plazma kaynaklıve rekombinat kaynaklı hastalar
proBplazmaHastaSay=proBrekombinantHastaSay=0
maxilacMiktarA=maxilacMiktarB=0

while True:

    tc = int(input("TC kimlik numarasını giriniz:\n"))
    topHastaSay+=1

    adSoyad=input("Ad Soyad giriniz:\n")

    hemoTip=str(input("Hemofili tipini giriniz(A/a/B/b):\n"))

    while hemoTip not in ['A','B','b','a']:
          hemoTip=(input("Hatalı! Belirtilen harfleri giriniz:\n"))
  #Hemofili A hastalığına sahip hastaları saydırıyor
    if hemoTip=="A"or hemoTip=="a":
        hemoASay+=1

    else: hemoBSay+=1

    faktorMiktari = float(input("Kandaki faktör miktarini giriniz(0-50):\n"))
    while faktorMiktari<0 or faktorMiktari >= 50 :#sınama
      faktorMiktari=float(input("Hatalı ! 0 ile 50 arasında giriniz:\n"))

    if faktorMiktari<1:
        #Kod tekrarından kaçınmak için şiddet değişkeni tutuldu
        siddet="Ağır"
        agırHastaSay+=1
    elif faktorMiktari<5:
        siddet="Orta"
        ortaHastaSay+=1
    else :
        siddet="Hafif"
        hafifHastaSay+=1


    antikorMiktari=float(input("Antikor miktarini giriniz:\n"))
    while antikorMiktari<0:
        antikorMiktari = float(input("Hatalı!0 veya daha büyük rakam giriniz:\n"))

    #kanama sayısının alınması hastanın şiddeti ortaysa alınıyor
    if faktorMiktari>=1 and faktorMiktari<5:
     kanamaSayisi=int(input("Yılda meydana gelen kanama sayısını giriniz:\n"))
     while kanamaSayisi < 0:
         kanamaSayisi = int(input("Hatalı!0 veya daha büyük rakam giriniz:\n"))

    #profilaksi programına alınacaksa kısıtı sağlanıyor
    if antikorMiktari<5: #inhibitörü olmamalı
        if faktorMiktari<1 or kanamaSayisi>3 :#ağır yada orta hasta olmalı
            kilo=float(input("Hastanın kilosunu giriniz:\n"))
            while kilo < 0 :
                kilo=float(input("Hatalı!0 yada daha büyük rakam giriniz:\n"))
            faktorTur=str(input("Faktör ilacının türünü giriniz(P/p/R/r):\n"))
            while faktorTur not in ['P', 'p', 'R', 'r']:
                faktorTur = (input("Hatalı! Belirtilen harfleri giriniz:\n"))

    print("Tc:",tc)
    print("Ad Soyad:",adSoyad)
    print("Hastalık Tipi:",hemoTip)
    print("Hastalığın şiddeti:",siddet)

    if antikorMiktari<5 and kanamaSayisi>3: #profilaksi uygulanacaksa bunlar hesaplanıyor
     if faktorMiktari < 1 or faktorMiktari<5 :
         print("Hastaya profilaksi uyulanacaktır.")
         if hemoTip=="A"or hemoTip=="a":
             faktorTipi="faktör-8"
             ilacSay=3
             artısMiktari=3
             inhibitorASay+=1#Profilaksi uygulanan hemofili hasta sayısı

             if faktorTur=="p" or faktorTur=="P":
                 proAplazmaHastaSay+=1
             elif faktorTur=="R" or faktorTur=="r" :
                 proArekombinantHastaSay+=1

         if hemoTip=="B" or hemoTip=="b":
             faktorTipi="faktör-9"
             ilacSay=2
             artısMiktari=1
             inhibitorBSay+=1

             if faktorTur=="p" or faktorTur=="P":
                 proBplazmaHastaSay+=1
             elif faktorTur=="R" or faktorTur=="r" :
                 proBrekombinantHastaSay+=1


         if siddet== "Orta" :
             proOrtaHastaSay+=1#Profilaksi uygulanan orta hasta sayıları

         if faktorTur=="P" or faktorTur=="p":
             faktorilacTur="Plazma kaynaklı faktör"
             fiyat=1.25

         if faktorTur == "R" or faktorTur == "r":
             faktorilacTur="Rekombinant Faktör"
             fiyat=1.5

     print ("Kullanacağı faktör ilacı:",faktorTipi,"-",faktorilacTur)
     print("Haftada kullanacağı ilaç sayısı:",ilacSay)

     minilacMiktar=((40-faktorMiktari)*kilo)/artısMiktari#Bir seferde kullanması gereken minumum ilaç miktarı
     print("Bir seferde kullanması gereken minumum ilaç miktarı:",format(minilacMiktar,".2f"),sep="")

     kalan=minilacMiktar%1000
     falkonSay1000=int(minilacMiktar // 1000)
     ilacMiktar=1000*falkonSay1000

     if kalan<=250:
      falkonSay250 += 1
      ilacMiktar+=250

     elif kalan <=500:
      falkonSay500+=1
      ilacMiktar+=500

     elif kalan<=750:
         falkonSay500+=1
         falkonSay250+=1
         ilacMiktar+=750

     elif kalan<=1000:
         falkonSay1000+=1
         ilacMiktar+=1000

     else:
         print()

     print("Bir seferde kullanacağı ilaç miktarı:",format(ilacMiktar,".2f") ,"ünite")
     print("Flakon çeşit ve sayıları:")
     print(" Flakon250 sayısı:",falkonSay250,"\n","Flakon500 sayısı:",falkonSay500,"\n","Flakon1000 sayısı:",falkonSay1000)

     aylıkToplamilac=4*ilacMiktar*ilacSay #haftalık tipine göre kaç kez kullanıldığı bilgisine göre ilacSay ile çarpıldı

     print("4 haftalık toplam ilaç miktarı:",format(aylıkToplamilac,".2f"),"ünite")

     #Aylık falkon sayılarının hesaplanması
     if falkonSay1000 > 0 : #Falkon sayılarının 0 olması durumundaki kontrol
         aylıkFalkonSay1000= 4 * ilacSay *falkonSay1000

     if falkonSay500 > 0:
         aylıkFalkonSay500=4*ilacSay*falkonSay500

     if falkonSay250 > 0:
         aylıkFalkonSay250=4*ilacSay*falkonSay250

     print("Aylık Flakon çeşit ve sayıları:")
     print(" Flakon250 sayısı:", aylıkFalkonSay250, "\n", "Flakon500 sayısı:", aylıkFalkonSay500, "\n", "Flakon1000 sayısı:",
           aylıkFalkonSay1000)

     aylıkilacUcret= aylıkToplamilac* fiyat

     print("4 haftalık ilaç tutarı:",aylıkilacUcret)

     if(hemoTip=="a" or hemoTip=="A"):
         if(aylıkToplamilac>maxilacMiktarA):
             maxilacMiktarA=aylıkToplamilac
             maxAmiktarTc=tc
             maxAmiktarAdSoyad=adSoyad
             maxAmiktarSiddet=siddet
             maxAmiktarkilo=kilo
             maxAmiktarTur=faktorTur
             maxAmiktarTutar=aylıkilacUcret

     if (hemoTip=="B" or hemoTip=="b"):
         if (aylıkToplamilac > maxilacMiktarB):
             maxilacMiktarB= aylıkToplamilac
             maxBmiktarTc = tc
             maxBmiktarAdSoyad = adSoyad
             maxBmiktarSiddet = siddet
             maxBmiktarkilo = kilo
             maxBmiktarTur = faktorTur
             maxBmiktarTutar = aylıkilacUcret

    else:
        print("Hastaya profilaksi uygulanmayacaktır.")



    devamMi = input("Başka hasta var mı(e/E/h/H)?:\n")#yeni gelecek hastaların için devammı tamam mı kontrolü

    while devamMi not in ['e', 'E', 'h', 'H']:
     print("Hatalı!Beirtilen harfleri giriniz:")
     devamMi = input("Başka hasta var mı(e/E/h/H)?:\n")

    if devamMi == 'h' or devamMi == 'H':
     break

## Bütün hastalar bittikten sonra ekrana yazdırılması istenen istatiksel bilgiler

print("-----------------------------------------------------------------------------")
print("Hemofili-A hastalarının sayısı:",hemoASay)
print("Hemofili-B hastalarının sayısı:",hemoBSay)
print("Toplam hasta sayısı:",topHastaSay)

#Zaten mutlaka 1 hasta girilecek o yüzden sıfıra bölünme kontrolü yapılmadı

print("Hastalığın şiddeti ağır olan hastaların sayısı:",agırHastaSay)
print("Hastalığın şiddeti ağır olan hastaların yüzdesi:",format((agırHastaSay*100)/topHastaSay,".2f"))
print("Hastalığın şiddet orta olan hastaların sayısı:",ortaHastaSay)
print("Hastalığın şiddeti orta olan hastaların yüzdesi:",format((ortaHastaSay*100)/topHastaSay,".2f"))
print("Hastalığın şiddeti hafif olan hastaların sayısı:",hafifHastaSay)
print("Hastalığın şiddeti hafif olan hastaların yüzdesi:",format((hafifHastaSay*100)/topHastaSay,".2f"))

if(hemoASay>0):
 print("Hemofili-A hastalarında inhibitor varlığı yüzdesi:",format(((topHastaSay-inhibitorASay)/hemoASay)*100,".2f"))
if(hemoBSay>0):
 print("Hemofili-B hastalarında inhibitor varlığı yüzdesi:",format(((topHastaSay-inhibitorBSay)/hemoBSay)*100,".2f"))

print("Profilaksi uygulanan Hemofili-A hasta sayısı:",inhibitorASay)
print("Profilaksi uygulanan Hemofili-A hasta yüzdesi:",format((inhibitorASay*100)/topHastaSay,".2f"))
print("Profilaksi uygulanan Hemofili-B hasta sayısı:",inhibitorBSay)
print("Profilaksi uygulanan Hemofili-B hasta yüzdesi:",format((inhibitorBSay*100)/topHastaSay,".2f"))

if(ortaHastaSay>0):#sistemde orta hasta sayısı olmaması durumunda
 print("Şiddeti orta olan hastalar arasında profilaksi uygulananların yüzdesi",format((proOrtaHastaSay*100)/ortaHastaSay))

print("Profilaksi uyulanan Hemofili-A hastaları içinde plazma kaynaklı faktör ilacı kullananların sayısı:",proAplazmaHastaSay)
print("Profilaksi uyulanan Hemofili-A hastaları içinde rekombinant kaynaklı faktör ilacı kullananların sayısı:",proArekombinantHastaSay)
print("Profilaksi uyulanan Hemofili-B hastaları içinde plazma kaynaklı faktör ilacı kullananların sayısı:",proBplazmaHastaSay)
print("Profilaksi uygulanan Hemofili-B hastaları içinde rekombinant kaynaklı faktör ilacı kullananların sayısı:",proBrekombinantHastaSay)

if(inhibitorASay>0 or inhibitorBSay>0):
    print("Profilaksi uyulanan Hemofili-A hastaları içinde plazma kaynaklı faktör ilacı kullananların yüzdesi:",
          format((proAplazmaHastaSay*100)/inhibitorASay,".2f"))
    print("Profilaksi uyulanan Hemofili-A hastaları içinde rekombinant kaynaklı faktör ilacı kullananların yüzdesi:",
      format((proArekombinantHastaSay * 100) / inhibitorASay, ".2f"))
    print("Profilaksi uyulanan Hemofili-B hastaları içinde plazma kaynaklı faktör ilacı kullananların yüzdesi:",
          format((proBplazmaHastaSay * 100) / inhibitorASay, ".2f"))
    print("Profilaksi uyulanan Hemofili-B hastaları içinde rekombinant kaynaklı faktör ilacı kullananların yüzdesi:",
          format((proAplazmaHastaSay * 100) / inhibitorASay, ".2f"))
print("SGK’nın karşıladığı", "\n",
      "4 haftalık ilac tutarı:", format(aylıkilacUcret,".2f"), "TL", "\n",
      "1 yıllık faktör ilacı tutarı:",format((aylıkilacUcret * 12),".2f"), "TL", "\n",
      sep=" ")
print("SGK'nın profilaksi uygulama kapsamında ortlama 1 hasta için karşıladığı yıllık toplam ilaç mikatarı:"
      ,format((aylıkToplamilac*12)/topHastaSay))


print("4 haftalık ilaç kullanım miktarı en çok olan Hemofili-A hastasının:", "\n",
      "TC kimlik numarası:", maxAmiktarTc, "\n",
      "Ad ve soyadı: ", maxAmiktarAdSoyad, "\n",
      "Hastalık şiddeti:", maxAmiktarSiddet, "\n",
      "Kilosu:", maxAmiktarkilo, "Kg", "\n",
      "Kullandığı ilaç türü:", maxAmiktarTur, "\n",
      "4 haftalık toplam ilaç kullanım miktarı:", maxilacMiktarA ,"ünite", "\n",
      "4 haftalık toplam ilaç tutarı:", maxAmiktarTutar, "TL", "\n")

print("4 haftalık ilaç kullanım miktarı en çok olan Hemofili-A hastasının:", "\n",
      "TC kimlik numarası:", maxBmiktarTc, "\n",
      "Ad ve soyadı: ", maxBmiktarAdSoyad, "\n",
      "Hastalık şiddeti:", maxBmiktarSiddet, "\n",
      "Kilosu:", maxBmiktarkilo, "Kg", "\n",
      "Kullandığı ilaç türü:", maxBmiktarTur, "\n",
      "4 haftalık toplam ilaç kullanım miktarı:", maxilacMiktarB ,"ünite", "\n",
      "4 haftalık toplam ilaç tutarı:", maxBmiktarTutar, "TL", "\n")