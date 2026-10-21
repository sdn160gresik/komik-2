# Pulau Komik — Panduan pemasangan

Paket ini dibuat untuk repositori `https://github.com/sdn160gresik/komik` dan mempertahankan pola folder yang sudah ada.

## Fitur
- Beranda fantasi ceria, responsif di HP dan komputer.
- Katalog otomatis dari `komik.json`.
- Kartu thumbnail menggunakan `halaman-00.jpg` sebagai sampul bawaan.
- Filter mata pelajaran, pencarian judul/materi, dan pengurutan.
- Pembaca gambar dengan navigasi, progres, layar penuh, keyboard, dan swipe.
- Metadata opsional per bab melalui `info.json` atau `metadata.json`.
- Generator Python yang membuat `komik.json` dari folder bab.
- Workflow deploy GitHub Pages.

## Struktur yang dikenali

Contoh mengikuti pola repositori saat ini:

```text
bhsi/
  nama-folder-bab/
    halaman-00.jpg
    halaman-01.jpg
    halaman-02.jpg
    info.json        # opsional
ipas/
  NAMA_BAB/
    halaman-00.jpg
    halaman-01.jpg
mtk/
  nama-bab/
    halaman-00.jpg
    halaman-01.jpg
soal-cerita/
  nama-bab/
    halaman-00.jpg
    halaman-01.jpg
```

Generator mencari setiap folder yang berisi `halaman-00.jpg`. Berkas bernomor `halaman-00.jpg`, `halaman-01.jpg`, `halaman-02.jpg`, dan seterusnya masuk ke daftar halaman. Untuk menghindari gambar cover tampil sebagai halaman isi, penamaan halaman isi yang disarankan dimulai dari `halaman-01.jpg`.

## Cara memasang

1. Unduh dan ekstrak ZIP paket ini.
2. Salin `index.html`, `assets/`, `generate_komik.py`, dan `.github/workflows/deploy-pages.yml` ke root repositori `sdn160gresik/komik`.
3. Jangan hapus folder komik, workflow lama `update-komik.yml`, atau file lain yang sudah ada.
4. Periksa apakah workflow lama `update-komik.yml` masih berjalan. Paket ini mempertahankan nama output `komik.json` dan field lama (`mapel`, `folder`, `path`, `file`, `nama`, `urutan`, `reader`) sambil menambah daftar `halaman`, thumbnail, dan metadata.
5. Commit dan push perubahan ke branch `main`.
6. Buka GitHub → Settings → Pages. Pilih **GitHub Actions** sebagai Build and deployment source.
7. Buka tab Actions dan pastikan workflow `Deploy Pulau Komik to GitHub Pages` berhasil.
8. Website biasanya tersedia di `https://sdn160gresik.github.io/komik/` setelah Pages aktif.

## Metadata opsional per bab

Buat `info.json` di folder bab:

```json
{
  "judul": "Detektif Misteri Angka",
  "mataPelajaran": "Matematika",
  "kelas": [4, 5, 6],
  "urutan": 1,
  "subjudul": "Petualangan Membongkar Rahasia KPK dan FPB",
  "deskripsi": "Belajar faktor, kelipatan, KPK, dan FPB melalui misteri angka.",
  "thumbnail": "halaman-00.jpg"
}
```

Metadata hanya opsional. Jika tidak ada, judul diambil dari nama folder dan mata pelajaran dari folder tingkat pertama. `thumbnail` dapat berupa nama file dalam folder bab atau URL gambar penuh.

## Catatan penting
- Pastikan setiap bab mempunyai `halaman-00.jpg`, karena generator katalog mengenali folder bab dari berkas ini.
- Nama mata pelajaran yang dikenal: `mtk`, `bhsi`, `ipas`, `pkn`, `ppkn`, `soal-cerita`, `seni`. Folder lain tetap muncul dengan nama yang dibentuk dari nama folder.
- Pastikan file gambar dapat diakses publik.
- Jika `update-komik.yml` lama dan workflow Pages berjalan bersamaan, keduanya dapat memicu commit. Apabila terjadi workflow berulang atau konflik, ubah workflow lama agar tidak melakukan commit `komik.json` (karena workflow Pages sudah membangunnya untuk deployment), atau konsolidasikan proses katalog dan deploy dalam satu workflow setelah memastikan cara kerja `save_komik.sh`.
- Paket ini tidak otomatis mengunggah berkas ke GitHub. Anda perlu menyalin file ke repositori dan melakukan commit/push, kecuali memakai integrasi GitHub yang terhubung.
