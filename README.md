# Pizza Picker

**Pizza Picker** to prosta aplikacja webowa stworzona w Pythonie z użyciem frameworka Flask. Pozwala użytkownikowi losowo wybrać jedną z dostępnych pizz z listy oraz pizzerię w której chcemy zjeść pizzę bez zbędnego zastanawiania się. Projekt zawiera elementy CI/CD oraz wdrożenie na platformie Azure.

---

## Struktura projektu

```
pizza-picker/
│
├── app.py                 # Główna aplikacja Flask
├── requirements.txt       # Wymagane pakiety
├── tests/                 # Testy jednostkowe
│   └── test_app.py
├── .github/
│   └── workflows/
│       └── main.yml       # Pipeline GitHub Actions
├── README.md              # Dokumentacja projektu
```

---

## Jak uruchomić lokalnie

1. **Klonuj repozytorium:**

```bash
git clone https://github.com/TWOJE_REPO/pizza-picker.git
cd pizza-picker
```

2. **Utwórz środowisko wirtualne i aktywuj:**

```bash
python -m venv venv
venv\Scripts\activate      # Windows
```

3. **Zainstaluj zależności:**

```bash
pip install -r requirements.txt
```

4. **Uruchom aplikację:**

```bash
python app.py
```

---

## Testy

Aby uruchomić testy:

```bash
pytest
```

---

## CI/CD (GitHub Actions)

Projekt wykorzystuje GitHub Actions do:

- automatycznego uruchamiania testów
- deploymentu na Azure Web App

Plik workflow znajduje się w: `.github/workflows/main.yml`

---

## Deployment

Aplikacja została wdrożona na platformie **Azure** z użyciem usługi **App Service**. Wykorzystano sekrety GitHub do przechowywania:

- `AZURE_WEBAPP_NAME`
- `AZURE_WEBAPP_PUBLISH_PROFILE`

W razie potrzeby możesz zaktualizować te dane w ustawieniach repozytorium na GitHubie.

---

## Technologie

- Python 3.9
- Flask
- GitHub Actions (CI/CD)
- Azure App Service

---

## Licencja
Ten projekt udostępniany jest na licencji MIT.
Możesz korzystać, modyfikować i rozpowszechniać go zgodnie z warunkami licencji.

---

##  Autor

Jan Kurczab WSB
