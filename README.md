# 🏦 Sistem Manajemen Antrian Bank

Aplikasi ini adalah sistem manajemen antrian bank berbasis desktop yang dirancang untuk mengelola alur pelanggan dengan efisien, menggunakan prioritas antrian dan pengumuman suara.

## 🖼️ Tampilan Antarmuka Aplikasi

Berikut adalah beberapa tangkapan layar yang menunjukkan antarmuka pengguna aplikasi:

### Layar Utama
Menampilkan status meja pelayanan saat ini, nomor antrian selanjutnya, daftar antrian yang menunggu, dan log aktivitas.
![Layar Utama Sistem Antrian Bank](https://media.discordapp.net/attachments/1395420030589730939/1395474433191448657/Screenshot_391.png?ex=687a9457&is=687942d7&hm=89035cda79055536dc829c2866b0265dd9f0d5e4841119ee565154f1a162f736&=&format=webp)

### Tambah Antrian Bisnis
Dialog untuk menambahkan pelanggan ke antrian bisnis, termasuk nama pelanggan dan jenis layanan.
![Dialog Tambah Antrian Bisnis](https://media.discordapp.net/attachments/1395420030589730939/1395474432859836648/Screenshot_392.png?ex=687a9457&is=687942d7&hm=808dbb42aaa3118437c40425a0279834b9f43d3867705a5acd675c8867c6da25&=&format=webp)

### Tambah Antrian Personal
Dialog untuk menambahkan pelanggan ke antrian personal, termasuk nama pelanggan dan jenis layanan.
![Dialog Tambah Antrian Personal](https://media.discordapp.net/attachments/1395420030589730939/1395474432524419222/Screenshot_393.png?ex=687a9457&is=687942d7&hm=9197a795109a653c30b504426f9953be5228a2d80b3cb7ae5008db086e028a32&=&format=webp)

### Panggilan Meja
Pesan konfirmasi yang muncul setelah memanggil pelanggan ke meja, menampilkan detail pelanggan.
![Dialog Panggilan Meja](https://media.discordapp.net/attachments/1395420030589730939/1395474432121896980/Screenshot_394.png?ex=687a9457&is=687942d7&hm=f0c1fe4067f0f079c50fc8870f70c88a3de0744436f1a05dfc84cf954fd888bb&=&format=webp)

## 🎯 Tujuan Aplikasi

Tujuan utama dari aplikasi ini adalah untuk:
1.  **Mengelola Antrian Pelanggan**: Memungkinkan penambahan dan pemanggilan pelanggan secara terstruktur.
2.  **Prioritas Layanan**: Memberikan prioritas lebih tinggi kepada pelanggan bisnis dibandingkan pelanggan personal.
3.  **Pengumuman Suara Otomatis**: Memberikan panduan suara yang jelas kepada pelanggan tentang nomor antrian dan meja layanan.
4.  **Tampilan Real-time**: Menampilkan status antrian dan meja layanan secara langsung.
5.  **Kemudahan Penggunaan**: Menyediakan antarmuka yang intuitif untuk petugas bank.

## ✨ Fitur Utama Berdasarkan Spesifikasi

Aplikasi ini dirancang untuk memenuhi persyaratan spesifik berikut:

*   **Antrian Terpisah dengan Prioritas**: Nomor antrian untuk tabungan bisnis (berawalan 'B') dan personal (berawalan 'P') memiliki urutan numerik yang terpisah dan independen (masing-masing 1-100, berulang). Pelanggan bisnis memiliki prioritas lebih tinggi daripada pelanggan personal. Sistem menggunakan `heap` untuk memastikan prioritas ini.
*   **Dua Meja Pelayanan**: Aplikasi mendukung dua meja pelayanan, yaitu `Meja 1` dan `Meja 2`, yang dapat memanggil pelanggan secara independen.
*   **Pengumuman Suara Otomatis**: Aplikasi wajib menggunakan suara untuk pemanggilan antrian. Sistem ini menggunakan pustaka `pyttsx3` untuk mengumumkan nomor antrian yang dipanggil ke meja tertentu dalam Bahasa Indonesia.
*   **Tampilan Nomor Antrian Meja**: Nomor antrian pelanggan yang sedang dilayani di `Meja 1` dan `Meja 2` ditampilkan secara jelas di antarmuka utama.

## 💡 Fungsionalitas Tambahan

Selain fitur utama di atas, aplikasi ini juga memiliki fungsionalitas tambahan:

1.  **Penambahan Antrian**:
    *   Petugas dapat menambahkan pelanggan baru ke antrian.
    *   Tersedia dua jenis antrian: **Bisnis** dan **Personal**.
    *   Setiap pelanggan akan mendapatkan nomor antrian unik (misalnya, B001, P002).
    *   Setelah ditambahkan, sistem akan memberikan pengumuman suara "Selamat datang. Nomor antrian Anda adalah [Nomor Antrian]".
    *   Pilihan Jenis Layanan: Saat menambahkan pelanggan, petugas dapat memilih jenis layanan yang relevan dari daftar yang telah ditentukan.

2.  **Panggilan Pelanggan**:
    *   Saat pelanggan dipanggil, sistem akan mengumumkan suara: "Nomor antrian [Nomor Antrian], silakan ke meja [Nomor Meja]".

3.  **Tampilan Status Real-time**:
    *   Layar utama menampilkan "Nomor Selanjutnya" yang akan dipanggil dari antrian.
    *   Daftar antrian yang menunggu ditampilkan secara real-time, diurutkan berdasarkan prioritas.
    *   Log aktivitas terbaru ditampilkan untuk memantau operasi sistem.

## 💻 Teknologi yang Digunakan

Aplikasi ini dikembangkan menggunakan bahasa pemrograman **Python** dengan pustaka-pustaka berikut:

*   **`tkinter`**: Pustaka standar Python untuk membuat antarmuka pengguna grafis (GUI). Digunakan untuk membangun semua elemen visual aplikasi seperti tombol, label, dan jendela.
*   **`pyttsx3`**: Pustaka text-to-speech (TTS) lintas platform yang digunakan untuk menghasilkan pengumuman suara.
*   **`heapq`**: Modul bawaan Python yang mengimplementasikan algoritma antrian prioritas (heap queue), penting untuk manajemen prioritas antrian Bisnis dan Personal.
*   **`threading`**: Digunakan untuk menjalankan pengumuman suara di latar belakang agar aplikasi tetap responsif saat suara diputar.
*   **`datetime`**: Untuk mengelola timestamp dan informasi waktu.

## 🖥️ Mode Layar Penuh Otomatis

Aplikasi ini dirancang untuk berjalan dalam mode layar penuh secara otomatis saat dieksekusi. Ini dicapai dengan menggunakan atribut `root.attributes('-fullscreen', True)` pada jendela utama `tkinter`.

*   **Manfaat**: Memberikan pengalaman pengguna yang imersif dan memastikan tampilan yang konsisten di berbagai ukuran monitor, ideal untuk display publik di area tunggu bank.
*   **Keluar dari Layar Penuh**: Untuk keluar dari aplikasi (dan mode layar penuh), Anda dapat menggunakan tombol "Keluar" yang tersedia di menu aplikasi.

## 🚀 Panduan Instalasi dan Penggunaan

Untuk menjalankan aplikasi ini, Anda perlu menginstal Python dan beberapa pustaka tambahan. Anda juga dapat mengemas aplikasi ini menjadi file executable (`.exe`) untuk distribusi yang lebih mudah.

### 📦 Instalasi Dependensi

Ikuti langkah-langkah di bawah ini untuk menginstal Python dan semua pustaka yang diperlukan:

1.  **Instal Python**:
    Jika Anda belum memiliki Python, unduh dan instal versi terbaru dari situs resmi Python: [python.org](https://www.python.org/downloads/). Pastikan untuk mencentang opsi "Add Python to PATH" selama instalasi.

2.  **Verifikasi Instalasi Python dan pip**:
    Buka Command Prompt (CMD) atau Terminal dan jalankan perintah berikut untuk memastikan Python dan pip (manajer paket Python) terinstal dengan benar:
    
    ```python --version```
    ```pip --version```
3.  **Instal Pustaka yang Diperlukan**:
    Navigasikan ke direktori proyek Anda di Command Prompt atau Terminal (tempat file `Bank_System_Queue.py` dan `requirements.txt` berada), lalu jalankan perintah berikut untuk menginstal semua dependensi:
    ```pip install -r requirements.txt```
    Perintah ini akan menginstal `pyttsx3` dan pustaka lain yang mungkin diperlukan.

### ⚙️ Membuat Aplikasi Executable (.exe)

Anda dapat mengubah skrip Python ini menjadi file `.exe` yang dapat dijalankan di Windows tanpa perlu menginstal Python atau dependensi secara terpisah. Kami akan menggunakan `PyInstaller` untuk ini.

1.  **Instal PyInstaller**:
    Jika Anda belum menginstalnya, instal PyInstaller menggunakan pip:
    ```pip install pyinstaller```

2.  **Buat File Executable**:
    Navigasikan ke direktori proyek Anda di Command Prompt atau Terminal. Kemudian, jalankan perintah PyInstaller berikut:
    ```pyinstaller --onefile --windowed Bank_System_Queue.py```
    *   `--onefile`: Mengemas semua yang diperlukan ke dalam satu file `.exe`.
    *   `--windowed` (atau `-w`): Mencegah jendela konsol hitam muncul saat aplikasi GUI dijalankan.

3.  **Temukan Aplikasi Anda**:
    Setelah proses selesai, Anda akan menemukan file `.exe` di dalam folder `dist` yang dibuat di direktori proyek Anda (misalnya, `dist/Bank_System_Queue.exe`).

**Catatan Penting**:
*   Beberapa perangkat lunak antivirus mungkin menandai file `.exe` yang dibuat oleh PyInstaller sebagai potensi ancaman. Ini adalah *false positive* yang umum karena cara PyInstaller mengemas aplikasi.
*   Proses pembuatan `.exe` mungkin membutuhkan waktu beberapa menit.

## 🤝 Interaksi Pengguna

Pengguna (petugas bank) berinteraksi dengan aplikasi melalui antarmuka grafis yang intuitif:

*   **Tombol Menu**: Tombol-tombol besar dan berwarna-warni di sisi kiri memungkinkan petugas untuk:
    *   Menambah antrian Bisnis atau Personal.
    *   Memanggil pelanggan ke Meja 1 atau Meja 2.
    *   Melihat statistik pelayanan.
    *   Mengakses pengaturan suara.
    *   Keluar dari aplikasi.
*   **Dialog Input**: Saat menambahkan pelanggan, jendela dialog akan muncul untuk memasukkan nama pelanggan dan memilih jenis layanan.
*   **Pesan Konfirmasi/Informasi**: Aplikasi memberikan umpan balik melalui `messagebox` untuk konfirmasi tindakan atau informasi penting (misalnya, "Nomor antrian telah ditambahkan!", "Tidak ada antrian!").
*   **Umpan Balik Visual & Audio**: Perubahan status antrian langsung terlihat di layar, dan pengumuman suara memberikan instruksi yang jelas kepada pelanggan.

Aplikasi ini dirancang untuk menjadi solusi yang kuat dan mudah digunakan untuk manajemen antrian di lingkungan bank.
