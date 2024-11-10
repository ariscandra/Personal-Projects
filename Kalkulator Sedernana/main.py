def tampilkan_menu():
    """Menampilkan menu kalkulator."""
    print("\n+========================================+")  
    print("| Selamat Datang di Kalkulator Sederhana |")  
    print("+========================================+")  
    print("Pilih operasi yang ingin dilakukan:")
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (*)")
    print("4. Bagi (/)")

def hitung(angka1, angka2, operasi):
    """Melakukan operasi aritmatika berdasarkan input pengguna."""
    if operasi == '+':
        return angka1 + angka2
    elif operasi == '-':
        return angka1 - angka2
    elif operasi == '*':
        return angka1 * angka2
    elif operasi == '/':
        if angka2 == 0:
            print("Error! Tidak dapat membagi dengan angka 0.")
            return None
        return angka1 / angka2
    else:
        print("Error! Operasi tidak valid.")
        return None

def kalkulator():
    """Fungsi utama untuk menjalankan kalkulator."""
    print("Kalkulator Sederhana")
    while True:
        tampilkan_menu()
        
        pilihan = input("Masukkan pilihan (1-4) atau 0 untuk keluar: ")
        
        if pilihan == '0':
            print("Terima kasih telah menggunakan kalkulator!")
            break
        
        if pilihan not in ['1', '2', '3', '4']:
            print("Error! Pilihan tidak valid. Silakan coba lagi.")
            continue
        
        try:
            bil1 = float(input("Masukkan bilangan pertama: "))
            bil2 = float(input("Masukkan bilangan kedua: "))
            
            if pilihan == '1':
                print("Diketahui: ", bil1, "+", bil2)
                hasil = hitung(bil1, bil2, '+')
            elif pilihan == '2':
                print("Diketahui: ", bil1, "-", bil2)
                hasil = hitung(bil1, bil2, '-')
            elif pilihan == '3':
                print("Diketahui: ", bil1, "x", bil2)
                hasil = hitung(bil1, bil2, '*')
            elif pilihan == '4':
                print("Diketahui: ", bil1, "/", bil2)
                hasil = hitung(bil1, bil2, '/')
            
            if hasil is not None:
                print(f"Hasil: {hasil}")
        except ValueError:
            print("Error! Input tidak valid. Silakan masukkan angka yang benar.")

# Panggil fungsi kalkulator untuk memulai
kalkulator()