import secrets
import string
import time



def vigenere_cipher(tekst, klucz, mode='encrypt'):
    zaszyfrowany_tekst = ""
    key_index = 0
    tekst = tekst.upper()
    klucz = klucz.upper()

    for litera in tekst:
        if litera.isalpha():
            tekst_val = ord(litera) - ord('A')
            klucz_litera = klucz[key_index % len(klucz)]
            klucz_val = ord(klucz_litera) - ord('A')

            if mode == 'encrypt':
                wynik_val = (tekst_val + klucz_val) % 26
            else:  # mode == 'decrypt'
                wynik_val = (tekst_val - klucz_val + 26) % 26

            zaszyfrowany_tekst += chr(wynik_val + ord('A'))
            key_index += 1
        else:
            zaszyfrowany_tekst += litera
    return zaszyfrowany_tekst


def generate_key(length):
    letters = string.ascii_uppercase
    return ''.join(secrets.choice(letters) for _ in range(length))


def reverse_text(text):
    return text[::-1]



def main():
    print("--- ZMODYFIKOWANY SZYFR VIGENÈRE'A ---")

    tekst_do_szyfrowania = "PROGRAMOWANIE"


    moj_klucz = generate_key(5)
    print(f"Wygenerowany losowy klucz: {moj_klucz}")


    start_time = time.time()

    wynik = vigenere_cipher(tekst_do_szyfrowania, moj_klucz, mode='encrypt')

    end_time = time.time()
    czas_trwania = end_time - start_time

    print(f"Tekst: {tekst_do_szyfrowania}")
    print(f"Wynik szyfrowania: {wynik}")
    print(f"Czas szyfrowania: {czas_trwania:.6f} sekund")


    oryginal = vigenere_cipher(wynik, moj_klucz, mode='decrypt')
    print(f"Wynik deszyfrowania: {oryginal}")


    odwrocony_wynik = reverse_text(wynik)
    print(f"Wynik odwrócony: {odwrocony_wynik}")


if __name__ == "__main__":
    main()