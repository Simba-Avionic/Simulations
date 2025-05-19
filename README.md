# Simulations

## Korzystanie z projektu

### Instalacja

1. Utwórz środowisko Pythona:
   ```bash
   python -m venv .venv
   ````

2. Zainstaluj zależności:

   ```bash
   pip install -r tools/requirements.txt
   ```

## 🧩 1. Plik YAML: **dane_symulacji_rocketpy.yaml**

**Zawiera: parametry fizyczne i środowiskowe rakiety**

### 🎯 Cel:

Umożliwia przeprowadzenie realistycznej symulacji lotu rakiety — zawiera wszystkie **fizyczne parametry wejściowe**. Plik ten jest bezpośrednio przetwarzany przez symulator.

> 🔧 Użytkownik: inżynier mechanik lub osoba wykonująca symulację

---

## 📈 2. Plik YAML: **Konfiguracja wyświetlania / wizualizacji**
> ⚠️ NOW NOT IMPLEMENTED

**Zawiera: informacje o tym, co chcemy zobaczyć po symulacji**

### 📌 Przykładowe dane:

* które wykresy mają być wygenerowane (ciąg vs czas, wysokość vs czas, prędkość)
* które dane mają być eksportowane do pliku CSV

### 🎯 Cel:

Steruje **wizualizacją wyników symulacji**, ale nie wpływa na sam przebieg symulacji. Umożliwia dostosowanie widoku wyników do potrzeb konkretnego testu.

> 🔧 Użytkownik: operator symulacji, osoba analizująca dane

---

## 📡 3. Plik YAML: **Konfiguracja sensorów i formatów danych awioniki**

> ⚠️ WORK IN PROGRESS

**Zawiera: ustawienia wymagane przez avionike**

### 📌 Przykładowe dane:

* jakie sensory są aktywne (np. akcelerometr, barometr, GPS)
* częstotliwość zapisu każdego sensora (np. 100 Hz, 10 Hz)
* format danych do zapisu (np. CSV)
* offsety, kalibracje

### 🎯 Cel:

Ten plik jest używany przez awionikę do poprawnego zbierania i zapisywania danych z misji. **Nie wpływa na symulację**, ale pozwala zintegrować ją z prawdziwym systemem pokładowym.

> 🔧 Użytkownik: elektronik / programista awioniki

---

## 🧠 Podsumowanie: jak to wszystko działa razem

| Plik YAML              | Co zawiera?                     | Kto go używa?            | Główne zastosowanie           |
| ---------------------- | ------------------------------- | ------------------------ | ----------------------------- |
| `simulation.yaml`      | Parametry rakiety i środowiska  | Mechanik                 | Symulacja fizyczna lotu       |
| `visualization.yaml`   | Co i jak wyświetlić             | Analityk / operator      | Wizualizacja wyników          |
| `avionics_config.yaml` | Ustawienia sensorów i logowania | Elektronik / programista | Zbieranie danych na pokładzie |


---

# 📘 Instrukcja formatowania plików YAML

## 📄 Co to jest YAML?

YAML to prosty format plików tekstowych używany do zapisywania danych w sposób czytelny dla człowieka i maszyny. W naszym projekcie służy np. do definiowania parametrów symulacji rakiety.

---

## ✅ Zasady formatowania YAML w naszym projekcie

Poniżej znajdują się zasady, których należy przestrzegać przy edycji lub tworzeniu plików `.yaml`:

---

### 1. **Maksymalna długość linii: 120 znaków**

* Staraj się, aby każda linia miała **maksymalnie 120 znaków**.
* Przekroczenie tego limitu nie przerwie działania, ale jest oznaczone jako **ostrzeżenie**.
* Ułatwia to czytanie plików w edytorze i przeglądarce kodu.

---

### 2. **Wcięcia: 2 spacje**

* Używaj **dokładnie 2 spacji** do wcięć (nie używaj tabulatorów).
* Przykład:

  ```yaml
  rakieta:
    masa: 25.0
    silniki:
      - typ: stały
      - typ: ciekły
  ```

---

### 3. **Listy: spójne wcięcia**

* Każdy element listy (`-`) powinien być **wcięty zgodnie z poprzednimi**.
* Przykład poprawny:

  ```yaml
  silniki:
    - typ: stały
    - typ: ciekły
  ```

---

### 4. **Brak zbędnych spacji na końcu linii**

* Nie zostawiaj **spacji na końcu linii** – powoduje to błędy lintowania.
* Twój edytor może mieć opcję automatycznego ich usuwania.

---

### 5. **Wartości logiczne: tylko `true` lub `false`**

* Do wyrażania wartości logicznych używaj **wyłącznie `true` lub `false`** (nie `yes/no`, `on/off` itd.).
* Przykład poprawny:

  ```yaml
  symulacja:
    zapis_logu: false
  ```

---

### 6. **Komentarze: 2 spacje po znaku `#`**

* Komentarz powinien być oddzielony **dwoma spacjami** od treści:

  ```yaml
  masa: 25.0  #  masa startowa w kilogramach
  ```

---

### 7. **Puste linie: maksymalnie 1 z rzędu**

* Nie używaj więcej niż **1 pustych linii pod rząd** w pliku.
* Przykład poprawny:

  ```yaml
  rakieta:
    masa: 25.0

  symulacja:
    czas: 10.0
  ```

---

### 8. **Nie powtarzaj nazw kluczy**

* Każda nazwa (klucz) może wystąpić tylko **raz w danym bloku**.
* Błąd (to nadpisuje wcześniejszą wartość!):

  ```yaml
  rakieta:
    masa: 25.0
    masa: 30.0  # ❌ błąd: powtórzony klucz
  ```

---

## 🛠️ Narzędzia wspomagające

* Używaj edytora, który podświetla składnię YAML i automatycznie usuwa końcowe spacje (np. VS Code z rozszerzeniem **YAML**).
* Pliki są automatycznie sprawdzane przez system CI na GitHub – błędy formatowania zablokują zatwierdzenie zmian.

---

## ℹ️ Potrzebujesz pomocy?

Jeśli nie jesteś pewien, czy plik jest poprawny – zapytaj osobę techniczną z zespołu lub uruchom komendę:
```bash
yamllint -c tools/.yamllint <nazwa_pliku>.yaml
```
```bash
 pykwalify -d dane_symulacji_rocketpy.yaml -s tools/data_schema.yml 
```


przed 1 uruchomieniem wymagane zainstalowanie yamllint:
```
pip install yamllint
```
