import time
import random


def cezar(napis, klucz):

    if not isinstance(napis, str) or not isinstance(klucz, int):
        raise TypeError("zły typ danych")

    wynik = ""
    for litera in napis:
        if litera.isupper():
            wynik += chr((ord(litera) + klucz - 65) % 26 + 65)
        elif litera.islower():
            wynik += chr((ord(litera) + klucz - 97) % 26 + 97)
        else:
            wynik += litera
    return wynik



def decrypt_caesar(text, shift):
    return cezar(text, -shift)


def reverse_text(text):
    return text[::-1]


def main():
    print("--- SZYFR CEZARA (GAŁĄŹ: POPRAWA_CEZARA) ---")
    print("1. Szyfruj (z pomiarem czasu i losowym kluczem)")
    print("2. Deszyfruj")
    print("3. Odwróć tekst")

    choice = input("Wybierz opcję (1/2/3): ")

    if choice == '1':
        text = input("Podaj tekst do zaszyfrowania: ")
        klucz_losowy = random.randint(1, 25)  # Wymagany generator klucza

        start_time = time.time()  # Wymagany pomiar czasu
        zaszyfrowany = cezar(text, klucz_losowy)
        end_time = time.time()

        print(f"\nWynik: {zaszyfrowany}")
        print(f"Użyty losowy klucz: {klucz_losowy}")
        print(f"Czas szyfrowania: {end_time - start_time:.6f} sekund")

    elif choice == '2':
        text = input("Podaj tekst: ")
        try:
            shift = int(input("Podaj klucz do deszyfracji: "))
            print("Wynik:", decrypt_caesar(text, shift))
        except ValueError:
            print("Błąd: Klucz musi być liczbą!")

    elif choice == '3':
        text = input("Podaj tekst do odwrócenia: ")
        print("Wynik:", reverse_text(text))
    else:
        print("Nieprawidłowy wybór.")


if __name__ == "__main__":
    main()