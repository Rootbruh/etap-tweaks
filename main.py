import os

from pynvim import command

print("""
 .smNdy+-    `.:/osyyso+:.`    -+ydmNs.    
/Md- -/ymMdmNNdhso/::/oshdNNmdMmy/. :dM/   
mN.     oMdyy- -y          `-dMo     .Nm    
.mN+`  sMy hN+ -:             yMs  `+Nm.    
 `yMMddMs.dy `+`               sMddMMy`    
   +MMMo  .`  .                 oMMM+       
   `NM/    `````.`    `.`````    +MN`      
   yM+   `.-:yhomy    ymohy:-.`   +My      
   yM:          yo    oy          :My             ETAP-TWEAKS FOR PARDUS GNU/LINUX
   +Ms         .N`    `N.      +h sM+           
   `MN      -   -::::::-   : :o:+`NM`       (ARAYÜZÜN SAĞLIKLI ÇALIŞMASI İÇİN UÇBİRİMİNİZİ 
    yM/    sh   -dMMMMd-   ho  +y+My              TAM EKRAN MODUNDA KULLANINIZ.)
    .dNhsohMh-//: /mm/ ://-yMyoshNd`        
      `-ommNMm+:/. oo ./:+mMNmmo:`          
     `/o+.-somNh- :yy: -hNmos-.+o/`         
    ./` .s/`s+sMdd+``+ddMs+s`/s. `/.       
        : -y.  -hNmddmNy.  .y- :           
         -+       `..`       +- 
""")



print("""
#################################################################################################
|                                                                                               |
|     -Pardus ETAP Ayar yöneticisi-                                                             |
|                                                                                               |
| -işlemler-                                                                                    |
|                                                                                               |
|  etap5 için e-kilit kurulumu(1)                                                               |
|  etap19 için e-kilit kurulumu(2)                                                              |
|  etap5 den etap19 a güncelleme(3)                                                             |
|  wine ve mono runtime kurulumu(4)                                                             |
|  eğitim vadisi z-kitap uygulamalarını yükleme(5)        yakında...                            |
|                                                                                               |
|                                                                                               |
|  -bilgilendirme-                                                                              |
|  5. işlem dışındaki işlemler çevrimdışı gerçekleşirken 5. işlemde indirme yapılmaktadır.      |
|                                                                                               |
#################################################################################################
""")

answer = input("[cCc PARDUS cCc]>>> ")

if answer == "1":
  os.system("./scripts/e-kilit_setup.sh")

elif answer == "2":
  os.system("./scripts/e-kilit_setup19.sh")

elif answer == "3":
  os.system("./scripts/etap-update.sh")

elif answer == "4":
  os.system("./scripts/wine-mono.sh")




elif answer == "5":
  print("""
##########################################
    Hangi içerikleri indireceksiniz?    
                                        

       -Edebiyat-
 11TurkDiliveEdebiyatiPdf
 onbirtdemsb
 10TurkDiliveEdebiyatiPDF
 10TurkDiliveEdebiyatiSoru
 9TurkDiliveEdebiyatiPDF
 9TurkDiliEdebiyatiSoru

       -Fizik-
11FizikPlanliDersFoyu
11FizikModulerSoruBankasi
10FizikPlanliDersFoyu
10FizikSoruBankasi
9FizikPlanliDersFoyu
9FizikSoruBankasi

     -Biyoloji-
11BiyolojiPlanliDersFoyu
11BiyolojiModulerSoruBankasi
10BiyolojiPlanliDersFoyu
10BiyolojiSoruBankasi
9BiyolojiPlanliDersFoyu
9BiyolojiSoruBankasi

    -Coğrafya-
11CografyaPlanliDersFoyu
11CografyaModulerSoruBankasi
10CografyaPlanliDersFoyu
10CografyaSoruBankasi
9CografyaPlanliDersFoyu
9CografyaSoruBankasi

    -Matematik-
11MatematikPlanlÄ±DersFoyu
11MatematikMSB
10MatematikPlanliDersFoyu
10MatematikSoruBankasi
9MatematikPlanliDersFoyu
9MatematikSoruBankasi

    -Kimya-
11KimyaPlanliDersFoyu
11KimyaModulerSoruBankasi
10KimyaPlanliDersFoyu
10KimyaSoruBankasi
9KimyaPlanliDersFoyu
9KimyaSoruBankasi

   -Tarih-
11TarihPlanliDersFoyu
11TarihModulerSoruBankasi
10TarihPlanliDersFoyu
10TarihSoruBankasi
9TarihPlanliDersFoyu
9TarihModulerSoruBankasi                                        |
##########################################
    """)
  lesson = input("[cCc PARDUS cCc]>>> ")
  command = f"wget https://cdn2.indivibook.com/EgitimVadisi/{lesson}.deb"
  os.system(command)


else:
    print(f"{answer} numaralı işlem geçersizdir.")