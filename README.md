# 🏦 Sistem Manajemen Antrian Bank

Aplikasi ini adalah sistem manajemen antrian bank berbasis desktop yang dirancang untuk mengelola alur pelanggan dengan efisien, menggunakan prioritas antrian dan pengumuman suara.

## 🖼️ Tampilan Aplikasi

Berikut adalah tampilan antarmuka utama aplikasi:

![Tampilan Antarmuka Utama Sistem Antrian Bank](/public/images/app-screenshot.png)

## 🎯 Tujuan Aplikasi

Tujuan utama dari aplikasi ini adalah untuk:
1.  **Mengelola Antrian Pelanggan**: Memungkinkan penambahan dan pemanggilan pelanggan secara terstruktur.
2.  **Prioritas Layanan**: Memberikan prioritas lebih tinggi kepada pelanggan bisnis dibandingkan pelanggan personal.
3.  **Pengumuman Suara Otomatis**: Memberikan panduan suara yang jelas kepada pelanggan tentang nomor antrian dan meja layanan.
4.  **Tampilan Real-time**: Menampilkan status antrian dan meja layanan secara langsung.
5.  **Kemudahan Penggunaan**: Menyediakan antarmuka yang intuitif untuk petugas bank.

## 💡 Fungsionalitas Utama

Aplikasi ini memiliki fungsionalitas inti sebagai berikut:

1.  **Penambahan Antrian**:
    *   Petugas dapat menambahkan pelanggan baru ke antrian.
    *   Tersedia dua jenis antrian: **Bisnis** dan **Personal**.
    *   Setiap pelanggan akan mendapatkan nomor antrian unik (misalnya, B001, P002).
    *   Nomor antrian berurutan dari 001 hingga 100, dan akan mengulang kembali dari 001 setelah mencapai 100. Sistem memastikan tidak ada nomor antrian ganda yang aktif.
    *   Setelah ditambahkan, sistem akan memberikan pengumuman suara "Selamat datang. Nomor antrian Anda adalah [Nomor Antrian]".

2.  **Manajemen Prioritas**:
    *   Pelanggan **Bisnis** memiliki prioritas lebih tinggi daripada pelanggan **Personal**.
    *   Sistem menggunakan struktur data `heap` untuk memastikan pelanggan dengan prioritas lebih tinggi dilayani terlebih dahulu. Jika prioritas sama, pelanggan yang datang lebih dulu akan dilayani.

3.  **Panggilan Pelanggan (Meja 1 & Meja 2)**:
    *   Tersedia dua meja layanan (`Meja 1` dan `Meja 2`).
    *   Petugas dapat memanggil pelanggan berikutnya dari antrian ke meja yang tersedia.
    *   Saat pelanggan dipanggil, sistem akan mengumumkan suara: "Nomor antrian [Nomor Antrian], silakan ke meja [Nomor Meja]".
    *   Nomor antrian yang sedang dilayani di setiap meja akan ditampilkan di layar utama.

4.  **Tampilan Status Real-time**:
    *   Layar utama menampilkan nomor antrian yang sedang dilayani di `Meja 1` dan `Meja 2`.
    *   Juga menampilkan "Nomor Selanjutnya" yang akan dipanggil dari antrian.
    *   Daftar antrian yang menunggu ditampilkan secara real-time, diurutkan berdasarkan prioritas.
    *   Log aktivitas terbaru ditampilkan untuk memantau operasi sistem.

5.  **Statistik Pelayanan**:
    *   Aplikasi melacak total pelanggan yang dilayani, jumlah pelanggan bisnis dan personal yang dilayani, serta panjang antrian yang menunggu.
    *   Statistik ini dapat dilihat melalui menu "Lihat Statistik".

6.  **Pengaturan Suara**:
    *   Tersedia opsi untuk menguji sistem suara.
    *   Memberikan informasi dasar tentang status sistem suara.

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
    Navigasikan ke direktori proyek Anda di Command Prompt atau Terminal (tempat file `queue_system.py` dan `requirements.txt` berada), lalu jalankan perintah berikut untuk menginstal semua dependensi:
    ```pip install -r requirements.txt```
    Perintah ini akan menginstal `pyttsx3` dan pustaka lain yang mungkin diperlukan.

### ⚙️ Membuat Aplikasi Executable (.exe)

Anda dapat mengubah skrip Python ini menjadi file `.exe` yang dapat dijalankan di Windows tanpa perlu menginstal Python atau dependensi secara terpisah. Kami akan menggunakan `PyInstaller` untuk ini.

1.  **Instal PyInstaller**:
    Jika Anda belum menginstalnya, instal PyInstaller menggunakan pip:
    ```pip install pyinstaller```

2.  **Buat File Executable**:
    Navigasikan ke direktori proyek Anda di Command Prompt atau Terminal. Kemudian, jalankan perintah PyInstaller berikut:
    ```pyinstaller --onefile --windowed queue_system.py```
    *   `--onefile`: Mengemas semua yang diperlukan ke dalam satu file `.exe`.
    *   `--windowed` (atau `-w`): Mencegah jendela konsol hitam muncul saat aplikasi GUI dijalankan.

3.  **Temukan Aplikasi Anda**:
    Setelah proses selesai, Anda akan menemukan file `.exe` di dalam folder `dist` yang dibuat di direktori proyek Anda (misalnya, `dist/queue_system.exe`).

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
