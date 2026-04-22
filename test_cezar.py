import pytest
from cezar import cezar

@pytest.fixture
def tekst_bazowy():
    return "Test"

@pytest.mark.basic
@pytest.mark.parametrize("napis, klucz, expected", [
    ("abc", 1, "bcd"),
    ("xyz", 2, "zab"),
], ids=["przesuniecie_1", "zawijanie_alfabetu"])
def test_cezar_param(napis, klucz, expected):
    assert cezar(napis, klucz) == expected

@pytest.mark.exceptions
def test_cezar_errors():
    with pytest.raises(TypeError):
        cezar(123, "klucz")

@pytest.mark.extended
def test_cezar_z_fixture(tekst_bazowy):
    # Sprawdza znaki specjalne i używa danych z fixture
    assert cezar(tekst_bazowy + "!", 1) == "Uftu!"