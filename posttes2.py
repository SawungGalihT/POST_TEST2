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
