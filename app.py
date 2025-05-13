import tkinter as tk
from tkinter import messagebox
import random

# Fungsi untuk mengecek jawaban
def check_answer(first_part, second_part, correct_word, selected_word, window):
    # Gabungkan kedua suku kata dan cek apakah hasilnya sesuai dengan kata yang benar
    if selected_word == correct_word:
        messagebox.showinfo("Selamat!", "Jawaban Anda Benar!")
        window.after(1000, create_game)  # Menunggu 1 detik dan buat game baru
    else:
        messagebox.showinfo("Coba Lagi", "Jawaban Anda Salah. Silakan coba lagi.")

# Fungsi untuk mengatur game
def create_game():
    # Membuat jendela utama baru
    window = tk.Tk()
    window.title("Gabungkan Kata")
    
    # Pasangan suku kata dan kata yang benar, termasuk hewan, benda, dan organ tubuh
    word_pairs = [
        # Kata dasar umum
        ("ba", "ca", "baca"),
        ("da", "ri", "dari"),
        ("ma", "kan", "makan"),
        ("sa", "la", "salam"),
        ("bu", "ka", "buku"),
        ("pe", "la", "pela"),
        ("ra", "ti", "rata"),
        ("ka", "ta", "kata"),
        ("pa", "la", "pala"),
        ("ba", "ti", "bati"),
        ("ma", "ta", "mata"),
        ("sa", "ti", "sati"),
        ("bu", "di", "budi"),
        ("se", "ra", "sera"),
        ("di", "ri", "diri"),
        ("ko", "ta", "kota"),
        ("bi", "sa", "bisa"),
        ("ti", "ga", "tiga"),
        ("ka", "wa", "kawa"),
        ("se", "ka", "seka"),
        ("ma", "si", "masi"),
        ("pa", "ti", "pati"),
        ("lo", "ka", "loka"),
        ("la", "ki", "laki"),
        ("pa", "ka", "paka"),

        # Hewan
        ("a", "yam", "ayam"),
        ("kam", "bing", "kambing"),
        ("ku", "cing", "kucing"), 
          ("be","bek","bebek"),
          ("ga","jah","gajah"),
        
        # Benda
        ("me", "ja", "meja"),
        ("ka", "ca", "kaca"),
        ("kur","si","kursi"),
        ("pen","sil","pensil"),
        ("sa","pu","sapu"),

        
        # Organ tubuh
        ("ka", "ki", "kaki"),
        ("ta", "ngan", "tangan"),
        ("pa", "ru", "paru"),
        ("hi", "dung", "hidung"),
        ("ma","ta","mata"),
        ("ram","but","rambut"),
        ("o","tak","otak"),
        ("ha","ti","hati"),
    ]
    
    # Memilih pasangan secara acak
    first_part, second_part, correct_word = random.choice(word_pairs)

    # Menampilkan instruksi
    instruction_label = tk.Label(window, text="Gabungkan suku kata berikut:", font=("Helvetica", 18), width=30, height=2)
    instruction_label.pack(pady=30)

    # Menampilkan suku kata yang harus digabungkan
    suku1_label = tk.Label(window, text=f"Suku kata 1: {first_part}", font=("Helvetica", 16), width=30, height=2)
    suku1_label.pack(pady=10)
    
    suku2_label = tk.Label(window, text=f"Suku kata 2: {second_part}", font=("Helvetica", 16), width=30, height=2)
    suku2_label.pack(pady=10)

    # Membuat beberapa pilihan kata (termasuk kata yang benar dan beberapa yang salah)
    incorrect_words = [word[2] for word in word_pairs if word[2] != correct_word]
    word_options = [correct_word] + random.sample(incorrect_words, 3)  # Menambahkan 3 kata salah yang diacak

    
    random.shuffle(word_options)  # Mengacak pilihan kata

    # Membuat tombol untuk pilihan kata dengan ukuran besar
    for word in word_options:
        button = tk.Button(window, text=word, font=("Helvetica", 18), width=15, height=2, command=lambda w=word: check_answer(first_part, second_part, correct_word, w, window))
        button.pack(pady=15)

    # Menjalankan aplikasi
    window.mainloop()

# Memulai game
create_game()
