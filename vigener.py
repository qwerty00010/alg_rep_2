
def vigenere_cipher(tekst, klucz, mode='encrypt'):
    """
    Główna funkcja szyfrująca/deszyfrująca.
    mode='encrypt' -> szyfruje
    mode='decrypt' -> deszyfruje
    """
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


def reverse_text(text):
    """Odwraca tekst - dodatkowa operacja na danych"""
    return text[::-1]


def main():
    print("--- ZMODYFIKOWANY SZYFR VIGENÈRE'A ---")

    # Dane wejściowe
    tekst_do_szyfrowania = "PROGRAMOWANIE"
    moj_klucz = "KOD"

    # 1. Wywołanie szyfrowania
    wynik = vigenere_cipher(tekst_do_szyfrowania, moj_klucz, mode='encrypt')
    print(f"Tekst: {tekst_do_szyfrowania}")
    print(f"Klucz: {moj_klucz}")
    print(f"Wynik szyfrowania: {wynik}")

    # 2. Wywołanie deszyfrowania (Twoja poprawka funkcjonalności)
    oryginal = vigenere_cipher(wynik, moj_klucz, mode='decrypt')
    print(f"Wynik deszyfrowania: {oryginal}")
    
    odwrocony = reverse_text(wynik)
    print(f"Wynik odwrócony: {odwrocone}")


if __name__ == "__main__":
    main()