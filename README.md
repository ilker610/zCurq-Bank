# zCurq-Bank
> Basit bir modüler Banka sistemi

Kullanım (Direkt Kullanım)
```
python main.py
```

Modül olarak kullanım
```py
from modules.functions import *

bank = functions("kullanici_adi","şifre")
durum = bank.login() # Giriş fonksiyonu çalışır

if durum == "giris_basarili": # Fonksiyondaki Return değerlerini okur.
  print("Başarılı")
```
  
