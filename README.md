# Minpro-2-DDP-SistemPenentuanKategoriBeratBadanBayiBaruLahir<br>

**MINI PROJECT 2 <br>
Nama : Jessica Chatarina Sinaga <br>
NIM : 2609116016<br>
Kelas : A<br>
Tema : Sistem Penentuan Kategori Berat Badan Bayi Baru Lahir<br>**
<br>
**1. Penjelasan mengenai kode program** <br>
Sistem Klasifikasi Kesehatan Bayi adalah sistem yang berfungsi untuk mencatat, mencari, dan mengelompokkan kondisi kesehatan bayi berdasarkan berat badannya secara otomatis (Kurus, Normal, Obesitas). Program ini dilengkapi pembagian hak akses pengguna (Admin dan User) serta fitur statistik ringkas untuk memantau rata-rata berat badan dan rekapitulasi data bayi. <br>
<br>
**2. Flowchart**<br>
_a. Halaman Login_<br>
<img width="867" height="805" alt="Cuplikan layar 2026-10-06 174225" src="https://github.com/user-attachments/assets/a0982178-0a79-4d28-bcff-38013793e6f9" /> <br>
Halaman Login merupakan pintu masuk utama ke dalam sistem yang bertugas memeriksa identitas dan hak akses pengguna sebelum mereka diperbolehkan masuk. Alur dimulai ketika pengguna diminta memasukkan username dan password pada antarmuka program.

Setelah input diterima, sistem secara otomatis mencocokkannya dengan basis data akun yang tersimpan. Jika kombinasi username atau password tidak cocok, sistem akan menolak akses, menampilkan pesan kesalahan, lalu mengarahkan pengguna untuk memilih apakah ingin mencoba login kembali atau keluar dari aplikasi. Sebaliknya, jika data login ditemukan dan valid, sistem akan langsung mengidentifikasi tingkat peran (role) akun tersebut. Pengguna dengan peran Admin akan diteruskan secara otomatis menuju Halaman Admin, sedangkan pengguna dengan peran User akan diarahkan masuk ke Halaman User. <br>
<br>
_b. Halaman Admin_<br>
<img width="1901" height="812" alt="Cuplikan layar 2026-10-06 183626" src="https://github.com/user-attachments/assets/91cb54c6-b766-429e-88fe-ac8a10eb3066" /> <br>
<img width="1901" height="808" alt="Cuplikan layar 2026-10-06 183651" src="https://github.com/user-attachments/assets/88cf0fe8-1387-4e43-9e37-736a9d5fdac3" /> <br>

Halaman Admin merupakan pusat kendali dengan hak akses penuh yang ditujukan untuk pengelolaan data secara menyeluruh. Begitu berhasil masuk, layar akan menampilkan daftar menu utama yang berisi tujuh pilihan tindakan.

Alur kerja pada halaman ini berjalan dalam sebuah lingkaran interaktif (looping). Apabila Admin memilih opsi pertama, sistem akan menjalankan fungsi penambahan data bayi baru dengan menghitung kategori kesehatan secara otomatis dari berat badan yang diinputkan. Jika memilih opsi kedua, sistem menampilkan tabel berisi seluruh catatan bayi. Opsi ketiga dan keempat masing-masing memproses pembaruan informasi dan penghapusan data berdasarkan kode identitas bayi. Opsi kelima berfungsi melakukan pencarian spesifik menggunakan kata kunci nama, sementara opsi keenam mengolah dan menampilkan kalkulasi statistik seperti rata-rata berat badan serta rekapitulasi kategori. Setelah setiap tindakan selesai dijalankan, aliran sistem akan selalu kembali ke tampilan menu Admin hingga pengguna memutuskan untuk memilih opsi ketujuh, yaitu keluar akun untuk berpindah ke Halaman Logout.<br>
Untuk materi lebih lanjut, berikut penjelasan mengenai setiap menu yang ada pada halaman admin : <br>
1. Tambahkan Data Bayi<br>
<img width="1615" height="242" alt="Cuplikan layar 2026-10-06 184608" src="https://github.com/user-attachments/assets/762740e7-ff80-4ab2-9d1c-1109715d620c" /> <br>
Menu ini berfungsi untuk memasukkan data fisik bayi baru ke dalam sistem dengan pembuatan kode identitas unik dan pencatatan tanggal input yang berjalan secara otomatis. Saat pengisian, Admin wajib memasukkan nama dan berat badan bayi, di mana sistem menerapkan validasi input yang ketat untuk mencegah data abnormal. Jika Admin menekan tombol Enter tanpa mengisi nama, memasukkan teks non-angka pada berat badan, atau menginput angka nol maupun nilai negatif, sistem akan menolak data tersebut, menampilkan pesan kesalahan spesifik, dan mengulang permintaan input hingga seluruh informasi terisi dengan benar sebelum secara otomatis mengkategorikan kondisi kesehatan bayi. Setelah seluruh proses pengisian berhasil diselesaikan, sistem akan menampilkan pesan konfirmasi penambahan data dan secara otomatis mengembalikan alur program ke tampilan menu utama Admin.<br>
2. Tampilkan Seluruh Data Bayi<br>
<img width="1607" height="219" alt="Cuplikan layar 2026-10-06 185450" src="https://github.com/user-attachments/assets/757446b0-0d20-46e9-904d-11c32235b94f" /> <br>
Menu ini bertugas menyajikan seluruh rekaman data kesehatan bayi yang tersimpan ke dalam format tabel rapi yang mencakup kode identitas, nama, berat badan, kategori kesehatan, dan tanggal pencatatan. Alur kerja menu ini murni bersifat pembacaan data tanpa mengubah isi basis data sama sekali. Apabila seluruh data telah dihapus atau memang belum ada data yang dimasukkan sejak awal, sistem tidak akan menampilkan tabel kosong melainkan memberi pemberitahuan bahwa belum ada data bayi yang disimpan. Begitu pencetakan tabel atau pesan pemberitahuan selesai ditampilkan ke layar, alur program akan langsung dialihkan kembali ke tampilan menu utama Admin. <br>
3. Ubah Data Bayi<br>
<img width="1785" height="298" alt="Cuplikan layar 2026-10-06 185745" src="https://github.com/user-attachments/assets/d3fb8916-2c7e-4bc0-9413-cd78b40110ac" /> <br>
Menu ini digunakan untuk memperbarui nama atau berat badan dari rekaman data bayi yang sudah ada di dalam sistem. Sebelum melakukan perubahan, sistem menampilkan daftar seluruh data bayi agar Admin dapat menginput kode identitas target, di mana Admin diberi opsi untuk membatalkan proses kapan saja cukup dengan mengetik kata 'batal'. Apabila kode identitas yang diinput tidak terdaftar, sistem akan menampilkan pesan kesalahan dan meminta penginputan ulang, sedangkan jika Admin tidak ingin mengubah salah satu kolom data, Admin cukup menekan tombol Enter untuk mempertahankan nilai lama, dan jika berat badan diperbarui maka kategori kesehatan bayi akan dihitung ulang secara otomatis. Baik setelah data berhasil diperbarui maupun ketika Admin memilih opsi batal, seluruh proses akan ditutup dengan mengembalikan alur program ke tampilan menu utama Admin.<br>
4. Hapus Data Bayi <br>
<img width="1895" height="304" alt="Cuplikan layar 2026-10-06 185949" src="https://github.com/user-attachments/assets/7422ba7f-253b-480a-88eb-8ebd849070dd" /> <br>
Menu ini berfungsi untuk menghapus satu catatan data bayi dari basis data secara permanen berdasarkan kode identitas yang dipilih. Setelah Admin memasukkan kode identitas target, sistem tidak langsung membuang data melainkan menyajikan tahap konfirmasi ulang untuk memastikan keputusan Admin. Apabila Admin mengetik kata 'batal' di awal atau memberikan jawaban selain kata 'ya' pada tahap konfirmasi, sistem akan menghentikan proses penghapusan, menampilkan pesan pembatalan, dan menjaga data tetap aman di dalam basis data. Setelah tindakan penghapusan berhasil dikonfirmasi atau dibatalkan, alur program akan secara otomatis kembali ke tampilan menu utama Admin. <br>
5. Cari Data Bayi <br>
<img width="1894" height="191" alt="Cuplikan layar 2026-10-06 190135" src="https://github.com/user-attachments/assets/52808b54-076f-49ce-b0b5-3fed6f1720b6" /> <br>
Menu ini memudahkan Admin dalam menemukan catatan bayi tertentu secara cepat berdasarkan pencarian kata kunci nama. Proses pencarian ini bersifat fleksibel karena tidak membedakan penggunaan huruf besar maupun huruf kecil serta mampu mencocokkan potongan kata. Apabila nama yang dicari tidak ada di dalam basis data, sistem tidak akan menampilkan tabel melainkan memberi pemberitahuan bahwa data bayi dengan kata kunci tersebut tidak ditemukan. Setelah hasil pencarian atau pesan tidak ditemukan selesai ditampilkan, sistem akan langsung mengarahkan alur program kembali ke tampilan menu utama Admin. <br>
6. Lihat Statistik Ringkas <br>
<img width="1865" height="131" alt="Cuplikan layar 2026-10-06 190340" src="https://github.com/user-attachments/assets/e1075953-a696-442d-94df-72c2de32c13c" /> <br>
Menu ini menyajikan rekapitulasi analisis angka dari seluruh data bayi yang terdaftar, seperti menghitung total populasi, rata-rata berat badan beserta pembulatannya ke atas dan ke bawah, hingga jumlah bayi pada tiap kategori kesehatan. Untuk mengantisipasi terjadinya kesalahan sistem akibat pembagian angka nol saat menghitung rata-rata, fungsi ini secara otomatis memeriksa ketersediaan data di awal. Jika basis data dalam keadaan kosong, sistem akan membatalkan perhitungan matematis dan langsung menampilkan pesan bahwa belum ada data untuk dihitung statistiknya. Selesai menyajikan ringkasan statistik atau pesan pembatalan tersebut, alur program akan secara otomatis dialihkan kembali ke tampilan menu utama Admin. <br>
7. Keluar akun<br>
<img width="1271" height="483" alt="Cuplikan layar 2026-10-06 190613" src="https://github.com/user-attachments/assets/0bde7c7d-d08e-4377-b2c5-8cb2411a780a" /> <br>
Menu ini berfungsi untuk mengakhiri sesi kerja Admin secara aman dengan melepaskan seluruh hak akses pengguna pada sesi tersebut. Begitu menu ini dipilih, perulangan pada dashboard Admin akan dihentikan (break) dan alur program tidak dikembalikan ke menu utama Admin, melainkan secara khusus diteruskan ke Halaman Logout untuk memberikan pilihan login ulang atau menghentikan aplikasi sepenuhnya. Selain itu, apabila Admin memasukkan angka di luar rentang pilihan satu sampai tujuh pada tampilan menu utama, sistem akan menolak input tersebut, memberikan pesan peringatan bahwa pilihan tidak valid, lalu memuat ulang dan mengembalikan tampilan ke menu utama Admin dari awal tanpa merusak jalannya program. <br>
<br>
_c. Halaman User_<br>
<img width="918" height="803" alt="Cuplikan layar 2026-10-06 183223" src="https://github.com/user-attachments/assets/ccd252e1-14f0-4581-97c7-9eacf483a51f" /> <br>
Halaman User dirancang khusus bagi pengguna operasional (seperti Bidan atau Suster) yang membutuhkan akses informasi tanpa hak untuk mengubah atau menghapus data (Read-Only). Setelah proses login berhasil mengonfirmasi peran sebagai User, antarmuka akan menyajikan menu terbatas yang terdiri dari empat pilihan.

Alur di halaman ini difokuskan pada penyajian dan analisis data. Jika User memilih opsi pertama, sistem akan mencetak seluruh daftar data kesehatan bayi ke layar. Jika memilih opsi kedua, program mengeksekusi fungsi pencarian data berdasarkan nama bayi yang diinputkan. Opsi ketiga akan menampilkan ringkasan statistik kesehatan seperti jumlah populasi dan rata-rata berat badan secara instan. Sama seperti pada halaman Admin, setiap kali operasi selesai diproses, alur program akan kembali menyajikan menu utama User. Proses ini berulang hingga User memilih opsi keempat untuk keluar dari akun dan menuju Halaman Logout.<br>
Pembahasan lebih lanjut mengenai menu yang ada pada halaman user, sebagai berikut : <br>
1. Tampilkan Seluruh Data Bayi<br>
<img width="1341" height="429" alt="Cuplikan layar 2026-10-06 193125" src="https://github.com/user-attachments/assets/4a1b7db9-a154-4e20-adcc-98d0868c424d" /> <br>
Fungsi ini dirancang untuk menyajikan keseluruhan catatan riwayat kesehatan bayi dalam susunan tabel terstruktur yang memuat identitas, nama, berat badan, status kesehatan, serta tanggal input. Karena diakses oleh User (seperti Bidan atau Suster), operasi pada fungsi ini murni bersifat pembacaan data tanpa menyediakan opsi untuk menambah, merubah, atau menghapus informasi. Seandainya seluruh record terhapus atau memang belum ada entri sama sekali, sistem tidak akan mencetak tabel kosong melainkan menampilkan pemberitahuan bahwa data masih belum tersedia. Begitu pesan atau tabel usai ditampilkan di layar, alur program akan secara otomatis kembali dialihkan ke halaman menu utama User. <br>
2. Cari Data Bayi<br>
<img width="1431" height="200" alt="Cuplikan layar 2026-10-06 193256" src="https://github.com/user-attachments/assets/5256a9a4-83e8-42be-8f17-0c86dfed85b6" /> <br>
Fungsi ini membantu User menemukan rekaman data bayi secara presisi hanya dengan memasukkan kata kunci nama tanpa harus membaca seluruh tabel. Mekanisme pencarian bekerja secara fleksibel karena mampu mengenali potongan kata serta tidak membedakan penggunaan huruf kapital maupun huruf kecil (case-insensitive). Apabila pencarian tidak menemukan nama yang sesuai di dalam basis data, sistem akan mengeluarkan instruksi peringatan bahwa entri yang dicari tidak ada. Begitu hasil pencocokan atau pesan tidak ditemukan selesai ditampilkan di layar, sistem langsung mengembalikan navigasi program ke menu utama User. <br>
3. Lihat Statistik Singkat<br>
<img width="1461" height="246" alt="Cuplikan layar 2026-10-06 193806" src="https://github.com/user-attachments/assets/2e38da75-06b2-4341-a34f-37d32cc6b155" /> <br>
Fungsi ini menyajikan rekapitulasi data secara kuantitatif untuk pemantauan, seperti kalkulasi jumlah populasi bayi terdaftar, hitungan rata-rata berat badan beserta pembulatannya ke atas dan ke bawah, hingga rekap jumlah bayi pada setiap kategori kesehatan. Untuk menghindari kegagalan sistem akibat perhitungan matematika pembagian dengan angka nol ketika data kosong, fungsi ini melakukan pemeriksaan ketersediaan record di awal. Jika basis data terdeteksi kosong, sistem akan menghentikan proses kalkulasi dan memunculkan pemberitahuan bahwa statistik belum dapat dihitung. Setelah sajian statistik atau pesan pembatalan selesai ditampilkan, alur program akan otomatis berpindah kembali ke menu utama User.<br>
4. Keluar Akun <br>
<img width="495" height="755" alt="Cuplikan layar 2026-10-06 194035" src="https://github.com/user-attachments/assets/fdc74773-8f98-4daf-91c6-789496085b91" /> <br>
Fungsi ini digunakan untuk menyelesaikan sesi kerja User secara aman dengan memutus hak akses akun pada sesi yang sedang berjalan. Saat opsi ini dieksekusi, perulangan menu User akan dihentikan (break) dan alur program tidak diarahkan balik ke menu utama User, melainkan secara khusus dialihkan menuju Halaman Logout untuk menentukan apakah ingin masuk kembali atau menutup program. Selain itu, seandainya User menginput angka di luar rentang satu sampai empat pada navigasi dashboard, sistem akan menolak perintah tersebut, memunculkan notifikasi bahwa pilihan tidak valid, lalu memuat ulang dan mengembalikan tampilan ke menu utama User tanpa mengganggu stabilitas program.<br>

_d. Halaman Keluar_<br>
<img width="758" height="785" alt="Cuplikan layar 2026-10-06 184250" src="https://github.com/user-attachments/assets/c8b0daba-4b8a-46fd-bd6e-bd4c344caff0" /> <br>
Halaman Logout merupakan bagian penutup yang menangani proses pengakhiran sesi pengguna serta terminasi aplikasi. Alur ini dipicu ketika pengguna baik dari Halaman Admin maupun Halaman User memilih opsi menu keluar akun.

Begitu pengguna memilih opsi keluar akun dari menu utama, sistem akan memutus hak akses sesi yang aktif, menampilkan pesan konfirmasi bahwa akun telah berhasil keluar, dan mengarahkan alur ke dialog validasi ulang. Pada tahap ini, pengguna diberikan pertanyaan apakah ingin mencoba masuk (login) kembali ke sistem atau tidak; apabila pengguna menjawab 'ya', sistem akan me-load ulang alur dan mengembalikan tampilan ke Halaman Login awal, sedangkan jika pengguna menjawab 'tidak', sistem akan menampilkan ucapan terima kasih dan secara resmi menutup seluruh alur program (End). Selain itu, jika pengguna memasukkan jawaban selain kata 'ya' atau 'tidak' pada dialog pilihan ulang tersebut, sistem akan menolak input, mengeluarkan notifikasi peringatan agar menjawab sesuai instruksi, lalu memuat ulang pertanyaan validasi tanpa memutus alur keluar program. <br>
<br>
**3. Kode Program** <br>
<img width="349" height="80" alt="Cuplikan layar 2026-10-06 202407" src="https://github.com/user-attachments/assets/c4f4c3ff-44ff-4e98-8c8c-8def606743c3" /> <br>
Bagian awal dari kode program ini diawali dengan mengimpor pustaka standar dan modul eksternal Python yang dibutuhkan oleh aplikasi. Library **datetime** diimpor untuk memproses serta mengambil tanggal saat ini secara otomatis ketika sistem mencatat data bayi baru. Library **pwinput** digunakan untuk mengamankan proses penginputan kata sandi agar karakter yang diketik oleh pengguna disamarkan di layar monitor. Sementara itu, **Library** math diimpor untuk menyediakan fungsi-fungsi perhitungan matematika khusus, seperti operasi pembulatan nilai rata-rata berat badan ke atas maupun ke bawah. <br>
<img width="1303" height="714" alt="Cuplikan layar 2026-10-06 203406" src="https://github.com/user-attachments/assets/cbed6d5f-05dc-4b38-8028-1d6c776bc634" /> <br>
Kode program menetapkan dua variabel dictionary utama yang berfungsi sebagai basis data sementara di dalam memori. Variabel data_pengguna menyimpan daftar kredensial akun yang diberi hak akses ke dalam aplikasi, termasuk informasi nama pengguna, kata sandi, peran akses, dan nama lengkap pemilik akun. Variabel data_bayi berfungsi untuk menampung seluruh rekam medis awal bayi baru lahir, di mana setiap entri data memiliki kunci unik seperti BAYI1 dan memuat rincian nama, berat badan, kategori kesehatan, serta tanggal pertama kali data dicatat. <br>
<img width="1087" height="231" alt="Cuplikan layar 2026-10-06 203715" src="https://github.com/user-attachments/assets/54afbe0c-cb55-49dc-b8cb-40ee2357a799" /> <br>
Fungsi tentukan_kategori_kesehatan dirancang untuk mengklasifikasikan kondisi fisik bayi berdasarkan parameter berat badan yang dimasukkan. Fungsi ini menerapkan struktur percabangan logis untuk mengevaluasi nilai berat badan: jika berat badan berada di bawah 2,5 kilogram maka fungsi akan mengembalikan kategori "Kurus", jika berada di rentang 2,5 hingga 4,0 kilogram akan dikategorikan sebagai "Normal", dan jika melebihi 4,0 kilogram maka akan dikategorikan sebagai "Obesitas atau Gemuk".<br>
<img width="1052" height="599" alt="Cuplikan layar 2026-10-06 203846" src="https://github.com/user-attachments/assets/605a3f72-b989-496d-a99b-04d7258a7468" /> <br>
Fungsi sistem_masuk_akun bertugas menangani seluruh alur autentikasi dan validasi hak akses pengguna saat aplikasi dijalankan. Fungsi ini akan menampilkan antarmuka halaman masuk akun, lalu meminta pengguna untuk memasukkan nama pengguna serta kata sandi. Penginputan kata sandi diproses menggunakan perintah pwinput yang dilengkapi dengan penanganan pengecualian (exception handling) untuk mengantisipasi potensi kegagalan sistem. Jika nama pengguna dan kata sandi yang dimasukkan cocok dengan data di data_pengguna, fungsi ini akan mengembalikan identitas, peran, dan nama lengkap pengguna; sebaliknya, jika tidak cocok, fungsi akan mengembalikan nilai kosong (None).<br>
<img width="1692" height="541" alt="Cuplikan layar 2026-10-06 204114" src="https://github.com/user-attachments/assets/0ab8e350-69d6-4c1e-818e-738c85b89902" /> <br>
Fungsi tampilkan_seluruh_data berfungsi untuk menyajikan seluruh rekam medis bayi yang tersimpan di dalam sistem ke dalam bentuk tabel yang rapi di layar terminal. Fungsi ini pertama-tama memverifikasi apakah terdapat data bayi yang tersimpan. Apabila data tersedia, fungsi akan mencetak header tabel dan melakukan pemformatan spasi teks sedemikian rupa agar kolom identitas, nama, berat badan, kategori kesehatan, dan tanggal pencatatan teratur secara simetris.<br>
<img width="1236" height="818" alt="Cuplikan layar 2026-10-06 204428" src="https://github.com/user-attachments/assets/0932a83e-68f3-4bd7-bf95-5efa613a5461" /> <br>
Fungsi ini digunakan untuk menambahkan rekam medis bayi baru ke dalam dictionary data_bayi. Fungsi ini secara otomatis membuatkan kode identitas baru secara berurutan, melakukan validasi agar nama bayi tidak dikosongkan, serta memastikan nilai berat badan yang diinput berupa angka positif. Setelah variabel berat badan tervalidasi, fungsi akan memanggil tentukan_kategori_kesehatan dan mencatat tanggal sistem hari ini sebelum menyimpan entri baru tersebut. <br>
<img width="1014" height="506" alt="Cuplikan layar 2026-10-06 205147" src="https://github.com/user-attachments/assets/5bad6872-29c2-407b-aaff-91f8a5de8b8a" /> <br>
<img width="1039" height="656" alt="Cuplikan layar 2026-10-06 205214" src="https://github.com/user-attachments/assets/60ca21bb-2932-453c-b2cf-4539d1bac436" /> <br>
Fungsi ini memfasilitasi proses penyesuaian atau perbaikan data bayi yang sudah tersimpan sebelumnya. Setelah pengguna memilih kode identitas bayi yang ingin diperbarui, fungsi ini memberikan fleksibilitas untuk mengubah nama atau berat badan. Jika pengguna menekan tombol Enter tanpa memasukkan nilai baru, sistem secara otomatis akan mempertahankan data lama. Apabila berat badan diperbarui, fungsi juga akan secara otomatis menghitung ulang kategori kesehatan bayi tersebut.<br>
<img width="1067" height="743" alt="Cuplikan layar 2026-10-06 205354" src="https://github.com/user-attachments/assets/4ff334ce-053c-4fde-97bb-9a2e8ad1431a" /> <br>
Fungsi ini bertugas untuk menghapus entri data bayi tertentu dari sistem penyimpanan. Fungsi ini meminta pengguna memasukkan kode identitas target yang ingin dihapus, lalu menampilkan dialog konfirmasi tindakan guna mencegah penghapusan data secara tidak sengaja. Jika konfirmasi disetujui, entri data tersebut akan dihapus dari dictionary data_bayi. <br>
<img width="1836" height="562" alt="Cuplikan layar 2026-10-06 205530" src="https://github.com/user-attachments/assets/5723b257-ad1a-475a-a89d-cdb043ad0cff" /> <br>
Fungsi ini memungkinkan pengguna untuk menemukan rekam medis bayi tertentu berdasarkan kata kunci nama. Fungsi ini memanfaatkan teknik dictionary comprehension dan penyesuaian huruf kecil (lowercase) sehingga pencarian bersifat fleksibel dan dapat menemukan nama bayi meskipun pengguna hanya mengetikkan sebagian huruf dari nama tersebut. <br>
<img width="1555" height="746" alt="Cuplikan layar 2026-10-06 205735" src="https://github.com/user-attachments/assets/c020bcc5-f47b-4dfe-99cc-cb5532afe311" />
Fungsi ini mengolah seluruh data rekam medis untuk menyajikan ringkasan informasi kuantitatif. Fungsi ini menghitung jumlah total bayi terdaftar, menghitung nilai rata-rata berat badan seluruh bayi, serta memanfaatkan fungsi math.ceil dan math.floor untuk menunjukkan hasil pembulatan angka rata-rata tersebut ke atas dan ke bawah. Selain itu, fungsi ini juga menghitung akumulasi total bayi pada masing-masing kategori kesehatan. <br>
<img width="988" height="825" alt="Cuplikan layar 2026-10-06 205903" src="https://github.com/user-attachments/assets/36db7775-d3ae-4898-bf9e-06929318f8ad" /> <br>
Fungsi ini menyajikan antarmuka menu interaktif khusus untuk pengguna berstatus Admin. Melalui menu ini, Admin diberikan akses penuh terhadap 7 opsi tindakan, yang meliputi penambahan data, penampilkan seluruh data, pengubahan data, penghapusan data, pencarian data, peninjauan statistik ringkas, hingga opsi untuk keluar dari akun.<br>
<img width="980" height="642" alt="Cuplikan layar 2026-10-06 210010" src="https://github.com/user-attachments/assets/e0f80248-a122-48a9-97c5-988755980557" /> <br>
Fungsi ini menyajikan antarmuka menu yang lebih terbatas khusus untuk pengguna berstatus User biasa (seperti Bidan atau Suster). Pengguna pada peran ini hanya diberikan akses terhadap 4 opsi tindakan yang bersifat non-destruktif, yaitu menampilkan data, mencari data, melihat statistik ringkas, dan keluar dari akun, tanpa diberi hak untuk menambah, mengubah, atau menghapus data.<br>
<img width="1029" height="775" alt="Cuplikan layar 2026-10-06 210057" src="https://github.com/user-attachments/assets/5af654a3-7a40-48a7-91d8-0382788296ce" /> <br>
Program terakhir ini dibagi menjadi 2 bagian yang mengendalikan program dari awal hingga akhir<br>
Fungsi program_utama bertindak sebagai penggerak utama aplikasi yang menjalankan perulangan login. Fungsi ini akan memanggil sistem_masuk_akun, mengevaluasi status keberhasilan masuk akun, dan mengarahkan pengguna ke menu_Admin atau menu_User sesuai dengan peran masing-masing. Apabila pengguna memilih untuk keluar dari menu atau gagal masuk akun, fungsi ini akan memberikan pertanyaan konfirmasi apakah pengguna ingin mencoba masuk akun kembali atau menghentikan program sepenuhnya.

**Blok if __name__ == "__main__"** Blok ini merupakan titik masuk (entry point) standar dalam pemrograman Python yang memastikan bahwa fungsi program_utama() hanya akan langsung dieksekusi apabila berkas kode ini dijalankan sebagai program utama, dan tidak akan berjalan secara otomatis apabila berkas ini diimpor oleh berkas kode lain.<br>
<br>
**4. Output**<br>
a. Halaman Login<br>
<img width="836" height="593" alt="Cuplikan layar 2026-10-06 211648" src="https://github.com/user-attachments/assets/33039e7a-de6b-4502-90d2-5cfa82f402e1" /> <br>
Keluaran di atas muncul saat aplikasi pertama kali dijalankan. Sistem mencetak header antarmuka masuk akun, menyamarkan kata sandi dengan karakter bintang (*) saat diketik, lalu mencetak pesan pemberitahuan berwarna/berformat sukses yang mengonfirmasi bahwa pengguna telah berhasil masuk menggunakan akun ADMIN beserta nama lengkapnya.<br>

<img width="721" height="361" alt="Cuplikan layar 2026-10-06 211715" src="https://github.com/user-attachments/assets/b25b43ef-2f4d-4f71-8fe5-a44c9814a061" /> <br>
Keluaran ini dihasilkan jika nama pengguna atau kata sandi yang dimasukkan tidak cocok dengan basis data_ data_pengguna_. Sistem mencetak peringatan gagal login dan langsung menyajikan pertanyaan konfirmasi interaktif untuk memberikan kesempatan kepada pengguna apakah ingin mencoba login kembali atau menghentikan program. <br>

<img width="746" height="508" alt="Cuplikan layar 2026-10-06 211730" src="https://github.com/user-attachments/assets/f824743c-2640-4fb3-9dc3-bc4c90794281" /> <br>
Jika kita memilih 'ya', kita akan diminta untuk memasukkan kembali nama pengguna dan kata sandi untuk dapat masuk ke program.<br>

<img width="742" height="325" alt="Cuplikan layar 2026-10-06 211804" src="https://github.com/user-attachments/assets/f7a86b0f-a143-452f-827a-2b7140f956b8" /> <br>
Namun, jika kita memilih tidak, program akan selesai.<br>

<img width="634" height="348" alt="Cuplikan layar 2026-10-06 213602" src="https://github.com/user-attachments/assets/373386ec-88be-4392-a7b8-75b0e8c02212" /> <br>
Keluaran ini ditampilkan jika akun yang masuk memiliki peran (role) sebagai admin. Menu ini menyajikan 7 pilihan aksi lengkap, termasuk fitur-fitur manipulasi data tingkat tinggi seperti menambah, mengubah, dan menghapus rekam medis bayi.<br>

<img width="586" height="272" alt="Cuplikan layar 2026-10-06 214045" src="https://github.com/user-attachments/assets/1fed8885-ef6c-4c34-92d1-03ad27b3fdce" /> <br>
Keluaran ini ditampilkan jika akun yang masuk memiliki peran sebagai user biasa. Opsi menu dibatasi hanya 4 pilihan yang bersifat non-destruktif (hanya dapat membaca/melihat data), tanpa menyertakan opsi untuk menambah, mengubah, atau menghapus data. <br>

<img width="1002" height="499" alt="Cuplikan layar 2026-10-06 214326" src="https://github.com/user-attachments/assets/a7c80618-88d5-40d4-b7cb-3c13fa8d1da9" /> <br>
Output ini muncul setelah admin memasukkan nama dan berat badan bayi baru secara valid. Sistem secara otomatis membuatkan kode identitas berurutan (BAYI4), mengklasifikasikan berat badan 2.8 kg ke dalam kategori "Normal", dan mencetak konfirmasi bahwa data berhasil tersimpan.<br>
<img width="970" height="630" alt="Cuplikan layar 2026-10-06 215117" src="https://github.com/user-attachments/assets/4171d256-3ada-4421-a5ca-0ea5cfd5bfe5" /> <br>
Keluaran di atas merupakan hasil dari fungsi tampilkan_seluruh_data. Sistem menampilkan header tabel beserta baris data rekam medis bayi yang tersimpan. Penggunaan format string berbasis lebar kolom membuat tampilan teks, angka desimal berat badan, dan tanggal tersusun dengan rapi dan simetris di layar terminal. <br>

<img width="986" height="729" alt="Cuplikan layar 2026-10-06 215347" src="https://github.com/user-attachments/assets/f0fc5cf0-12ab-4522-bfcd-e6e98152e05c" /> <br> 
Output ini menampilkan alur pembaruan data. Sistem menampilkan data lama di dalam tanda kurung siku [...] sebagai acuan. Pengguna memperbarui nama menjadi "Somat" dan berat badan menjadi 3 kg, yang secara otomatis memicu pembaruan kategori kesehatan di dalam basis data. <br>


<img width="1003" height="425" alt="Cuplikan layar 2026-10-06 215639" src="https://github.com/user-attachments/assets/514b194c-c781-402c-8b7f-70ced42d25ab" /> <br>
Keluaran ini memperlihatkan alur penghapusan data. Setelah identitas target BAYI2 dimasukkan, sistem menampilkan pesan konfirmasi terlebih dahulu. Setelah pengguna menjawab "ya", sistem menghapus entri tersebut dan menampilkan konfirmasi sukses penghapusan.<br>

<img width="971" height="525" alt="Cuplikan layar 2026-10-06 215755" src="https://github.com/user-attachments/assets/93e66ade-ecbe-48fa-8e1d-2d6b98bc8588" /> <br>
Keluaran ini dihasilkan oleh fungsi cari_data_bayi. Sistem melakukan pencarian kata kunci secara case-insensitive (tidak membedakan huruf besar/kecil) dan menampilkan entri data yang cocok ke dalam bentuk tabel terbatas. <br>

<img width="697" height="438" alt="Cuplikan layar 2026-10-06 215814" src="https://github.com/user-attachments/assets/dbb46cc3-e1d2-43a3-8b7f-bc2c4a587518" /> <br>
Keluaran ini muncul apabila kata kunci nama yang dicari oleh pengguna tidak cocok dengan seluruh data nama bayi yang ada di dalam sistem.<br>

<img width="891" height="511" alt="image" src="https://github.com/user-attachments/assets/8ebef0c7-aa78-432f-b9a9-f72205a6eb42" /> <br>
Output ini menyajikan ringkasan analisis data kuantitatif seluruh bayi. Sistem menampilkan total bayi terdaftar, nilai rata-rata berat badan beserta hasil pembulatannya menggunakan modul math (floor dan ceil), serta akumulasi jumlah bayi pada tiap-tiap kategori kesehatan.<br>

**Penerapan Nilai Tambahan** :<br>
<br>
1. Validasi Input Menggunakan Error Handling<br>
Penerapan error handling dalam program ini dirancang agar aplikasi tidak langsung terhenti (crash) ketika pengguna memasukkan data yang tidak sesuai tipe data atau formatnya.<br>
<img width="768" height="234" alt="Cuplikan layar 2026-10-06 220725" src="https://github.com/user-attachments/assets/1ce17f89-2487-4ca9-8cfc-c89f02ce1692" /> <br>
Jika pengguna memasukkan angka 0 atau minus (misal -2.5), kondisi if berat_badan <= 0 akan mencegah angka tersebut diproses dan meminta input ulang.<br>

<img width="1210" height="399" alt="Cuplikan layar 2026-10-06 221107" src="https://github.com/user-attachments/assets/617ccb3a-d7b9-499c-bc25-8a18376a8b02" /> <br>
Sistem mengizinkan pengguna mengosongkan input (menekan Enter) jika tidak ingin mengubah berat badan lama.
Jika ada teks yang dimasukkan, blok try-except ValueError bertugas memastikan teks tersebut dapat dikonversi menjadi angka positif secara valid sebelum disimpan.<br>
<br>
2.Penerapan 3 library<br>
<img width="349" height="80" alt="Cuplikan layar 2026-10-06 202407" src="https://github.com/user-attachments/assets/b430147e-591d-41ff-a5a5-23a478b95d58" /> <br>
a. _Fungsi datetime.date.today_ mengambil tanggal lokal dari sistem operasi saat data bayi ditambahkan, kemudian .strftime("%Y-%m-%d") memformatnya menjadi bentuk string standar (Tahun-Bulan-Tanggal) tanpa memerlukan input tanggal manual dari pengguna. <br>
b. _fungsi pwinput_ Menyamarkan karakter kata sandi yang diketikkan pengguna di layar terminal menjadi karakter bintang/asterisk (*), mencegah orang lain melihat kata sandi secara langsung (shoulder surfing).<br>
c._fungsi math_ menggunakan 2 kategori <br>
math.ceil() digunakan untuk melakukan pembulatan nilai desimal rata-rata berat badan ke atas ke bilangan bulat terdekat.<br>
math.floor() digunakan untuk melakukan pembulatan nilai desimal rata-rata berat badan ke bawah ke bilangan bulat terdekat.<br>


