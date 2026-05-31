# ScholarSpace

Platform informasi event akademik dan teknologi — lomba, beasiswa, bootcamp, magang, dan peluang karier untuk mahasiswa.

---

## Cara Setup

### 1. Pastikan Python 3.10+ sudah terinstall
```bash
python --version
```

### 2. Buat dan aktifkan virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install django pillow
```

### 4. Buat dan jalankan migrasi database
```bash
python manage.py makemigrations events accounts
python manage.py migrate
```

### 5. Isi data awal, lalu jalankan server
```bash
python manage.py seed_data
python manage.py runserver
```

Buka browser: **http://127.0.0.1:8000**

---

## Akun Bawaan

| Tipe | Username | Password | URL |
|------|----------|----------|-----|
| Admin (Staff) | `admin` | `admin123` | `/admin-panel/` |
| Django Admin | `admin` | `admin123` | `/django-admin/` |

---

## Struktur Folder

```
scholarspace/
│
├── manage.py                        # Entry point semua perintah Django
├── README.md                        # Panduan ini
├── db.sqlite3                       # File database (dibuat otomatis setelah migrate)
│
├── scholarspace/                      # Konfigurasi proyek utama
│   ├── settings.py                  # Database, static files, timezone, installed apps
│   ├── urls.py                      # Router URL utama — menghubungkan semua app
│   ├── wsgi.py                      # Entry point deploy ke server (WSGI)
│   └── asgi.py                      # Entry point deploy ke server (ASGI)
│
├── events/                          # App utama — semua logika event
│   ├── models.py                    # 4 model: Event, Category, Registration, Bookmark
│   ├── views.py                     # Logika halaman publik
│   ├── admin_views.py               # Logika halaman admin panel kustom
│   ├── admin.py                     # Konfigurasi Django Admin bawaan (tema kustom)
│   ├── urls.py                      # URL halaman publik
│   ├── admin_urls.py                # URL /admin-panel/
│   ├── apps.py
│   ├── tests.py
│   └── management/
│       └── commands/
│           └── seed_data.py         # Command isi data awal (8 kategori + 15 event)
│
├── accounts/                        # App autentikasi pengguna
│   ├── views.py                     # Login, register, logout, profil
│   ├── urls.py                      # URL /accounts/
│   ├── apps.py
│   └── models.py
│
├── templates/                       # Semua file HTML
│   ├── base.html                    # Layout utama: navbar + footer (diwarisi semua halaman)
│   │
│   ├── admin/
│   │   └── base_site.html           # Override tampilan Django Admin jadi semi-glass
│   │
│   ├── events/
│   │   ├── landing.html             # Halaman beranda
│   │   ├── explore.html             # Daftar + filter event
│   │   ├── detail.html              # Detail lengkap satu event
│   │   ├── register.html            # Form pendaftaran event
│   │   ├── bookmarks.html           # Daftar event tersimpan
│   │   └── _card.html               # Komponen kartu event (dipakai ulang di landing & explore)
│   │
│   ├── accounts/
│   │   ├── login.html
│   │   ├── register.html
│   │   └── profile.html
│   │
│   └── admin_panel/
│       ├── base_admin.html          # Layout sidebar admin kustom
│       ├── dashboard.html           # Dashboard statistik
│       ├── event_list.html          # Tabel semua event
│       ├── event_form.html          # Form tambah / edit event
│       ├── category_list.html       # Tabel kategori + form tambah
│       ├── category_form.html       # (redirect helper)
│       ├── registration_list.html   # Tabel semua pendaftar + filter
│       └── registration_detail.html # Detail lengkap satu pendaftar
│
├── static/
│   ├── css/
│   │   └── main.css                 # Design system lengkap (semi-glass, warna, layout)
│   └── js/
│       └── main.js                  # Efek scroll navbar + auto-dismiss notifikasi
│
└── media/
    └── posters/                     # Hasil upload poster event oleh admin
```

---

## Fitur Utama

### Pengguna Umum (tanpa login)
- Melihat landing page: statistik real-time, event unggulan, event terbaru, 8 kategori
- Menjelajahi semua event dengan 4 filter sekaligus: kata kunci, kategori, status, tipe
- Melihat detail lengkap setiap event: deskripsi, benefit, syarat, info penyelenggara
- Mengklik link langsung ke website resmi event (Dicoding, Gojek, LPDP, dll)

### Pengguna Login
- Semua fitur pengguna umum
- Mendaftar ke event melalui form (nama, NPM, email, HP, angkatan, motivasi)
- Menyimpan dan menghapus event dari daftar bookmark
- Melihat semua event tersimpan di halaman Tersimpan
- Mengakses halaman profil pribadi

### Admin (Staff)
- Dashboard statistik: total event, event aktif, total pendaftar, total kategori
- CRUD event lengkap: tambah, edit, hapus, upload poster, tandai sebagai featured
- Kelola kategori: tambah dan hapus kategori dengan nama, slug, icon, dan warna
- Lihat daftar semua pendaftar dengan filter per event
- Lihat detail lengkap tiap pendaftar: data diri, email langsung kirim, HP langsung buka WhatsApp, motivasi
- Hapus data pendaftar
- Akses Django Admin bawaan di `/django-admin/` dengan tema semi-glass kustom

---

## Teknologi yang Digunakan

| Komponen | Teknologi |
|----------|-----------|
| Backend framework | Django 4.x (Python) |
| Arsitektur | MVT — Model View Template |
| Database | SQLite (development) |
| ORM | Django ORM |
| Frontend | HTML5 + CSS3 murni (tanpa framework JS) |
| Font | Sora + Inter (Google Fonts) |
| Upload file | Django FileField + Pillow |
| Autentikasi | Django built-in authentication |
| Admin | Django Admin (tema kustom) + custom admin panel |

---
