import datetime
import getpass
import math

data_pengguna = {
            "admin": {"kata_sandi": "admin123", "peran": "admin", "nama": "Administrator Klinik"},
            "user": {"kata_sandi": "user123", "peran": "user", "nama": "Bidan Suster"},
        }

data_bayi = {
        "BAYI1": {
            "nama_bayi": "Chika",
            "berat_badan": 2.1,
            "kategori_kesehatan": "Kurus",
            "tanggal_pencatatan": "2026-10-01",
        },
        "BAYI2": {
            "nama_bayi": "Gilbert",
            "berat_badan": 3.2,
            "kategori_kesehatan": "Normal",
            "tanggal_pencatatan": "2026-10-02",
        },
        "BAYI3": {
            "nama_bayi": "Alena",
            "berat_badan": 4.3,
            "kategori_kesehatan": "Obesitas atau Gemuk",
            "tanggal_pencatatan": "2026-10-03",
        },
    }

def tentukan_kategori_kesehatan(berat_badan):
        "Fungsi mengklasifikasikan kondisi fisik bayi berdasarkan berat badan"
        if berat_badan < 2.5:
            return "Kurus"
        elif 2.5 <= berat_badan <= 4.0:
            return "Normal"
        else:
            return "Obesitas atau Gemuk"

def sistem_masuk_akun():
    "Fungsi autentikasi pengguna dengan validasi nama penngguna dan kata sandi"
    print("\n" + "=" * 50)
    print(" SISTEM KLASIFIKASI KESEHATAN BAYI ")
    print(" HALAMAN MASUK AKUN ")
    print("=" * 50)

    nama_pengguna = input("Masukkan Nama Pengguna: ").strip()
    try:
        kata_sandi = getpass.getpass("Masukkan Kata Sandi: ").strip()
    except Exception:
        kata_sandi = input("Masukkan Kata Sandi: ").strip()
    
    if nama_pengguna in data_pengguna:
        if data_pengguna[nama_pengguna]["kata_sandi"] == kata_sandi:
            return (
                nama_pengguna,
                data_pengguna[nama_pengguna]["peran"],
                data_pengguna[nama_pengguna]["nama"],
                )
    return None, None, None

def tampilkan_seluruh_data():
    " Fungsi untuk menampilkan seluruh data kesehatan bayi"
    print("\n" + "-" * 75)
    print("DAFTAR DATA KESEHATAN BAYI BARU LAHIR")
    print("-" * 75)

    if not data_bayi:
        print("Belum ada data bayi yang disimpan.")
        return

    print(
        f"{'Identitas':<10} | {'Nama Bayi':<20} | {'Berat (kg)':<12} | {'Kategori Kesehatan':<20} | {'Tanggal Input':<12}"
        )
    print("-" * 75)
    for identitas_bayi, rincian in data_bayi.items():
            print(
                f"{identitas_bayi:<10} | {rincian['nama_bayi']:<20} | {rincian['berat_badan']:<12.2f} | {rincian['kategori_kesehatan']:<20} | {rincian['tanggal_pencatatan']:<12}"
            )
    print("-" * 75)

def tambah_data_bayi():
    " Fungsi untuk menambah data bayi baru (Akses Admin)"
    print("\n Tambahkan Data Bayi Baru ")

    nomor_urutan = len(data_bayi) + 1
    identitas_baru = f"BAYI{nomor_urutan}"
    while identitas_baru in data_bayi:
        nomor_urutan += 1
        identitas_baru = f"BAYI{nomor_urutan}"

    while True:
        nama_bayi = input("Masukkan Nama Bayi: ").strip()
        if nama_bayi:
            break
        print("Kesalahan: Nama bayi tidak boleh kosong!")

    while True:
        try:
            berat_badan = float(input("Masukkan Berat Badan (Kilogram): "))
            if berat_badan <= 0:
                print("Kesalhan: Berat badan harus lebih dari nol kilogram!")
                continue
            break
        except ValueError:
            print("Kesalahan Input: Harap masukkan angka yang valid!")

    kategori_kesehatan = tentukan_kategori_kesehatan(berat_badan)
    tanggal_hari_ini = datetime.date.today().strftime("%Y-%m-%d")

    data_bayi[identitas_baru] = {
        "nama_bayi": nama_bayi,
        "berat_badan": berat_badan,
        "kategori_kesehatan": kategori_kesehatan,
        "tanggal_pencatatan": tanggal_hari_ini,
    }

    print(
        f"\n[BERHASIL] Data {nama_bayi} dengan Identitas {identitas_baru} berhasil ditambahkan dengan kategori: {kategori_kesehatan}"
    )

def ubah_data_bayi():
    "Fungsi untuk memperbarui data bayi (Akses Admin)"
    print("\n Ubah Data Bayi ")
    if not data_bayi:
        print("Belum ada data bayi yang dapat diubah.")
        return

    tampilkan_seluruh_data()

    while True:
        identitas_target = (
            input("\nMasukkan Identitas Bayi yang ingin diubah (atau ketik 'batal'): ")
            .strip()
            .upper()
        )
        if identitas_target.lower() == "batal":
            return
        if identitas_target in data_bayi:
            break
        print("Kesalahan: Identitas Bayi tidak ditemukan! Periksa kembali tabel di atas.")

    data_lama = data_bayi[identitas_target]
    print(f"\nMengubah Data untuk Identitas: {identitas_target} ({data_lama['nama_bayi']})")

    nama_baru = input(
        f"Nama Baru (Tekan Enter jika tidak diubah [{data_lama['nama_bayi']}])"
    ).strip()
    if not nama_baru:
        nama_baru = data_lama["nama_bayi"]

    while True:
        input_berat = input(
            f"Berat Badan Baru dalam kilogram (Tekan Enter jika tidak diubah [{data_lama['berat_badan']} kg]): "
        ).strip()
        if not input_berat:
            berat_baru = data_lama["berat_badan"]
            break
        try:
            berat_baru = float(input_berat)
            if berat_baru <= 0:
                print("Kesalahan: Berat Badan harus lebih dari nol kilogram!")
                continue
            break
        except ValueError:
            print("Kesalahan Input: Harap Masukkan angka yang valid!")

    kategori_baru = tentukan_kategori_kesehatan(berat_baru)

    data_bayi[identitas_target]["nama_bayi"] = nama_baru
    data_bayi[identitas_target]["berat_badan"] = berat_baru
    data_bayi[identitas_target]["kategori_kesehatan"] = kategori_baru

    print(f"\n[BERHASIL] Data dengan Identitas {identitas_target} berhasil diperbarui!")

def hapus_data_bayi():
    "Fungsi untuk menghapus data bayi (Akses Admin)"
    print("\n Hapus Data Bayi ")
    if not data_bayi:
        print("Belum ada data bayi yang dapat dihapus.")
        return

    tampilkan_seluruh_data()

    while True:
        identitas_target = (
            input("\nMasukkan Identitas Bayi yang ingin dihapus (atau ketik 'batal'):")
            .strip()
            .upper()
        )
        if identitas_target.lower() == "batal" :
            return
        if identitas_target in data_bayi:
            break
        print("Kesalahan: Identitas Bayi Tidak Ditemukan!")

    konfirmasi = (
        input(
            f"Apakah Anda yakin ingin menghapus data {data_bayi[identitas_target]['nama_bayi']}? (ya/tidak): "
        )
        .strip()
        .lower()
    )
    if konfirmasi == "ya":
        data_terhapus = data_bayi.pop(identitas_target)
        print(
            f"\n[BERHASIL] Data bayi '{data_terhapus['nama_bayi']}' dengan Identitas {identitas_target} telah dihapus."
        )
    else:
        print("\n[BATAL] Penghapusan data dibatalkan.")

def cari_data_bayi():
    "Fungsi untuk mencaru data bayi berdasarkan nama"
    print("\n Cari Data Bayi ")
    kata_kunci = input("Masukkan nama bayi yang ingin dicari: ").strip().lower()

    hasil_pencarian = {
        identitas: rincian
        for identitas, rincian in data_bayi.items()
        if kata_kunci in rincian["nama_bayi"].lower()
    }

    if not hasil_pencarian:
        print(f"Tidak ditemukan data bayi dengan nama yang mengandung '{kata_kunci}'.")
    else:
        print(f"\nHasil Pencarian ({len(hasil_pencarian)} data ditemukan):")
        print(
            f"{'Identitas':<10} | {'Nama Bayi':<20} | {'Berat (kg)':<12} | {'Kategori Kesehatan':<20} | {'Tanggal Input':<12}"
        )
        print("-" * 75)
        for identitas_bayi, rincian in hasil_pencarian.items():
            print(
                f"{identitas_bayi:<10} | {rincian['nama_bayi']:<20} | {rincian['berat_badan']:<12.2f} | {rincian['kategori_kesehatan']:<20} | {rincian['tanggal_pencatatan']:<12} "
            )

def statistik_ringkas():
    "Fungsi perhitungan statistik sederhana mengguakan pustaka math"
    print("\n Statistik Ringkas Kesehatan Bayi ")
    if not data_bayi:
        print("Belum ada data untuk dihitung statistiknya.")
        return

    total_bayi = len(data_bayi)
    semua_berat_badan = [rincian["berat_badan"] for rincian in data_bayi.values()]

    rata_rata_berat = sum(semua_berat_badan) / total_bayi
    pembulatan_ke_atas = math.ceil(rata_rata_berat)
    pembulatan_ke_bawah= math.floor(rata_rata_berat)

    jumlah_kurus = sum(
        1 for  rincian in data_bayi.values() if rincian["kategori_kesehatan"] == "Kurus"
    )
    jumlah_normal = sum(
        1 for rincian in data_bayi.values() if rincian["kategori_kesehatan"] == "Normal"
    )
    jumlah_obesitas = sum(
            1 for rincian in data_bayi.values() if rincian["kategori_kesehatan"] == "Obesitas atau Gemuk"
        )

    print(f"Total Bayi Terdaftar : {total_bayi}")
    print(
        f"Rata-rata berat Badan : {rata_rata_berat:.2f} kg (Pembulatan ke bawah: {pembulatan_ke_bawah}, Pembulatan ke atas: {pembulatan_ke_atas})"  
    )
    print(f"- Jumlah Kategori Kurus     : {jumlah_kurus}")
    print(f"- Jumlah Kategori Normal    : {jumlah_normal}")
    print(f"- Jumlah Kategori Obesitas  : {jumlah_obesitas}")

def menu_Admin(nama_lengkap):
    "Menu khusus untuk peran Admin"
    while True:
        print("\n" + "=" * 50)
        print(f" MENU ADMIN - Selamat Datang, {nama_lengkap}")
        print("=" * 50)
        print("1. Tambah Data Bayi")
        print("2. Tampilkan Seluruh Data Bayi")
        print("3. Ubah Data Bayi")
        print("4. Hapus Data Bayi")
        print("5. Cari Data Bayi")
        print("6. Lihat Statistik Ringkas")
        print("7. Keluar Akun")
        print("=" * 50)

        pilihan_menu = input("Pilih menu (1-7): ").strip()

        if pilihan_menu == "1":
            tambah_data_bayi()
        elif pilihan_menu == "2":
            tampilkan_seluruh_data()
        elif pilihan_menu == "3":
            ubah_data_bayi()
        elif pilihan_menu == "4":
            hapus_data_bayi()
        elif pilihan_menu == "5":
            cari_data_bayi()
        elif pilihan_menu == "6":
            statistik_ringkas()
        elif pilihan_menu == "7":
            print(f"\nAdmin '{nama_lengkap}' berhasil keluar dari akun.")
            break
        else:
            print("Kesalahan: Pilihan menu tidak valid! Harap masukkan angka 1 sampai 7.")

def menu_User(nama_lengkap):
    "Menu khusus untuk peran user"
    while True:
        print("\n" + "=" * 50)
        print(f" MENU USER - Selamat Datang, {nama_lengkap}")
        print("=" * 50)
        print("1. Tampilkan Seluruh Data Bayi")
        print("2. Cari Data Bayi")
        print("3. Lihat Statistik Ringkas")
        print("4. Keluar Akun")
        print("=" * 50)

        pilihan_menu = input("Pilih menu (1-4): ").strip()

        if pilihan_menu == "1":
            tampilkan_seluruh_data()
        elif pilihan_menu == "2":
            cari_data_bayi()
        elif pilihan_menu == "3":
            statistik_ringkas()
        elif pilihan_menu == "4":
            print(f"\nUser '{nama_lengkap}' berhasil keluar dari akun.")
            break
        else:
            print("Kesalahan: Pilihan menu tidak valid! Harap masukkan angka 1 sampai 4.")


def program_utama():
    "Fungsi utama penggerak seluruh alur sistem"
    while True:
        nama_pengguna, peran, nama_lengkap = sistem_masuk_akun()

        if nama_pengguna:
            print(
                f"\n[MASUK AKUN BERHASIL] Anda masuk sebagai {peran.upper()} ({nama_lengkap})"
            )
            if peran == "admin":
                menu_Admin(nama_lengkap)
            elif peran == "user":
                menu_User(nama_lengkap)
        else:
            print("\n[MASUK AKUN GAGAL] Nama Pengguna atau Kata Sandi salah!")

        while True:
            pilihan_mengulang = (
                input("\nApakah Anda ingin mencoba masuk akun kembali? (ya/tidak): ")
                .strip()
                .lower()
            )
            if pilihan_mengulang in ["ya", "tidak"]:
                break
            print("Kesalahan Input: Harap jawab dengan kata 'ya' atau 'tidak'. ")

        if pilihan_mengulang == "tidak":
            print("\nTerima kasih telah menggunakan aplikasi ini. Sampai jumpa!")
            break

if __name__ == "__main__":
    program_utama()