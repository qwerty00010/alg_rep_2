# Dokumentacja szyfru Cezara

### Krótkie działanie szyfru
Szyfr Cezara przesuwa litery w tekście o określoną liczbę miejsc w alfabecie.

### Dostępne funkcje w kodzie
* `cezar(napis, klucz)`

### Argumenty (parametry) funkcji
* `napis` – tekst, który chcemy zmienić.
* `klucz` – o ile miejsc przesunąć litery.

### Co funkcja zwraca
Funkcja zwraca zmieniony tekst (zaszyfrowany lub odszyfrowany).

### Przykłady użycia (kod)
```python
from cezar import cezar

# Przykład szyfrowania
wynik = cezar("abc", 1)
print(wynik)  # pokaże: bcd