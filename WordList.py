import os
import random

def generate_wordlist(chars, min_len, max_len, word_count, filename):
    words = set()  # Təkrarlanan sözləri önləmək üçün set() istifadə edilir

    while len(words) < word_count:
        length = random.randint(min_len, max_len)  # Rastgele uzunluq seç
        word = ''.join(random.choices(chars, k=length))  # Şifrə yarat
        words.add(word)

    with open(filename, "w") as f:
        for word in words:
            f.write(word + "\n")

    print(f"\n✅ Wordlist '{filename}' dosyasına kaydedildi!")
    print(f"📌 Toplam {word_count} kelime oluşturuldu.")

def main():
    os.system("clear")  # 🔹 Termux ekranını təmizlə

    print("************************************")
    print("      🚀 HACKLAB WORDLIST 🚀       ")
    print("************************************\n")

    letters = input("Hərfləri daxil edin (örn: abcdefABCDEF): ")
    numbers = input("Rəqəmləri daxil edin (örn: 0123456789): ")
    symbols = input("Simvolları daxil edin (örn: !@#$%^&*): ")

    chars = letters + numbers + symbols  # Bütün daxil edilənləri birləşdiririk

    min_len = int(input("Minimum uzunluğu daxil edin: "))
    max_len = int(input("Maksimum uzunluğu daxil edin: "))
    
    # Kelime sayısını sor ve sınırları belirle (1000 - 200000 arası)
    while True:
        word_count = int(input("Neçə şifrə yaradılacaq? (1000 - 200000): "))
        if 1000 <= word_count <= 200000:
            break
        print("❌ HATA: Şifrə sayı 1000 ilə 200000 arasında olmalıdır!")

    filename = input("Wordlist faylının adını daxil edin (örn: wordlist.txt): ")

    generate_wordlist(chars, min_len, max_len, word_count, filename)

if __name__ == "__main__":
    main()