# Proyek Segmentasi Citra Dengan Deteksi Tepi  

Proyek ini mengimplementasikan beberapa operator deteksi tepi (edge detection) klasik untuk melakukan segmentasi citra. Program ini memproses beberapa citra contoh dan menghasilkan visualisasi perbandingan dari setiap operator yang digunakan.   


## Fitur Utama  

- Operator Deteksi Tepi yang diimplementasikan  
1. Roberts
2. Prewitt
3. Sobel
4. Frei-Chen  

- Fungsi Penting  
1. Membaca citra dari folder *citra*
2. Melakukan konvolusi manual dengan kernel
3. Normalisasi hasil untuk disimpan sebagai gambar
4. Menampilkan hasil dalam grid 2x2 menggunakan matplotlib
5. menyimpan hasil setiap operator dan perbandingannya ke folder *output*  

## Catatan Penting  
- Program akan membuat folder *output* secara otomatis jika belum ada
- Jika ada citra yang tidak ditemukan, program akan menampilkan pesan error dan lanjut ke citra selanjutnya.  

## Catatan Penting
Proyek ini dibuat untuk tujuan pembelajaran.