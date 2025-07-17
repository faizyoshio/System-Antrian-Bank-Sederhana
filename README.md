# 🏦 Sistem Manajemen Antrian Bank

Aplikasi ini adalah sistem manajemen antrian bank berbasis desktop yang dirancang untuk mengelola alur pelanggan dengan efisien, menggunakan prioritas antrian dan pengumuman suara.

## 🖼️ Tampilan Aplikasi

Berikut adalah tampilan antarmuka utama aplikasi:

![Tampilan Input Bisnis Pada Sistem Antrian Bank](https://media.discordapp.net/attachments/1395420030589730939/1395420140388094105/Screenshot_378.png?ex=687a61c7&is=68791047&hm=26394b50e3556ea5657e39e7a3da36d78f2e6aee7b29aa64abaa110970071b6f&=&format=webp)


![Tampilan Input Personal Sistem Pada Antrian Bank](https://media.discordapp.net/attachments/1395420030589730939/1395420139930779658/Screenshot_379.png?ex=687a61c7&is=68791047&hm=6c9ce6da5f07610b0870548a23fbc7bdebce0dd60fc362af0083fce173d33563&=&format=webp)


![Tampilan Panggilan Untuk Ke-Meja Pada Sistem Antrian Bank](https://media.discordapp.net/attachments/1395420030589730939/1395420139520000041/Screenshot_380.png?ex=687a61c6&is=68791046&hm=a113ddcc40242ea9db5e3d71aab83fd79a00ee863075f56086d8ac7b0d2bdc26&=&format=webp)

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
