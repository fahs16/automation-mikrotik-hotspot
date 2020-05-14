Tools ini dibuat dengan latar belakang project membuat hotspot pada router di semua dinas pada salah satu pemerintahan di Indonesia.

Kondisinya saat ini, akses ke semua router sama semua user dan passwordnya.

Pada baris 32 script run.py, sesuaikan port, user, dan password.

- Tools ini dibuat untuk memudahkan dan mempercepat konfigurasi router berdasarkan kondisi yang ada saat ini.
- Karena dari data yang diperoleh dari user dan kondisi yang dialami script inilah yang menurut saya cukup efektif
- Kumpulan data yang saya peroleh antara lain :
  
  IP Target
  
  User Hotspot
  
  Password Hotspot

- Data tersebut didapatkan dalam suatu aplikasi tiketing.
- Script ini dibuat dari bahasa python 2 dan scripting router mikrotik.
- Cara penggunaan :

```
aceng@terminal-msr-dji-sam-soe:~/develop$ python run.py   
Masukkan Target IP : <masukkan IP target>
Masukkan user hotspot : <masukkan user hotspot>
Masukkan password hotspot : <masukkan password hotspot>
```