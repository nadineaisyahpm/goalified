1. Penjelasan implementasi checklist Tugas 2 PBP secara step-by-step:
    1. Membuat sebuah proyek Django baru.
    -> Pertama, saya membuat repositori baru di Github secara manual, yang saya namakan 'Goalified', yaitu nama untuk toko football shop untuk tugas 2 saya. Repositori ini akan digunakan sebagai direktori utama untuk project tersebut. Kemudian, saya melakukan cloning repositori dari Github ke penyimpanan lokal komputer saya. Lalu, saya membuat requirements.txt yang berisi dependencies seperti tutorial 0, dan saya lakukan instalasi terhadap dependencies yang ada dengan command 'pip install -r requirements.txt.'. Jika sudah, saya membuat virtual environment python dan melakukan konfigurasi environment variables .env serta .env.prod seperti yang sudah dicontohkan pada tutorial 0, dengan SCHEMA diubah menjadi "SCHEMA=tugas_individu". Untuk memulai project Goalified, saya menjalankan command 'django-admin startproject goalified' yang akan membuat folder direktori proyek. 
    2. Membuat aplikasi dengan nama main pada proyek tersebut.
    -> Untuk membuat aplikasinya, saya menjalankan command 'python3 manage.py startapp main'.
    3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    -> Pada folder proyek, di file urls.py saya menambahkan:

        urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),   
        ]

        Ini dilakukan agar semua route dihandle oleh main.urls.
    4. Membuat model pada aplikasi main dengan nama Product dengan atribut (Pada main/models.py, saya mengisi):

        class Product(models.Model):
            name = models.CharField(max_length=200)
            price = models.IntegerField()
            description = models.TextField()
            thumbnail = models.URLField(default="https://via.placeholder.com/150")
            category = models.CharField(max_length=100)
            is_featured = models.BooleanField(default=False)
        
        def __str__(self):
            return self.name
        
        Ini bertujuan untuk merepresentasikan struktur data yang akan disimpan pada database sesuai ketentuan pada instruksi tugas 2.
        Selain itu, pada settings.py, saya menambahkan 'main' ke dalam INSTALLED_APPS agar Django mengetahui bahwa aplikasi main aktif, dan model Product yang ada di dalamnya bisa dimigrasikan ke database.
    5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.
        Pada main/views.py, saya menambahkan:

        def show_main(request):
            context = {
                'app_name': 'Goalified',
                'name': '2406408224 - Nadine Aisyah Putri Maharani',
                'class_name': 'PBP F'
            }
            return render(request, 'main/main.html', context)

        Ini bertujuan agar template HTML yang saya buat dapat menampilkan nama aplikasi, kelas, dan nama saya.
    6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
        Pada folder main, saya membuat file urls.py dan menambahkan:

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]

        Ini dilakukan agar url tanpa embel-embel apapun akan otomatis membuka home page ketika dibuka, dan home page tersebut akan menampilkan HTML yang memetakan fungsi yang sudah saya buat pada views.py tadi.
    7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
        (Sebelumnya saya melakukan migrasi untuk menyimpan semua penambahan yang saya lakukan di proyek Django saya, dengan command:

        python manage.py makemigrations
        python manage.py migrate
        
        Lalu, saya juga melakukan git add, commit, dan push semua perubahan ke repositori Github saya.)

        Sebelum deploy, saya buat dulu project baru di Pacil Web Service dengan nama yang sama untuk mendapatkan username, password, serta instruksi command deployment ke link website https://pbp.cs.ui.ac.id/nadine.aisyah/goalified. Lalu sesuai instruksi saya menjalankan command-command ini:

        git remote add pws https://pbp.cs.ui.ac.id/nadine.aisyah/goalified  # menambahkan remote baru bernama pws yang tersambung ke repo PWS.
        git branch -M master                                       # mengganti nama branch lokal jadi master supaya sesuai dengan branch default PWS.
        git push pws master                                        # mengirim semua kode di branch master ke remote pws (PWS server).

2. Link bagan: https://drive.google.com/file/d/1hNUGE_TBC8sBH16AcKXhppUd9u4a3nOw/view?usp=sharing
    Penjelasan Alur Django Request-Response Cycle:
        1. Client (Browser)
            Pengguna mengakses aplikasi web melalui browser dengan mengetikkan URL atau mengirimkan permintaan HTTP (GET/POST).

        2. Web Server -> WSGI/ASGI
            Permintaan diterima oleh web server (misalnya Nginx/Apache), kemudian diteruskan ke WSGI/ASGI yang menjadi jembatan antara server dan Django.

        3. Middleware
            Sebelum mencapai inti aplikasi, permintaan melewati lapisan middleware. Middleware dapat berfungsi untuk autentikasi, keamanan (CSRF), session, logging, dan lain-lain.

        4. URL Resolver (urls.py)
            Django mencocokkan URL permintaan dengan pola (pattern) yang telah didefinisikan di urls.py. Dari sini ditentukan fungsi atau class view mana yang harus dijalankan.

        5. View (views.py)
            View berfungsi sebagai pengendali logika aplikasi.
            Jika dibutuhkan data, view akan memanggil models.py untuk melakukan query ke database.
            View kemudian mengolah data tersebut, lalu mengirimkan data ke template untuk dirender, atau langsung mengembalikan response (misalnya JSON atau redirect).

        6. Model (models.py)
            Models merupakan representasi dari tabel database. Django menggunakan ORM (Object-Relational Mapping) untuk memudahkan interaksi dengan database tanpa harus menulis SQL secara langsung.

        7. Template (HTML)
            Template adalah berkas .html yang digunakan untuk menampilkan data kepada pengguna. Data yang sudah diambil dan diolah di view dikirim ke template sebagai context untuk dirender menjadi halaman HTML dinamis.

        8. Response
            Setelah dirender, Django menghasilkan objek HttpResponse yang berisi HTML final atau jenis respon lainnya. Response ini dikirim kembali ke browser pengguna melalui lapisan middleware dan WSGI/ASGI.

3. Penjelasan peran settings.py dalam proyek Django:
    Dalam proyek Django, file settings.py berperan sebagai pusat konfigurasi yang mengatur bagaimana proyek dijalankan. Di dalamnya terdapat berbagai pengaturan penting, seperti informasi database yang digunakan, daftar aplikasi yang aktif, lokasi template dan static files, bahasa serta timezone, hingga secret key yang menjaga keamanan proyek. Setiap kali server dijalankan, Django akan membaca settings.py untuk memastikan seluruh komponen proyek dapat berjalan sesuai dengan konfigurasi yang telah ditentukan.

4. Cara kerja migrasi database di Django:
    Migrasi database di Django bekerja sebagai cara untuk menerjemahkan perubahan yang kita buat pada model di models.py ke dalam bentuk perubahan struktur tabel di database. Setiap kali kita menambahkan, mengubah, atau menghapus atribut pada model, Django akan mencatat perubahan itu dalam file migrasi menggunakan perintah 'python manage.py makemigrations'. Setelah itu, perintah python manage.py migrate dijalankan untuk benar-benar menerapkan perubahan tersebut ke dalam database. Dengan mekanisme ini, struktur database selalu sesuai dengan model yang ada di proyek Django.

5. Pendapat mengenai mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak:
    Menurut saya, Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena framework ini memiliki struktur yang jelas, terorganisir, dan lengkap sehingga memudahkan pemula untuk memahami alur kerja sebuah aplikasi web. Django sudah menyediakan banyak fitur bawaan seperti autentikasi, manajemen database, serta sistem template, sehingga mahasiswa bisa lebih fokus belajar konsep dasar pengembangan perangkat lunak tanpa harus membangun semuanya dari nol. Selain itu, Django juga menggunakan bahasa Python yang sintaksnya sederhana dan mudah dipahami, sehingga cocok sebagai titik awal sebelum mendalami framework lain yang lebih kompleks.

6. Feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    Tidak ada.