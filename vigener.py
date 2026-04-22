def vigenere_cipher(tekst, klucz):
    if klucz is None or klucz == "":
        raise ValueError("Błędny klucz")
    zaszyfrowany_tekst = ""
    key_index = 0

    # Upewniamy się, że klucz i tekst są wielkimi literami dla uproszczenia
    tekst = tekst.upper()
    klucz = klucz.upper()

    for litera in tekst:
        if litera.isalpha():  # Szyfrujemy tylko litery
            # 1. Uzyskaj wartość liczbową litery tekstu (zakres 0-25)
            tekst_val = ord(litera) - ord('A')

            # 2. Uzyskaj wartość liczbową litery klucza (używając modulo dla zawijania klucza)
            klucz_litera = klucz[key_index % len(klucz)]
            klucz_val = ord(klucz_litera) - ord('A')

            # 3. Oblicz zaszyfrowaną literę (dodaj przesunięcie i zastosuj modulo 26)
            zaszyfrowana_val = (tekst_val + klucz_val) % 26

            # 4. Zamień wynik z powrotem na znak
            zaszyfrowany_tekst += chr(zaszyfrowana_val + ord('A'))

            # 5. Zwiększ indeks klucza tylko po zaszyfrowaniu litery
            key_index += 1
        else:
            # Jeśli znak nie jest literą (np. spacja), dodaj go bez zmian
            zaszyfrowany_tekst += litera

    return zaszyfrowany_tekst


def vigenere_decrypt(tekst, klucz):
    tekst = tekst.upper()
    klucz = klucz.upper()
    wynik = ""
    key_index = 0

    for litera in tekst:
        if litera.isalpha():
            t_val = ord(litera) - ord('A')
            k_val = ord(klucz[key_index % len(klucz)]) - ord('A')

            # Kluczowa zmiana: (t - k) zamiast (t + k)
            oryginalna_val = (t_val - k_val) % 26
            wynik += chr(oryginalna_val + ord('A'))
            key_index += 1
        else:
            wynik += litera
    return wynik

# Przykład użycia:
tekst_do_szyfrowania = "PROGRAMOWANIE"
moj_klucz = "KOD"
wynik = vigenere_cipher(tekst_do_szyfrowania, moj_klucz)

print(f"Tekst: {tekst_do_szyfrowania}")
print(f"Klucz: {moj_klucz}")
print(f"Wynik: {wynik}")