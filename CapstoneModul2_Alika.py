# Data pasien: ID, nama, tanggal lahir, gender, pasien dokter siapa, dan jenis konsultasi
data_pasien = [
    ["01-1", "Rachim", "Pria", "pasien lama", "dr. Gito", "Online"],
    ["02-2", "Tiara", "Wanita", "pasien baru", "dr. Bee", "Walk in"],
    ["01-3", "Eko", "Pria", "pasien lama", "dr. Rodi", "Walk in"]
]

# Fungsi untuk menentukan kode gender
def kode_gender(gender):
    return '01' if gender.lower() == 'pria' else '02'


# Fungsi untuk menentukan nomor urut pasien
def nomor_urut():
    return f"{len(data_pasien) + 1}"


# Fungsi gabungan untuk membuat ID
def generate_id(gender):
    return f"{kode_gender(gender)}-{nomor_urut()}"


# Menampilkan list pasien online
def ambil_pasien_online(data):
    pasien_online = []
    for pasien in data:
        if pasien[5].lower() == "online":
            pasien_online.append(pasien)
    return pasien_online
data_pasien_online = ambil_pasien_online(data_pasien)


# Menampilkan list pasien walk in
def ambil_pasien_walkin(data):
    pasien_walkin = []
    for pasien in data:
        if pasien[5].lower() == "walk in":
            pasien_walkin.append(pasien)
    return pasien_walkin
data_pasien_walkin = ambil_pasien_walkin(data_pasien)


# Fungsi input validasi 
def input_tidak_kosong(prompt):
    while True:
        value = input(prompt).strip()
        if value and all(c.isalpha() or c.isspace() for c in value):
            return value.title()
        print("Input tidak boleh kosong dan harus huruf!")

def input_gender(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ["pria", "wanita"]:
            return value.capitalize()
        print("Jenis kelamin hanya boleh 'Pria' atau 'Wanita'.")

def input_riwayat(prompt):
    while True:
        value = input(prompt).strip().lower()
        if "lama" in value:
            return "pasien lama"
        elif "baru" in value:
            return "pasien baru"
        else:
            print("apakah pasien lama atau baru?")

def input_dokter(prompt):
    while True:
        value = input(prompt).strip().lower()
        words = value.split()
        if "bee" in words:
            return "dr. Bee"
        elif "gito" in words:
            return "dr. Gito"
        elif "rodi" in words:
            return "dr. Rodi"
        else:
            print("Dokter tersedia hanya: dr. Bee, dr. Gito, dan dr. Rodi.")

def input_konsul(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ["online", "walk in"]:
            return value.title()
        print("Jenis konsul yang tersedia hanya 'Online' atau 'Walk In'.")


# Fungsi untuk menampilkan daftar pasien
def tampilkan_data_pasien(mode="all"):
    if len(data_pasien) == 0:
            print("Tidak ada data Pasien")
            return
    if mode == "all":
        print("\nDaftar Semua Pasien:")
        for i, pasien in enumerate(data_pasien, start=1):
            print(f"{i}. {', '.join(pasien)}")
    elif mode == "online":
        print("\nDaftar Pasien Online:")
        for pasien in ambil_pasien_online(data_pasien):
            print(", ".join(pasien))
    elif mode == "walkin":
        print("\nDaftar Pasien Walk-in:")
        for pasien in ambil_pasien_walkin(data_pasien):
            print(", ".join(pasien))
  
def menu_satu():
    while True:
        print("\n\t\t*** Menampilkan Daftar Pasien ***")
        if not data_pasien:
            print("Tidak ada data Pasien")
            break
        tampilkan_data_pasien()
        print("\n1. Menampilkan Daftar Pasien Online")
        print("2. Menampilkan Daftar Pasien Walk-in")
        print("3. kembali ke Menu Utama")

        pilihan = input("Pilih menu (1-3): ")
        if pilihan == "1":
             hasil = ambil_pasien_online(data_pasien)
             if not hasil:
                 print("\ntidak ada pasien Online")
             else:
                 print("\nDaftar Pasien Online:")
                 for pasien in hasil:
                     print(pasien)

        elif pilihan == "2":
            hasil = ambil_pasien_walkin(data_pasien)
            if not hasil:
                 print("\ntidak ada pasien Walk In")
            else:
                print("\nDaftar Pasien Walk In:")
                for pasien in hasil:
                    print(pasien)

        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid.")


# Fungsi untuk menambah pasien
def menu_dua():
    while True:
        print("\n\t\t*** Menambah Pasien ***\n")
        print("1. Tambahkan Data Pasien")
        print("2. kembali ke Menu Utama")
        pilihan = input("Pilih menu (1/2): ")
        if pilihan == "1":
            def tambah_pasien():
                nama_pasien = input_tidak_kosong("Nama: ")
                gender = input_gender("Jenis kelamin (Pria/Wanita): ")
                riwayat = input_riwayat("Pasien lama/baru: ")
                nama_dokter = input_dokter("Berobat dengan dokter siapa: ")
                konsul_type = input_konsul("Jenis konsul (Online/Walk In): ")
                id_pasien = generate_id(gender)
                data_pasien.append([id_pasien, nama_pasien, gender, riwayat, nama_dokter, konsul_type])
                print(f"Pasien berhasil ditambahkan dengan ID: {id_pasien}")
                print(data_pasien[-1])
            tambah_pasien()
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid.")


# Fungsi untuk edit data pasien
def menu_tiga():
    while True:
        print("\n\t\t*** Mengedit Data Pasien ***\n")
        print("1. Edit Data Pasien")
        print("2. kembali ke Menu Utama")
        pilihan = input("Pilih menu (1/2): ")
        if pilihan == "1":
            def edit_pasien():
                if len(data_pasien) == 0:
                    print("\nTidak ada data Pasien")
                    return
                index_input = input("Masukkan nomor pasien yang ingin diubah: ").strip()
                if not index_input.isdigit():
                        print("Harus angka!")
                        return
                index=int(index_input)-1    
                if 0 <= index < len(data_pasien):
                    print("Masukkan data baru (biarkan kosong jika tidak diubah):\n")

        # Edit nama
                    nama_input = input(f"Nama [{data_pasien[index][1]}]: ").strip()
                    nama = data_pasien[index][1] if not nama_input else (nama_input.title() if nama_input.replace(" ", "").isalpha() else input_tidak_kosong("Nama: "))

        # Edit gender
                    gender_input = input(f"Jenis kelamin [{data_pasien[index][2]}]: ").strip()
                    gender = data_pasien[index][2] if not gender_input else input_gender("Jenis kelamin (Pria/Wanita): ")

        # Edit riwayat
                    riwayat_input = input(f"Riwayat [{data_pasien[index][3]}]: ").strip()
                    riwayat = data_pasien[index][3] if not riwayat_input else input_riwayat("Pasien lama/baru: ")

        # Edit dokter
                    dokter_input = input(f"Dokter [{data_pasien[index][4]}]: ").strip()
                    dokter = data_pasien[index][4] if not dokter_input else input_dokter("Berobat dengan dokter siapa: ")

        # Edit jenis konsul
                    konsul_input = input(f"Jenis Konsul [{data_pasien[index][5]}]: ").strip()
                    konsul = data_pasien[index][5] if not konsul_input else input_konsul("Jenis konsul (Online/Walk In): ")

        # Simpan perubahan
                    data_pasien[index] = [data_pasien[index][0], nama, gender, riwayat, dokter, konsul]
                    print("\nData pasien berhasil diperbarui: \n")
                    print(data_pasien[index])
                else: 
                    print("Pilihan tidak valid.")
                    return
            edit_pasien()
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid.")


# Fungsi untuk hapus data pasien
def menu_empat():
    while True:
        print("\n\t\t*** Menghapus Data Pasien ***\n")
        print("1. Hapus Data Pasien")
        print("2. kembali ke Menu Utama")
        pilihan = input("Pilih menu (1/2): ")
        if pilihan == "1":
           def hapus_pasien():
                if len(data_pasien) == 0:
                    print("Tidak ada data Pasien")
                    return
                
                index_input = input("Masukkan nomor pasien yang ingin dihapus: ").strip()
                if not index_input.isdigit():
                        print("Harus angka!")
                        return
                index=int(index_input)-1 
                if 0 <= index < len(data_pasien):
                    konfirmasi = input(f"Yakin ingin menghapus {data_pasien[index][0]}? (y/n): ").lower()
                    if konfirmasi == "y":
                                del data_pasien[index]
                                print("Pasien berhasil dihapus.")         
                    elif konfirmasi == "n":
                        print("\nTidak ada data pasien yang dihapus.")
                    else:
                        print("\nPilihan Konfirmasi tidak valid.")
                        return
                
                else:
                    print("Nomor pasien tidak valid.")
           hapus_pasien()

        elif pilihan == "2":
             break
        else:
            print("Pilihan tidak valid.")


# Fungsi utama (main menu)
def menu_utama():
    while True:
        print("\n\t\t=== Administrasi Pasien Klinik ===\n")
        print("1. Menampilkan Daftar Pasien")
        print("2. Menambah Pasien")
        print("3. Edit Data Pasien")
        print("4. Hapus Data Pasien")
        print("5. Exit Program")
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            menu_satu()
        elif pilihan == "2":
            menu_dua()
        elif pilihan == "3":
            menu_tiga()
        elif pilihan == "4":
            menu_empat()
        elif pilihan == "5":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

# Jalankan program

menu_utama()
