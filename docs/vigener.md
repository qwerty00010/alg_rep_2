# Szyfr Vigenère'a

<div style = "text-align: center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1280px-Python-logo-notext.svg.png" width="100" alt="Python Logo" >
</div>

### Opis działania szyfru
Szyfr Vigenère’a to klasyczny szyfr polialfabetyczny. Działa on poprzez przesuwanie liter tekstu jawnego o wartość odpowiadającą kolejnym literom słowa kluczowego. W przeciwieństwie do szyfru Cezara, przesunięcie nie jest stałe - zmienia się w zależności od pozycji litery w tekście.

---

### Dokumentacja kodu

#### Dostępne funkcje:
`vigenere_cipher(tekst, klucz)`

### Parametry:

- **tekst** | `string` | Wiadomość, którą chcesz zaszyfrować. 
-  **klucz** | `string` | Słowo kluczowe definiujące przesunięcia.

**Co zwraca funkcja:**
* Zwraca `string` – tekst zaszyfrowany (tylko litery alfabetu łacińskiego są szyfrowane, inne znaki pozostają bez zmian).
* Rzuca błąd `ValueError`, jeśli klucz jest pusty lub nie został podany.

---

### 💻 Implementacja

```python
def vigenere_cipher(tekst, klucz):
    """
    Szyfruje tekst jawny przy użyciu klucza metodą Vigenère'a.
    """
    if klucz is None or klucz == "":
        raise ValueError("Błędny klucz - klucz nie może być pusty!")
        
    zaszyfrowany_tekst = ""
    key_index = 0

    # Ujednolicenie wielkości liter
    tekst = tekst.upper()
    klucz = klucz.upper()

    for litera in tekst:
        if litera.isalpha():  
            # Wartość liczbowa litery tekstu (0-25)
            tekst_val = ord(litera) - ord('A')

            # Wartość liczbowa aktualnej litery klucza
            klucz_litera = klucz[key_index % len(klucz)]
            klucz_val = ord(klucz_litera) - ord('A')

            # Obliczenie nowej litery (modulo 26)
            zaszyfrowana_val = (tekst_val + klucz_val) % 26
            zaszyfrowany_tekst += chr(zaszyfrowana_val + ord('A'))

            key_index += 1
        else:
            # Znaki niebędące literami dodajemy bez zmian
            zaszyfrowany_tekst += litera

    return zaszyfrowany_tekst
```

---

### Przykład użycia

```python
tekst_jawny = "Hello World"
klucz = "PYTHON"

wynik = vigenere_cipher(tekst_jawny, klucz)
print(f"Zaszyfrowany tekst: {wynik}") 
# Wynik: WCEEY LCEKW
```

