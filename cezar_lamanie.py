# brute_force_cezar.py

def decrypt_caesar(text, shift):
    """Pomocnicza funkcja deszyfrująca"""
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result


def break_caesar(ciphertext):
    """Główna funkcja łamiąca szyfr metodą Brute Force"""
    print(f"\n--- Łamanie szyfru dla tekstu: '{ciphertext}' ---\n")

    # Wykorzystujemy fakt, że istnieje tylko 26 możliwych przesunięć
    for shift in range(26):
        decrypted = decrypt_caesar(ciphertext, shift)

        # Opcjonalnie: Prosta analiza częstotliwości (szukanie polskich słów/liter)
        # Dla uproszczenia wyświetlamy wszystkie, by użytkownik sam wskazał poprawne.
        print(f"Klucz {shift:2}: {decrypted}")


def main():
    print("--- PROGRAM DO ŁAMANIA SZYFRU CEZARA ---")
    encrypted_text = input("Podaj zaszyfrowany tekst do złamania: ")

    if encrypted_text:
        break_caesar(encrypted_text)
    else:
        print("Nie podano tekstu.")


if __name__ == "__main__":
    main()