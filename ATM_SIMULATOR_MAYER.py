def periksa(tanya):
    while True:
        try:
            nanya = int(input(tanya))
            return nanya
        except ValueError:
            print("\nERROR!, Input salah ❌\n")


def tampil():
    print("\n1. Isi Saldo")
    print("2. Cek Saldo")
    print("3. Tarik Saldo")
    print("4. Keluar Transaksi")


def isi(saldo):
    while True:
        ngisi = periksa("\nIsi Berapa 💳: Rp")
        if ngisi == 0:
            print("Tidak dapat mengisi saldo dengan nominal Rp0! 😒")
            return ngisi
        print("Berhasil diisi! 🥳🥳\n")
        saldo += ngisi
        return saldo


def cek():
    while True:
        print(f"Saldo anda 💰: 👉 Rp{saldo} 👈\n")
        break


def tarik(saldo):
    while True:
        narik = periksa("Tarik Berapa 💵: Rp")
        if saldo < narik:
            print(f"Saldo Tidak cukup untuk ditarik sebesar: Rp{narik}! 😥")
            return saldo
        print(f"Berhasil Ditarik! 😁👍\n")
        saldo -= narik
        return saldo


saldo = 0

print("\n===================🏦 SELAMAT DATANG DI ATM BANK MAYERAS 🏦================\n")

while True:
    tampil()
    opsi = periksa("\nPilih 1,2,3,4 👉: ")

    if opsi > 4:
        print("\nPilih hanya sampai nomor 4❗\n")
    elif opsi < 1:
        print("\nPilih hanya dari nomor 1❗\n")

    elif opsi == 1:
        saldo = isi(saldo)

    elif opsi == 2:
        cek()

    elif opsi == 3:
        if saldo <= 0:
            print("Tidak Dapat Menarik!, saldo anda kosong! 😰\n")
            continue
        saldo = tarik(saldo)

    elif opsi == 4:
        print("\nTerimakasih telah menggunakan aplikasi ATM_SIMULATOR_MAYER... 🙏😊\n")
        exit()

# © MayerAS 29 November 2023
