# 🍕 Pizza Picker

Mała aplikacja Flask, która zwraca propozycję pizzy na podstawie preferencji.

## Uruchomienie lokalne
```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app app run
```

## Testy
```bash
pytest -q
```

## CI/CD
Workflow `.github/workflows/ci-cd.yml` buduje, testuje i wdraża do Azure Web App.

## Deployment
1. Utwórz zasoby Azure (`az group`, `az appservice plan`, `az webapp`).
2. Wygeneruj service principal (`az ad sp create-for-rbac --sdk-auth`).
3. Dodaj sekrety `AZURE_CREDENTIALS` i `AZURE_WEBAPP_NAME` w GitHub.
