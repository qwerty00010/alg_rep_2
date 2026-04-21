import pytest
from vigener import vigenere_cipher, generate_key

def test_vigenere_encryption():

    assert vigenere_cipher("KOT", "A", mode='encrypt') == "KOT"

def test_vigenere_decryption():

    zaszyfrowane = vigenere_cipher("PYTHON", "KEY", mode='encrypt')
    assert vigenere_cipher(zaszyfrowane, "KEY", mode='decrypt') == "PYTHON"

def test_key_generator():

    klucz = generate_key(10)
    assert len(klucz) == 10
    assert isinstance(klucz, str)