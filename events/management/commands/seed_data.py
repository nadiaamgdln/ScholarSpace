from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from events.models import Category, Event
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Seed data for ScholarSpace'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@scholarspace.id', 'admin123')
            self.stdout.write('Superuser: admin / admin123')

        cats = [
            {'name':'Lomba','slug':'lomba','icon':'🏆','color':'#d97706'},
            {'name':'Beasiswa','slug':'beasiswa','icon':'🎓','color':'#1a56db'},
            {'name':'Bootcamp','slug':'bootcamp','icon':'💻','color':'#7c3aed'},
            {'name':'Webinar','slug':'webinar','icon':'🎙️','color':'#0891b2'},
            {'name':'Workshop','slug':'workshop','icon':'🔧','color':'#059669'},
            {'name':'Magang','slug':'magang','icon':'💼','color':'#db2777'},
            {'name':'Karier','slug':'karier','icon':'📈','color':'#ea580c'},
            {'name':'Event Kampus','slug':'event-kampus','icon':'🏛️','color':'#4f46e5'},
        ]
        co = {}
        for c in cats:
            obj, _ = Category.objects.get_or_create(slug=c['slug'], defaults=c)
            co[c['slug']] = obj
        self.stdout.write(f'Categories: {len(cats)}')

        now = timezone.now()
        events = [
            # LOMBA (2 events)
            {
                'title': 'Gemastik XVI 2025 — Kompetisi IT Nasional',
                'category': co['lomba'], 'organizer': 'Ditjen Dikti Kemdikbud',
                'description': 'Gelar Mahasiswa Teknologi Terbaik (Gemastik) merupakan kompetisi bergengsi tingkat nasional di bidang teknologi informasi dan komunikasi.\n\nBidang yang dilombakan:\n- Pengembangan Perangkat Lunak\n- Keamanan Siber\n- Data Mining & Business Intelligence\n- Desain Pengalaman Pengguna (UI/UX)\n- Animasi\n- Pengembangan Game\n- Karya Tulis Ilmiah TIK',
                'event_date': now+timedelta(days=75), 'deadline': now+timedelta(days=40),
                'location': 'Universitas Brawijaya, Malang',
                'link_online': 'https://gemastik.kemdikbud.go.id',
                'event_type': 'offline', 'price': 'Gratis',
                'benefit': '- Hadiah total ratusan juta rupiah\n- Piala dan medali\n- Sertifikat Dikti\n- Peluang beasiswa',
                'requirement': '- Mahasiswa aktif S1/D4/D3\n- Tim 2–5 orang\n- Karya orisinal belum pernah menang lomba lain',
                'status': 'open', 'is_featured': True,
            },
            {
                'title': 'ICPC Asia Regional 2025',
                'category': co['lomba'], 'organizer': 'ICPC Foundation',
                'description': 'International Collegiate Programming Contest (ICPC) adalah kompetisi pemrograman bergengsi tingkat internasional untuk mahasiswa.\n\nPeserta akan menyelesaikan soal algoritmik dalam waktu terbatas secara tim (3 orang per tim).',
                'event_date': now+timedelta(days=95), 'deadline': now+timedelta(days=50),
                'location': 'Online + Onsite Asia Regional',
                'link_online': 'https://icpc.global',
                'event_type': 'hybrid', 'price': 'Gratis',
                'benefit': '- Medali untuk finalis\n- Sertifikat internasional\n- Tiket ke World Finals bagi juara',
                'requirement': '- Mahasiswa aktif usia maks 24 tahun\n- Tim 3 orang\n- Belum pernah ikut World Finals lebih dari 2x',
                'status': 'open', 'is_featured': False,
            },
            # BEASISWA (2 events)
            {
                'title': 'Beasiswa PIJAK x IBM SkillsBuild — Pelatihan AI Gratis',
                'category': co['beasiswa'], 'organizer': 'Dicoding x IBM SkillsBuild',
                'description': 'Program Pijak in collaboration with IBM SkillsBuild menghadirkan beasiswa pelatihan Artificial Intelligence (AI) berstandar industri global, 100% gratis.\n\nProgram ini menargetkan 30.000 talenta digital Indonesia. Kurikulum mencakup:\n- Dasar-dasar AI\n- Machine Learning praktis\n- Soft skills karier\n- Project portofolio nyata\n- Bimbingan expert industri\n\nPeserta terpilih berpeluang mendapat konversi hingga 20 SKS.',
                'event_date': now+timedelta(days=60), 'deadline': now+timedelta(days=30),
                'location': 'Online (Dicoding Platform)',
                'link_online': 'https://www.dicoding.com/pijak',
                'event_type': 'online', 'price': 'Gratis (Beasiswa)',
                'benefit': '- Pelatihan AI 100% gratis\n- Sertifikat IBM SkillsBuild & Dicoding\n- Konversi hingga 20 SKS\n- Sesi bersama expert industri\n- Peluang rekrutmen kerja',
                'requirement': '- WNI semua kalangan\n- Pelajar, mahasiswa, atau umum\n- Komitmen mengikuti program hingga selesai\n- Memiliki laptop dan koneksi internet',
                'status': 'open', 'is_featured': True,
            },
            {
                'title': 'Beasiswa Google Generation Scholarship 2026',
                'category': co['beasiswa'], 'organizer': 'Google Indonesia',
                'description': 'Google Generation Scholarship adalah program beasiswa Google untuk mendukung mahasiswa berprestasi di bidang ilmu komputer dan teknologi.\n\nProgram mencakup mentorship langsung dari engineer Google, akses eksklusif ke Google Career Certificate, dan networking dengan komunitas tech global.',
                'event_date': now+timedelta(days=110), 'deadline': now+timedelta(days=55),
                'location': 'Online',
                'link_online': 'https://buildyourfuture.withgoogle.com/scholarships',
                'event_type': 'online', 'price': 'Gratis',
                'benefit': '- Stipend bulanan\n- Akses Google Career Certificate\n- Mentorship engineer Google\n- Network tech global\n- Undangan event Google',
                'requirement': '- Mahasiswa aktif S1 semester 4+\n- IPK minimal 3.0\n- Fasih bahasa Inggris\n- Passion di bidang teknologi',
                'status': 'upcoming', 'is_featured': False,
            },
            # BOOTCAMP (3 events)
            {
                'title': 'Coding Camp 2026 powered by DBS Foundation',
                'category': co['bootcamp'], 'organizer': 'Dicoding x DBS Foundation',
                'description': 'Coding Camp powered by DBS Foundation adalah program beasiswa pelatihan coding online yang merupakan hasil kolaborasi DBS Foundation dan Dicoding sejak 2022.\n\nProgram 2026 menargetkan 70.000 peserta dengan tiga jalur:\n- Gen AI Engineer\n- Data Scientist\n- Full-Stack Web Developer\n\nPelatihan mencakup lebih dari 900 jam belajar terstruktur, soft skills, dan literasi keuangan.',
                'event_date': now+timedelta(days=45), 'deadline': now+timedelta(days=1),
                'location': 'Online (Platform Dicoding)',
                'link_online': 'https://www.dicoding.com/codingcamp/registration',
                'event_type': 'online', 'price': 'Gratis (Beasiswa)',
                'benefit': '- Pelatihan intensif 900+ jam\n- Sertifikat kompetensi nasional\n- Soft skills & literasi keuangan\n- Job Exchange Event\n- Diutamakan: mahasiswa, disabilitas, perempuan, warga berpenghasilan rendah',
                'requirement': '- WNI pelajar/mahasiswa/umum\n- Belum pernah ikut Coding Camp 2025 atau 2026 batch 1\n- Komitmen belajar penuh\n- Laptop dan internet',
                'status': 'open', 'is_featured': True,
            },
            {
                'title': 'Bootcamp React.js & Next.js — Frontend Mastery',
                'category': co['bootcamp'], 'organizer': 'Hacktiv8 Indonesia',
                'description': 'Bootcamp intensif selama 6 minggu untuk menguasai ekosistem React.js dan Next.js secara mendalam.\n\nMateri:\n- React Hooks & State Management (Redux)\n- Next.js App Router & Server Components\n- TypeScript untuk React\n- Testing dengan Jest & Testing Library\n- Deployment Vercel & CI/CD',
                'event_date': now+timedelta(days=21), 'deadline': now+timedelta(days=14),
                'location': 'Online via Zoom',
                'link_online': 'https://hacktiv8.com',
                'event_type': 'online', 'price': 'Rp 2.500.000',
                'benefit': '- Sertifikat Hacktiv8\n- Career support & job referral\n- Akses materi seumur hidup\n- Proyek portfolio siap pakai',
                'requirement': 'Mahasiswa/umum yang sudah menguasai HTML, CSS, JavaScript dasar',
                'status': 'open', 'is_featured': False,
            },
            {
                'title': 'Bangkit Academy 2025 — Google, GoTo, Traveloka',
                'category': co['bootcamp'], 'organizer': 'Google, GoTo, Traveloka',
                'description': 'Bangkit adalah program persiapan karier intensif yang diselenggarakan Google, GoTo, dan Traveloka untuk menciptakan talenta digital siap industri.\n\nTiga jalur studi:\n- Machine Learning\n- Cloud Computing\n- Mobile Development (Android)\n\nDurasi 5 bulan dengan soft skills, English session, dan Capstone Project.',
                'event_date': now+timedelta(days=30), 'deadline': now+timedelta(days=10),
                'location': 'Online',
                'link_online': 'https://grow.google/intl/id_id/bangkit/',
                'event_type': 'online', 'price': 'Gratis (Seleksi)',
                'benefit': '- Sertifikat dari Google\n- Peluang kerja langsung\n- Capstone project di tim lintas jalur\n- Network alumni luas',
                'requirement': 'Mahasiswa aktif semester 4–7, IPK 3.0+, komitmen penuh 20 jam/minggu',
                'status': 'open', 'is_featured': False,
            },
            # WEBINAR (2 events)
            {
                'title': 'Webinar: Karier sebagai AI Engineer di Era GenAI',
                'category': co['webinar'], 'organizer': 'Dicoding Indonesia',
                'description': 'Webinar gratis membahas peluang dan tantangan karier sebagai AI Engineer di era Generative AI.\n\nTopik yang akan dibahas:\n- Landscape AI di industri Indonesia 2025\n- Skill yang dibutuhkan perusahaan tech\n- Roadmap belajar AI dari nol\n- Q&A dengan praktisi AI senior',
                'event_date': now+timedelta(days=7), 'deadline': now+timedelta(days=5),
                'location': 'YouTube Live / Zoom Webinar',
                'link_online': 'https://www.dicoding.com/events',
                'event_type': 'online', 'price': 'Gratis',
                'benefit': 'E-sertifikat, rekaman webinar, materi slide',
                'requirement': 'Terbuka untuk semua mahasiswa dan umum',
                'status': 'open', 'is_featured': False,
            },
            {
                'title': 'Tech Talk: Cybersecurity di Era Zero Trust',
                'category': co['webinar'], 'organizer': 'ID-CERT Indonesia',
                'description': 'Diskusi teknis mendalam tentang implementasi arsitektur Zero Trust Security di organisasi modern bersama praktisi keamanan siber nasional.',
                'event_date': now+timedelta(days=18), 'deadline': now+timedelta(days=16),
                'location': 'Zoom Meeting',
                'link_online': 'https://cert.id',
                'event_type': 'online', 'price': 'Gratis',
                'benefit': 'Sertifikat elektronik, rekaman sesi',
                'requirement': 'Mahasiswa IT / profesional yang tertarik cybersecurity',
                'status': 'open', 'is_featured': False,
            },
            # WORKSHOP (2 events)
            {
                'title': 'Workshop Git, GitHub & CI/CD untuk Tim Developer',
                'category': co['workshop'], 'organizer': 'Lab Informatika',
                'description': 'Workshop hands-on belajar version control profesional menggunakan Git dan GitHub, dilanjutkan dengan implementasi CI/CD dasar menggunakan GitHub Actions.\n\nMateri:\n- Git fundamentals & branching strategy\n- Pull Request & Code Review workflow\n- GitHub Actions untuk CI/CD\n- Deployment otomatis ke server',
                'event_date': now+timedelta(days=10), 'deadline': now+timedelta(days=8),
                'location': 'Lab Komputer Informatika, Banda Aceh',
                'event_type': 'offline', 'price': 'Gratis',
                'benefit': 'Sertifikat, makan siang, sticker pack',
                'requirement': 'Mahasiswa aktif, wajib membawa laptop',
                'status': 'open', 'is_featured': False,
            },
            {
                'title': 'Workshop UI/UX Design dengan Figma — From Zero to Prototype',
                'category': co['workshop'], 'organizer': 'Google Developer Student Club',
                'description': 'Workshop intensif 1 hari belajar Figma dari dasar hingga membuat prototype interaktif yang siap dipresentasikan ke klien atau tim developer.',
                'event_date': now+timedelta(days=25), 'deadline': now+timedelta(days=22),
                'location': 'Online via Zoom',
                'link_online': 'https://gdsc.community.dev',
                'event_type': 'online', 'price': 'Gratis',
                'benefit': 'Sertifikat GDSC, template Figma, rekaman',
                'requirement': 'Terbuka untuk semua, tidak perlu pengalaman desain sebelumnya',
                'status': 'open', 'is_featured': False,
            },
            # MAGANG (2 events)
            {
                'title': 'Gojek Tech Internship Program 2025',
                'category': co['magang'], 'organizer': 'Gojek Indonesia',
                'description': 'Program magang teknis di Gojek selama 3–6 bulan. Kamu akan terlibat langsung dalam pengembangan produk yang digunakan jutaan pengguna di Asia Tenggara.\n\nBidang tersedia:\n- Backend Engineering (Go, Kotlin)\n- Frontend Engineering (React, Vue)\n- Data Engineering & Analytics\n- Mobile Development (Android/iOS)',
                'event_date': now+timedelta(days=120), 'deadline': now+timedelta(days=20),
                'location': 'Jakarta / Remote Hybrid',
                'link_online': 'https://www.gojek.com/careers',
                'event_type': 'hybrid', 'price': 'Gratis (Digaji)',
                'benefit': '- Uang saku kompetitif\n- Mentoring dari senior engineer\n- Peluang direkrut full-time\n- Pengalaman produk skala besar',
                'requirement': 'Mahasiswa semester 6+, kuasai salah satu: Python/Go/Kotlin/JavaScript, IPK 3.2+',
                'status': 'open', 'is_featured': False,
            },
            {
                'title': 'Tokopedia Engineer Internship 2025',
                'category': co['magang'], 'organizer': 'Tokopedia (TikTok Shop)',
                'description': 'Bergabung sebagai intern engineer di salah satu platform e-commerce terbesar Indonesia. Kamu akan bekerja di tim produk nyata dengan impact langsung ke jutaan pengguna.',
                'event_date': now+timedelta(days=90), 'deadline': now+timedelta(days=25),
                'location': 'Jakarta / Remote',
                'link_online': 'https://www.tokopedia.com/careers',
                'event_type': 'hybrid', 'price': 'Gratis (Digaji)',
                'benefit': '- Allowance menarik\n- Work from anywhere fleksibel\n- Return offer untuk performa terbaik',
                'requirement': 'Mahasiswa aktif S1 teknik/informatika, familiar dengan sistem terdistribusi',
                'status': 'open', 'is_featured': False,
            },
            # KARIER (1 event)
            {
                'title': 'Tech Career Fair 2025 — 50+ Perusahaan Teknologi',
                'category': co['karier'], 'organizer': 'Glints Indonesia',
                'description': 'Pameran karier teknologi terbesar yang menghadirkan 50+ perusahaan teknologi terkemuka Indonesia.\n\nDapatkan kesempatan:\n- Interview on the spot\n- Networking dengan rekruter\n- Workshop persiapan karier\n- CV & portfolio review',
                'event_date': now+timedelta(days=35), 'deadline': now+timedelta(days=32),
                'location': 'Jakarta Convention Center',
                'link_online': 'https://glints.com',
                'event_type': 'offline', 'price': 'Gratis',
                'benefit': 'Akses interview langsung, CV review, sertifikat, networking',
                'requirement': 'Mahasiswa tingkat akhir dan fresh graduate S1/D4',
                'status': 'open', 'is_featured': False,
            },
            # EVENT KAMPUS (1 event)
            {
                'title': 'Hackathon Nasional IF USK — Build for Aceh',
                'category': co['event-kampus'], 'organizer': 'HMIF Universitas Syiah Kuala',
                'description': 'Hackathon 48 jam membangun solusi teknologi untuk permasalahan nyata di Aceh. Peserta akan dibagi ke dalam tim lintas disiplin untuk merancang, membangun, dan mempresentasikan produk digital.\n\nTema: Smart City, AgriTech, HealthTech, EduTech',
                'event_date': now+timedelta(days=55), 'deadline': now+timedelta(days=35),
                'location': 'Gedung AAC Dayan Dawood, Banda Aceh',
                'link_online': 'https://hmif.usk.ac.id',
                'event_type': 'offline', 'price': 'Rp 50.000/tim',
                'benefit': '- Hadiah Rp 15 juta untuk juara 1\n- Mentoring dari praktisi industri\n- Sertifikat nasional\n- Networking luas',
                'requirement': 'Tim 3–5 orang, minimal 1 anggota mahasiswa aktif',
                'status': 'open', 'is_featured': False,
            },
        ]

        created = 0
        for ev_data in events:
            if not Event.objects.filter(title=ev_data['title']).exists():
                Event.objects.create(**ev_data)
                created += 1
        self.stdout.write(f'Events created: {created}')
        self.stdout.write('Done! Run: python manage.py runserver')
