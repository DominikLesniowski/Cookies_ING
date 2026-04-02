## Uruchomienie lokalne

### 1. Sklonuj repozytorium

```bash
git clone https://github.com/DominikLesniowski/ING_Cookies_Test.git
cd ING_Cookies_Test
```

### 2. Utwórz i aktywuj wirtualne środowisko

```bash
python3 -m venv venv
```

- **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

### 3. Zainstaluj zależności

```bash
pip install -r requirements.txt
playwright install
```

### 4. Uruchom testy

**Sekwencyjnie na wszystkich przeglądarkach:**
```bash
 pytest --browser chromium --browser firefox --browser webkit -v  
```

**Równolegle na wszystkich przeglądarkach jednocześnie (wymaga pytest-xdist):**
```bash
 pytest --browser chromium --browser firefox --browser webkit -v -n 3
```

Flaga `-n 3` uruchamia 3 workerów — po jednym na każdą przeglądarkę.

**Na wybranej przeglądarce:**
```bash
pytest  --browser chromium  -v
pytest  --browser Firefox -v
pytest  --browser webkit -v
```

---

<!-- ## GitHub Actions — pipeline

Pipeline zdefiniowany w `.github/workflows/tests.yml` uruchamia testy **równolegle** na trzech przeglądarkach przy każdym pushu lub pull requeście do gałęzi `main`.

Każdy job instaluje osobną instancję przeglądarki i uruchamia testy niezależnie. Flaga `fail-fast: false` zapewnia, że niepowodzenie jednego joba nie anuluje pozostałych — widać wyniki dla każdej przeglądarki osobno.

Możesz też uruchomić pipeline ręcznie przez zakładkę **Actions → Run workflow** w repozytorium GitHub. -->
