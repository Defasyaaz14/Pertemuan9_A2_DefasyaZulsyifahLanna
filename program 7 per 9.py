# Pendeklarasian array
buku = []

# Fungsi Show Data
def show_data():
    if len(buku) <= 0:
        print("Belum Ada Data")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s" % (indeks, buku[indeks]))

# Fungsi Insert Data
def insert_data():
    buku_baru = input("Judul Buku: ")
    buku.append(buku_baru)

# Fungsi Edit Data
def edit_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if indeks >= len(buku):
        print("ID Salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru

# Fungsi Delete Data
def delete_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if indeks >= len(buku):
        print("ID salah")
    else:
        buku.pop(indeks)

# Fungsi Show Menu
def show_menu():
    print("\n======Menu=====")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    menu = int(input("Pilih Menu : "))
    print("\n")
    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print("Input yang Anda masukkan salah")

if __name__ == "__main__":
    while True:
        show_menu()

