# Pulau Komik — Sistem Baru

## Apa yang berubah?
- Generator memindai semua folder bab yang berisi gambar JPG/JPEG/PNG/WEBP/GIF.
- Tidak perlu `halaman-00.jpg` untuk mendeteksi folder.
- Mata pelajaran berasal dari folder tingkat pertama; metadata per bab bersifat opsional.
- Sampul menggunakan metadata, `cover.jpg`/`sampul.jpg`/`thumbnail.jpg`, atau gambar pertama.
- Satu workflow membangun katalog dan menerbitkan GitHub Pages.

## Instalasi
1. Salin `index.html`, `assets/`, `generate_catalog.py`, dan `.github/workflows/pulau-komik.yml` ke root repositori `sdn160gresik/komik`.
2. Pertahankan folder gambar yang ada.
3. Di GitHub → Settings → Pages, pilih **GitHub Actions**.
4. Tinjau workflow lama yang mengubah `komik.json`. Nonaktifkan workflow lama hanya jika sudah dipastikan tidak ada fungsi penting yang dibutuhkan.
5. Commit dan push ke `main`, lalu periksa tab Actions.

Alamat yang diharapkan setelah Pages aktif: https://sdn160gresik.github.io/komik/

## Struktur
Contoh: `mtk/detektif-angka/halaman-01.jpg`, `bhsi/aku-yang-unik/gambar-1.png`, `ipas/DIMANA_INDONESIA_BERADA?/halaman-02.jpg`. Gambar harus berada langsung di folder bab.

## Metadata opsional
Buat `info.json` di folder bab:
```json
{
  "judul": "Detektif Misteri Angka",
  "mataPelajaran": "Matematika",
  "kelas": [4, 5, 6],
  "urutan": 1,
  "subjudul": "Petualangan KPK dan FPB",
  "deskripsi": "Belajar faktor dan kelipatan melalui misteri angka.",
  "thumbnail": "cover.jpg"
}
```
Tanpa metadata, judul dibaca dari nama folder dan sampul diambil dari gambar pertama. Workflow membangun katalog saat deployment, tanpa commit balik `komik.json`.
