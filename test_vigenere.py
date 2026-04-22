from vigener import vigenere_cipher
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

