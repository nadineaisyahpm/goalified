JAWABAN TUGAS 3 PBP
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Jawaban: Data delivery penting agar server dapat mengirim informasi ke client atau aplikasi lain dengan cara yang terstruktur dan mudah digunakan. Contohnya apabila aplikasi butuh menampilkan daftar produk, data harus dikirim dalam format yang bisa dibaca dan diproses oleh front-end. Dengan data delivery, integrasi antar-platform akan lebih mudah, sebagai contoh API bisa digunakan oleh aplikasi lain tanpa harus membuat ulang backend.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Kenapa JSON lebih populer?
Jawaban: Menurut saya, JSON lebih praktis untuk kebanyakan aplikasi web modern. Formatnya lebih ringkas, mudah dibaca, dan mudah diolah, terutama jika memakai JavaScript. XML memiliki kelebihan apabila kita membutuhkan validasi struktur yang kompleks, namun biasanya terlalu berbelit-belit. Oleh karena itu, JSON lebih sering digunakan untuk API dan data transfer karena cepat dan ringan.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Jawaban: Fungsi is_valid() digunakan untuk memeriksa apakah data yang diisi user sesuai aturan form. Contohnya memeriksa apakah setiap field yang wajib diisi oleh user tidak kosong dan tipe data yang digunakan sesuai. Apabila tidak valid, form tidak akan disimpan ke database. Jadi, method ini penting untuk mencegah user agar tidak memasukkan data error atau kosong yang bisa membuat aplikasi bermasalah.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Jawaban: csrf_token digunakan untuk mencegah serangan CSRF (Cross-Site Request Forgery). Tanpa token ini, attacker dapat membuat request palsu dari browser user yang sedang login, misalnya untuk mengubah data secara ilegal/tanpa izin. Dengan adanya token, setiap request form akan dicek terlebih dahulu ke server, sehingga serangan tersebut dapat dicegah.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawaban: Melanjutkan dari Tugas 2 PBP saya, berikut adalah langkah-langkah implementasi yang saya lakukan:

            1. Membuat model Product dan forms.py
            -> Pertama, saya membuka models.py di app main yang sudah diisi oleh field-field yang dibutuhkan dari Tugas 2 PBP sebelumnya. Selanjutnya, saya membuat forms.py di app main. Di situ, saya membuat class ProductForm yang menggunakan ModelForm Django, sehingga semua field di Product bisa digunakan untuk membuat form input data produk. Ini akan memudahkan saya menambahkan produk baru melalui halaman web.

            2. Menambahkan views di views.py
            -> Setelah itu, saya menambahkan views di views.py. Saya mulai dari view untuk tampilan:
                - product_list untuk menampilkan semua produk,
                - product_detail untuk menampilkan detail satu produk,
                - add_product untuk menampilkan form tambah produk dan menyimpan data ke database.

                Selain itu, saya juga menambahkan views untuk API:
                - show_json dan show_xml untuk menampilkan semua produk dalam format JSON atau XML,
                - show_json_by_id dan show_xml_by_id untuk menampilkan satu produk berdasarkan ID.

            3. Menambahkan routing URL di main/urls.py
            -> Kemudian, saya membuka urls.py di app main. Saya menambahkan route untuk semua view yang sudah dibuat, termasuk URL untuk API. Saya juga menambahkan app_name = 'main' di bagian atas agar saya dapat menggunakan namespace ketika membuat link di template, sehingga {% url 'main:product_list' %} dan sejenisnya bisa bekerja dengan benar.

            4. Membuat template HTML
            -> Setelah itu, saya membuat template HTML. Pertama, saya membuat base.html sebagai kerangka umum halaman web dengan block {% block content %} agar dapat saya extend. Lalu saya membuat:

            - product_list.html, yang menampilkan daftar produk lengkap dengan tombol “Tambah Produk” dan tombol “Lihat Detail” di setiap produk
            - product_detail.html, untuk menampilkan detail lengkap satu produk serta tombol kembali ke daftar produk
            - add_product.html, untuk menampilkan form input produk baru lengkap dengan tombol submit dan tombol kembali

            Setelah semua template siap, saya menjalankan server menggunakan python manage.py runserver dan membuka halaman web di browser. Saya memeriksa semua halaman: daftar produk, detail produk, dan form tambah produk, untuk memastikan semuanya bekerja dengan benar.

            5. Memeriksa hasil request JSON dan XML menggunakan Postman
            -> Setelah itu, saya mencoba API JSON dan XML menggunakan Postman. Saya mengakses semua URL yang tersedia, yaitu /json/, /xml/, /json/<id>/, dan /xml/<id>/. Setiap kali berhasil, saya mengambil screenshot hasilnya untuk dimasukkan ke dokumentasi.

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Jawaban: Tidak ada.

7. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
Jawaban: Link Google Drive berisi screenshot dari hasil request keempat URL: https://drive.google.com/drive/folders/1IAQZUN4vrzg6VQm4QPKoLiVQd3WjLneJ?usp=sharing