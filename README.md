# POST_TEST2
# NAMA: SAWUNG-GALIH-TRIATMOJO
# KELAS: SISTEM-INFORMASI-B
# NIM: 2309116058
#
# TOKO-HASIL-PADI
import sys
from prettytable import PrettyTable

username_admin = "lek nyoto"
password_admin = "4444"

daftar_barang = [["beras",12000],["dedak",10000],["meniran",7500],["sekam",2500]]
keranjang = []
daftar_transaksi = [50000,154000,60000,100000]

def tampil_transaksi():
    table_transaksi = PrettyTable()
    table_transaksi.title = "Daftar Transaksi"
    table_transaksi.field_names = ["Id Transaksi", "Jumlah Belanjaan"]
    for i in range(len(daftar_transaksi)):
        table_transaksi.add_row([i+439521, "Rp. " + str(daftar_transaksi[i]),])
    print(table_transaksi)
    input("\nTekan ENTER untuk kembali. ")

def tampil_keranjang():
    daftar_keranjang = PrettyTable() 
    daftar_keranjang.title = "Keranjang"
    daftar_keranjang.field_names = ["Nomor","Nama Barang", "Harga Barang / kg"]
    total_harga = 0
    for i in range(len(keranjang)):
        daftar_keranjang.add_row([i+1, keranjang[i][0], "Rp. " + str(keranjang[i][1]),])
        total_harga += keranjang[i][1]
    print(daftar_keranjang)
    return total_harga

def checkout(parameter1):
    cekot = PrettyTable()
    cekot.title = "Pembayaran Berhasil"
    cekot.field_names = ["Nomor","Nama Barang", "Harga Barang / kg"]
    total_harga = 0
    for i in range(len(keranjang)):
        cekot.add_row([i+1, keranjang[i][0], "Rp. " + str(keranjang[i][1]),])
        total_harga += keranjang[i][1]
    cekot.add_row(["-------------","-------------","-------------"])
    cekot.add_row([" ","Uang","Rp. "+str(parameter1)])
    cekot.add_row(["-------------","-------------","-------------"])
    cekot.add_row([" ","Total","Rp. "+str(total_harga)])
    cekot.add_row(["-------------","-------------","-------------"])
    cekot.add_row([" ","Kembalian","Rp. "+str(parameter1-total_harga)])
    print(cekot)

def tampil_barang():
    table = PrettyTable()
    table.title = "Daftar Barang"
    table.field_names = ["Nomor","Nama Barang", "Harga Barang / kg"]
    for i in range(len(daftar_barang)):
        table.add_row([i+1, daftar_barang[i][0], "Rp. " + str(daftar_barang[i][1]),])
    print(table)
    
def menu_admin():
    while True:
        print("\n\nMenu Admin\n")
        print("1. Tambahkan Barang")
        print("2. Lihat Daftar Barang")
        print("3. Edit Barang")
        print("4. Hapus Barang")
        print("5. Lihat Data Transaksi")
        print("6. Kembali")
        pil =  str(input("Masukkan pilihan anda : "))
        print("")
        if (pil == "1") :
            tampil_barang()
            nama_barang = str(input("Masukkan nama barang : "))
            harga_barang = int(input("\nMasukkan harga barang : "))
            barang = [nama_barang, harga_barang]
            daftar_barang.append(barang)
            print("")
            tampil_barang()
            input("Barang Berhasil Ditambahkan. Tekan ENTER Untuk Kembali. ")

        elif (pil == "2") :
            tampil_barang()

        elif (pil == "3") :
            tampil_barang()
            print("")
            nomor_edit = int(input("Barang Nomor Berapa Yang Ingin Diubah : "))
            nama_barang = str(input("Masukkan nama barang : "))
            harga_barang = int(input("Masukkan harga barang : "))
            barang = [nama_barang, harga_barang]
            daftar_barang[nomor_edit-1] = barang
            print("")
            tampil_barang()
            input("Barang Berhasil Diubah. Tekan ENTER Untuk Kembali. ")

        elif (pil == "4") :
            tampil_barang()
            print("")
            nomor_hapus = int(input("Barang Nomor Berapa Yang Ingin Dihapus : "))
            daftar_barang.pop(nomor_hapus-1)
            tampil_barang()
            input("Barang Berhasil Dihapus. Tekan ENTER Untuk Kembali. ")

        elif (pil == "5") :
            tampil_transaksi()

        elif (pil == "6") :
            break

def menu_pelanggan():
    while True:
        tampil_barang()
        barang_pilihan = int(input("\nMasukkan barang pilihan anda : "))
        barang = daftar_barang[barang_pilihan-1]
        keranjang.append(barang)
        print("")
        total_harga_belanjaan = tampil_keranjang()
        nambah = str(input("\nIngin menambah belanjaan? [y/n] : "))
        print("")
        print("")
        if nambah == "y" or nambah == "Y" :
            continue
        elif nambah == "n" or nambah == "N" :
            break
    uang = int(input("Masukkan Jumlah Uang Anda : "))
    if uang-total_harga_belanjaan >=0 :
        checkout(uang)
        input("\nTerimakasih telah belanja di toko kami. ")
        daftar_transaksi.append(total_harga_belanjaan)
    else :
        input("Uang anda tidak cukup. Nabung aja dulu. ")

def login():
    username = str(input("Masukkan Username : "))
    password = str(input("Masukkan Password : "))
    if (username == username_admin and password == password_admin) :
        menu_admin()
    else :
        input("Anda Bukan Admin! Tekan ENTER Untuk Kembali. ")
    

while True:
    print("="*10, "SELAMAT DATANG","="*10, "\n   DI TOKO HASIL PADI LEK NYOTO\n\n")
    print("Menu")
    print("1. Login Admin")
    print("2. Lanjutkan Sebagai Pelanggan")
    print("3. Exit")
    pilihan = str(input("Masukkan Pilihan Anda : "))
    print("")

    if (pilihan == "1") : 
        login()
    elif (pilihan == "2") : 
        menu_pelanggan()
    elif (pilihan == "3") : 
        sys.exit()

![TOKO PADI drawio](https://github.com/SawungGalihT/POST_TEST2/assets/144757389/959c860c-f6d3-4721-aa25-117fe1e50e25)
Gambar FlowChart

![Screenshot 2023-10-08 2240523](https://github.com/SawungGalihT/POST_TEST2/assets/144757389/70d2c2d6-68f0-49c0-b896-090f94834c86)
saat program di run akan muncul menu seperti berikut.


![Screenshot 2023-10-08 224052](https://github.com/SawungGalihT/POST_TEST2/assets/144757389/e696237d-8110-45d2-887f-96d6abbdef56)

ketika memilih pilihan 1. (Login Admin) maka akan keluar ussername dan password Admin untuk memverivikasi bahwa anda adalah admin.
ketika anda memasukkan ussername dan password dengan benar maka anda akan masuk ke menu admin, yang di menu tersebut terdapat 6 pilihan yaitu:
1. Tambahkan Barang (menambahkan barang baru). 2. Lihat Daftar Barang (melihat daftar barang yang sudah ada / yang baru). 3. Edit Barang (mengedit / memperbarui / mengubah barang yang sudah ada). 4. Hapus Barang (menhapus barang yang sudah ada). 5. Lihat Data Transaksi (melihat data transaksi yang sudah dilakukan oleh peanggan). 6. Kembali (Kembali Ke Menu Awal).

![Screenshot 2023-10-08 224352](https://github.com/SawungGalihT/POST_TEST2/assets/144757389/1a6b7cfb-e12e-4ea4-a94c-e7412298d3fd)

Ketika anda memasukkan pilihan 1. Tambahkan Barang. Maka anda akan diperlihatkan daftar barang yang sudah ada. Kemudian anda dapat memasukkan nama dan harga dari barang baru yang ingin anda masukkan (Disini sebagai contoh untuk nama barangnya adalah "beras merah" dan harga barangnya "20000"). Kemudian setelah anda memasukkan nama dan harga dari barang baru tersebut, anda akan diperlihatkan daftar barang yang baru yang berisi barang dan harga yang sudah anda masukkan. 

![Screenshot 2023-10-08 224425](https://github.com/SawungGalihT/POST_TEST2/assets/144757389/656376eb-3394-43dc-a698-a1fb34b01bf9)

Ketika anda memasukkan pilihan 2. Lihat Daftar Barang. Maka anda akan diperlihatkan daftar barang anda baik yang belum diubah maupun yang sudah diubah.

![Screenshot 2023-10-08 224438](https://github.com/SawungGalihT/POST_TEST2/assets/144757389/06fca96c-5e2f-4130-9c54-877b1be975db)

Ketika anda memasukkan pilihan 3. Edit Barang. Maka anda akan diperlihatkan daftar barang, kemudian anda dapat mengedit / memperbarui / mengubah barang yang sudah ada, dengan memilih barang nomor berapa yang ingin diedit, memasukkan nama dan harga barang yang baru (Disini sebagai contoh untuk barang yang ingin dirubah adalah barang nomor 2, dengan memasukkan nama barang "dedak", dan harganya "8000"). Kemudian setelah anda mengganti barang (memasukkan nama dan harga barang yang baru), anda akan diperlihatkan daftar barang yang sudah diganti / diedit.

![Screenshot 2023-10-08 224453](https://github.com/SawungGalihT/POST_TEST2/assets/144757389/80af6924-7e68-4fb6-bbcd-df8b7487171a)

Ketika anda memasukkan pilihan 4. Hapus Barang. Maka anda akan diperlihatkan daftar barang, kemudian anda dapat menghapus barang yang sudah ada, dengan memilih barang nomor berapa yang ingin dihapus (Disini sebagai contoh untuk barang yang ingin dihapus adalah barang nomor 4, dengan memasukkan nomor 4 pada pilihan). Kemudian setelah anda menghapus barang, anda akan diperlihatkan daftar barang yang baru(ada barang yang dihapus)

![Screenshot 2023-10-08 224509](https://github.com/SawungGalihT/POST_TEST2/assets/144757389/19a77202-905e-47fa-8b2e-58997dd7f3da)

Ketika anda memasukkan pilihan 5. Lihat Data Transaksi. Maka anda akan diperlihatkan data transaksi yang sudah dilakukan oleh pelanggan.

![Screenshot 2023-10-08 224525](https://github.com/SawungGalihT/POST_TEST2/assets/144757389/58faf35b-912d-4d4a-af79-7146ba41a979)

Ketika anda memasukkan pilihan 6. Kembali. Maka anda akan kembali ke menu awal.

![Screenshot 2023-10-08 224542](https://github.com/SawungGalihT/POST_TEST2/assets/144757389/d5466da5-ab99-4019-a592-f75069062265)

Ketika anda kembali ke menu awal, dan memasukkan pilihan 2. Lanjutkan Sebagai Pelanggan. Dan anda akan diminta untuk memasukkan barang pilihan anda(Yang ingin anda beli). Setelah anda memasukkan pilihan barang yang anda pilih maka barang tersebut akan masuk kek keranjang(Disini sebagai contoh barang yang dimasukkan adalah barang nomor 1), dan kemudian anda akan ditanya lagi, apakah anda akan menambah barang lagi. Disini terdapat dua pilihan yaitu (y untuk melanjutkan memilih barang dan n untuk berhenti memilih barang).(disini sebagai contoh memilih y)

![Screenshot 2023-10-08 224558](https://github.com/SawungGalihT/POST_TEST2/assets/144757389/72e3a3eb-1f84-42db-8c57-8a1e37c5d550)

Ketika anda memilih y maka anda akan melanjutkan memilih barang, dan dapat diketahui sebagai contoh disini memasukkan barang nomor 4, dan barang yang telah dipilih/dimasukkan itu akan masuk ke keranjang, jadi untuk sekarang terdapat 2 barang di keranjang itu. Dan kembali terdapat pilihan y/n, disini memasukkan pilihan y.

![Screenshot 2023-10-08 224626](https://github.com/SawungGalihT/POST_TEST2/assets/144757389/d35aa957-bf10-4c34-9e66-d2c911809236)

Ketika anda memilih pilihan y maka anda akan melanjutkan memilih barang, disini memsukkan barang nomor 2,, dan barang yang dipilih itu akan masuk ke keranjang, jadi terdapat 3 barang di keranjang untuk sekarang. Disini terdapat pilihan y/n, dan disini memasukkan pilihan n (yang dimana pilihan n digunakan untuk berhenti memilih barang). Setelah anda memasukkan pilihan n, anda akan diarahkan untuk memasukkan jumlah / nominal uang yang akan anda masukkan/ bayar (disini memasukkan jumlah/ nominal uang sebanyak 50000). setelah memasukan jumlah/ nominal uang yang cukup, anda akan diberikan semacam struk pembelanjaan yang berisi: jumlah barang, harga dari masing masing barang, total harga barang yang dibeli/dipilih, dan jika jumlah/ nominal uang yang anda masukkan melebihi total harga barang yang dibeli/dipilih, akan ditampilkan jumlah kembaliannya. Juga ditampilkan ucapan "terimakasih telah berbelanja di toko kami".

![Screenshot 2023-10-08 224646](https://github.com/SawungGalihT/POST_TEST2/assets/144757389/ebaf95d3-f502-43c8-a479-6a031452b900)

Jika anda menekan enter maka anda akan kembali ke menu utama. Jika anda masuk sebagai admin dan memilih pilihan 5. Lihat Data Transaksi. Maka anda dapat melihat data dari transaksi dari pelanggan baru.

![Screenshot 2023-10-08 224704](https://github.com/SawungGalihT/POST_TEST2/assets/144757389/c5366d6e-ad8a-4510-a070-b7f2752b529e)

Ketika anda Membayar barang yang dibeli/dipilih,  dan jumlah/ nominal uang yang anda masukkan kurang dari total harga barang yang anda beli/ pilih, maka program akan menampilkan ucapan "Uang anda tidak cukup.Nabung aja dulu.

![Screenshot 2023-10-08 224716](https://github.com/SawungGalihT/POST_TEST2/assets/144757389/fe300bc2-3aa9-43df-977e-f6d3c4c0188c)

Ketika anda berada di menu utama, dan anda memasukkan pilihan 1. Login Sebagai Admin. dan ketika anda salah memasukkan username atau password, maka akan ditampilkan "Anda bukan Admin !! Silahkan tekan ENTER untuk kembali". Ketika anda menekan ENTER, anda akan kembali ke menu utama. Dan ketika anda memasukkan pilihan 3.  Exit. maka anda akan keluar dari program.
