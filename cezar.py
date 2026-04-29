import sys
def cezar(napis, klucz):
    """
    Szyfruje tekst za pomocą szyfru Cezara.

    Args:
        napis: tekst do zaszyfrowania
        klucz: liczba przesunięcia

    Returns:
        Zaszyfrowany tekst

    Raises:
        TypeError: jeśli zły format danych
    """
    # ... tutaj dalej Twój kod funkcji ...

# 1. Funkcja szyfrująca (Logika)
def encrypt_caesar(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result


# 2. Funkcja deszyfrująca (Wymagana dodatkowa funkcjonalność)
def decrypt_caesar(text, shift):
    return encrypt_caesar(text, -shift)


# 3. Funkcja odwracająca (Druga dodatkowa funkcjonalność)
def reverse_text(text):
    return text[::-1]


# 4. Główna część programu
def main():
    print("--- SZYFR CEZARA (GAŁĄŹ: CEZAR-KOD) ---")
    print("1. Szyfruj")
    print("2. Deszyfruj")
    print("3. Odwróć tekst")

    choice = input("Wybierz opcję (1/2/3): ")

    if choice in ['1', '2']:
        text = input("Podaj tekst: ")
        try:
            shift = int(input("Podaj przesunięcie: "))
            if choice == '1':
                print("Wynik:", encrypt_caesar(text, shift))
            else:
                print("Wynik:", decrypt_caesar(text, shift))
        except ValueError:
            print("Błąd: Przesunięcie musi być liczbą!")

    elif choice == '3':
        text = input("Podaj tekst do odwrócenia: ")
        print("Wynik:", reverse_text(text))
    else:
        print("Nieprawidłowy wybór.")


if __name__ == "__main__":
    main()
