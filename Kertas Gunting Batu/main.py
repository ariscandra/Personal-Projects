import random

print("\n" + "="*40)
print("|" + " "*14 + "Kertas, Gunting, Batu" + " "*14 + "|")
print("="*40)

def tampilkan_menu():
    """Menampilkan menu pilihan untuk game."""
    print("\nPilih pilihan Anda:")
    print("1. Batu")
    print("2. Kertas")
    print("3. Gunting")
    print("4. Keluar")

def hasil_pertandingan(pilihan_user, pilihan_computer):
    """Menentukan hasil pertandingan antara pemain dan komputer."""
    if pilihan_user == pilihan_computer:
        return "Seri!"
    elif (pilihan_user == "Batu" and pilihan_computer == "Gunting") or \
         (pilihan_user == "Kertas" and pilihan_computer == "Batu") or \
         (pilihan_user == "Gunting" and pilihan_computer == "Kertas"):
        return "Anda menang!"
    else:
        return "Anda kalah!"

def main():
    """Fungsi utama untuk menjalankan game."""
    pilihan = ["Batu", "Kertas", "Gunting"]

    print("Selamat datang di game Kertas Gunting Batu!")
    
    while True:
        tampilkan_menu()
        try:
            pilihan_user = int(input("Masukkan pilihan Anda (1-4): "))
            
            if pilihan_user == 4:
                print("Terima kasih telah bermain!")
                break

            if pilihan_user not in [1, 2, 3]:
                print("Pilihan tidak valid! Silakan pilih 1, 2, atau 3.")
                continue

            # Pilihan pemain
            pilihan_user = pilihan[pilihan_user - 1]

            # Pilihan komputer (acak)
            pilihan_computer = random.choice(pilihan)

            print(f"\nAnda memilih: {pilihan_user}")
            print(f"Komputer memilih: {pilihan_computer}")

            # Menentukan hasil pertandingan
            print(hasil_pertandingan(pilihan_user, pilihan_computer))

        except ValueError:
            print("Input tidak valid! Silakan masukkan angka yang benar.")
            
# Panggil fungsi utama untuk memulai game
main()
