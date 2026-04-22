from vigener import vigenere_cipher, vigenere_decrypt
import pytest

def test_vinegre_basic():
    tekst = "PYTHON"
    klucz = "A"
    zaszyfrowany_tekst = vigenere_cipher(tekst, klucz)
    assert zaszyfrowany_tekst == "PYTHON"


def test_dl_klucza():
    tekst = "ABCDE"
    klucz = "AB"
    zaszyfrowany_tekst = vigenere_cipher(tekst, klucz)
    assert zaszyfrowany_tekst == "ACCEE"


def test_raise_error():
    tekst = "ABCDE"
    klucz = None

    # Test sprawdzający, czy funkcja poprawnie wyrzuca błąd
    with pytest.raises(ValueError, match="Błędny klucz"):
        vigenere_cipher(tekst, klucz)

#def test_twenty_five():
    # 'Z' to 25. litera alfabetu (indeks 25)
    # Przy poprawnym modulo 26: (25 + 0) % 26 = 25 -> 'Z'
    # Przy błędnym modulo 25: (25 + 0) % 25 = 0 -> 'A'

    #tekst = "Z"
    #klucz = "A"  # Przesunięcie o 0

    #wynik = vigenere_cipher(tekst, klucz)

    # Ten assert zawiedzie (rzuci błąd), jeśli w kodzie jest % 25
    # Bo funkcja zwróci "A" zamiast oczekiwanego "Z"
    #assert wynik == "Z", f"Błąd! Oczekiwano 'Z', a otrzymano '{wynik}'. Prawdopodobnie złe modulo!"


# --- ZINTEGROWANE TESTY SZYFROWANIA (Osoba A i B) ---
@pytest.mark.parametrize("tekst, klucz, expected", [
    # Dane z pierwszej listy
    ("AAA", "BCD", "BCD"),
    ("XYZ", "B", "YZA"),
    ("", "KLUCZ", ""),
    ("ABC", "A", "ABC"),
    ("hello", "key", "RIJVS"),
    ("Hello World", "abc", "HFNLP YOSND"),
    # Dane z drugiej listy
    ("PYTHON", "ABC", "PZVHPP"),
    ("ZZZ", "B", "AAA"),
], ids=[
    "przesuniecie_BCD", "koniec_alfabetu", "pusty_napis", "zero_shift",
    "male_litery", "spacje_i_mieszane", "standardowe_szyfrowanie", "zawijanie_alfabetu"
])

def test_vigenere_encrypt_ids(tekst, klucz, expected):
    assert vigenere_cipher(tekst, klucz) == expected


# --- TESTY ODSZYFROWYWANIA ---
@pytest.mark.parametrize("zaszyfrowany, klucz, expected", [
    ("PZVHPP", "ABC", "PYTHON"),
    ("BCD", "BCD", "AAA"),
], ids=[
    "odszyfrowanie_standard", "odszyfrowanie_to_samo"
])

def test_vigenere_decrypt_ids(zaszyfrowany, klucz, expected):
    assert vigenere_decrypt(zaszyfrowany, klucz) == expected


