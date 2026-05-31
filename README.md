# ScholarSpace

Platform informasi event akademik dan teknologi — lomba, beasiswa, bootcamp, magang, dan peluang karier untuk mahasiswa.

---

## Cara Setup (5 langkah)

### 1. Pastikan Python 3.10+ terinstall
```bash
python --version
```

### 2. Buat & aktifkan virtual environment
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

### 4. Inisialisasi database
```bash
python manage.py makemigrations events accounts
python manage.py migrate
```

### 5. Isi data awal & jalankan
```bash
python manage.py seed_data
python manage.py runserver
```

Buka browser: **http://127.0.0.1:8000**

---

## Akun Bawaan

| Tipe | Username | Password | URL |
|------|----------|----------|-----|
| Admin Staff | `admin` | `admin123` | `/admin-panel/` |
| Django Admin | `admin` | `admin123` | `/django-admin/` |

---

## Peta URL

| URL | Halaman |
|-----|---------|
| `/` | Landing page |
| `/explore/` | Daftar semua event + filter |
| `/event/<id>/` | Detail event |
| `/event/<id>/register/` | Form pendaftaran |
| `/event/<id>/bookmark/` | Toggle simpan event |
| `/bookmarks/` | Event tersimpan (login required) |
| `/accounts/login/` | Halaman login |
| `/accounts/register/` | Daftar akun baru |
| `/accounts/profile/` | Profil pengguna |
| `/admin-panel/` | Dashboard admin kustom |
| `/admin-panel/events/` | Kelola event |
| `/admin-panel/categories/` | Kelola kategori |
| `/admin-panel/registrations/` | Data pendaftar |
| `/django-admin/` | Admin bawaan Django |

---

## Struktur Folder

```
scholarspace/
│
├── manage.py                  # Entry point Django CLI
│
├── usktechhub/                # Konfigurasi proyek utama
│   ├── settings.py            # Pengaturan database, static, dll
│   ├── urls.py                # URL routing utama
│   ├── wsgi.py / asgi.py      # Deploy entry point
│
├── events/                    # App utama
│   ├── models.py              # Model: Event, Category, Registration, Bookmark
│   ├── views.py               # Logic halaman publik
│   ├── admin_views.py         # Logic halaman admin kustom
│   ├── admin.py               # Konfigurasi Django Admin
│   ├── urls.py                # URL publik
│   ├── admin_urls.py          # URL admin panel kustom
│   └── management/commands/
│       └── seed_data.py       # Command untuk isi data awal
│
├── accounts/                  # App autentikasi
│   ├── views.py               # Login, register, logout, profil
│   └── urls.py                # URL akun
│
├── templates/                 # Semua template HTML
│   ├── base.html              # Layout utama (navbar, footer)
│   ├── admin/
│   │   └── base_site.html     # Override tema Django Admin
│   ├── events/
│   │   ├── landing.html       # Halaman beranda
│   │   ├── explore.html       # Daftar + filter event
│   │   ├── detail.html        # Detail event
│   │   ├── register.html      # Form pendaftaran
│   │   ├── bookmarks.html     # Event tersimpan
│   │   └── _card.html         # Komponen kartu event
│   ├── accounts/
│   │   ├── login.html
│   │   ├── register.html
│   │   └── profile.html
│   └── admin_panel/
│       ├── base_admin.html    # Layout sidebar admin kustom
│       ├── dashboard.html
│       ├── event_list.html
│       ├── event_form.html
│       ├── category_list.html
│       └── registration_list.html
│
├── static/
│   ├── css/main.css           # Semua styling (semi-glass design system)
│   └── js/main.js             # Interaksi minimal
│
└── media/
    └── posters/               # Upload poster event
```

---

## Fitur Utama

### Pengguna Umum (tanpa login)
- Melihat landing page dengan statistik dan event unggulan
- Menjelajahi semua event dengan filter (kategori, status, tipe)
- Melihat detail lengkap setiap event
- Klik link event eksternal (Dicoding, Gojek, dll)

### Pengguna Login
- Semua fitur pengguna umum
- Mendaftarkan diri ke event (form pendaftaran)
- Menyimpan/menghapus event ke bookmark
- Melihat daftar event tersimpan
- Halaman profil pribadi

### Admin (Staff)
- Dashboard statistik (total event, pendaftar, kategori aktif)
- CRUD event lengkap (tambah, edit, hapus, upload poster)
- Kelola kategori
- Lihat & hapus data pendaftar
- Filter pendaftar per event
- Akses Django Admin (`/django-admin/`) dengan tema glass

---

## Teknologi

| Komponen | Teknologi |
|----------|-----------|
| Backend Framework | Django 4.x (Python) |
| Database | SQLite (development), mudah diganti PostgreSQL |
| Frontend | HTML5, CSS3 (semi-glass design) |
| Font | Inter + Sora (Google Fonts) |
| File Upload | Django + Pillow |
| Auth | Django built-in authentication |
| Admin | Django Admin (custom theme) + custom panel |

---

## Deploy ke Production

```bash
# 1. Ganti SECRET_KEY di settings.py
# 2. Set DEBUG = False
# 3. Tambahkan domain ke ALLOWED_HOSTS
# 4. Collect static files
python manage.py collectstatic

# 5. Gunakan PostgreSQL (opsional)
# Install: pip install psycopg2-binary
# Update DATABASES di settings.py
```
