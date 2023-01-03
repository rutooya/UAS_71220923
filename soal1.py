print("="*42)
print("*"*13,"Justice League", "*"*13)
print("="*42)
list = ("brucewyne", "victorstone", "ciscoramon")
username = input("Masukkan username anda: ")
print("="*5,"WELCOME", username,"="*5)
def pilihan_1():
    anggota_baru = input("Nama Anggota baru: ")
    print("data","'",anggota_baru,"'", "berhasil ditambahkan")
    list = ("brucewyne", "victorstone", "ciscoramon", anggota_baru)
    pilihan()
def pilihan_2():
    anggota_hapus = input("Anggota yang akan dihapus: ")
    if anggota_hapus == (list):
        print("data","'", anggota_hapus,"'", "berhasil dihapus")
        list = ("brucewyne", "victorstone", "ciscoramon", anggota_hapus)
        pilihan()
    else:
        print("data","'", anggota_hapus,"'", "tidak ditemukan")
        pilihan()

def pilihan_3():
    print(list)
    pilihan()

def pilihan():
    print("1. Tambah Anggota Justice League")
    print("2. Hapus Anggota Justice League")
    print("3. Tampilkan Anggota Justice League")
    print("4. Exit")
    pilih = int(input("Masukan pilihan anda: "))
    if pilih == 1:
        pilihan_1()
    elif pilih == 2:
        pilihan_2()
    elif pilih == 3:
        pilihan_3()
    else:
        print("see u next time MR. ", username, ",GLHF")
def user_name(): 
    if username == "brucewyne":
        pilihan()
    elif username == "victorstone":
        pilihan()
    elif username == "ciscoramon":
        pilihan()
    else:
        print("Acces denied")
user_name()