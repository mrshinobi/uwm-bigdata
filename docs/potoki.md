# Potoki w Unix/Linux

Potoki (ang. "pipes") to narzędzie w systemach Unix i Linux, które pozwala na przekazywanie danych
z wyjścia jednego programu do wejścia innego programu.


## Jak działają?

Potoki pozwalają na tworzenie ciągów poleceń, gdzie wynik jednego polecenia jest natychmiast przekazywany
jako wejście do kolejnego polecenia. To przekazywanie odbywa się w czasie rzeczywistym, dzięki czemu drugie
polecenie może zacząć przetwarzanie danych od razu po otrzymaniu pierwszych fragmentów danych z pierwszego polecenia.

Fizycznym mechanizmem komunikacji jest komunikacja międzyprocesowa (IPC), która pozwala na przekazywanie danych między
procesami w systemie operacyjnym. Potoki są jednym z najczęściej używanych mechanizmów IPC w systemach Unix/Linux.


### Przykład użycia potoku

Przykład użycia potoku do wyszukiwania określonych danych w plikach i policzenia ich ilości:

```bash
grep 'szukany_tekst' plik.txt | wc -l
```

gdzie:

- `grep 'szukany_tekst' plik.txt` - wyszukuje w pliku `plik.txt` linie zawierające tekst `szukany_tekst`
- `wc -l` - zlicza ilość linii przekazanych do niego z poprzedniego polecenia
- `|` - to operator potoku, który przekazuje wynik z lewej strony do polecenia po prawej stronie


### Przykłady potoków

- `cat plik.txt | grep 'szukany_tekst' | wc -l` - wyświetla zawartość pliku `plik.txt`, następnie filtruje linie zawierające `szukany_tekst` i zlicza ich ilość
- `ls -l | grep 'plik'` - wyświetla listę plików w bieżącym katalogu, a następnie filtruje wynik, wyświetlając tylko te linie, które zawierają słowo `plik`
- `cat plik.txt | grep 'szukany_tekst' | sort` - wyświetla zawartość pliku `plik.txt`, następnie filtruje linie zawierające `szukany_tekst` i sortuje wynik
- `ps aux | grep 'proces' | awk '{print $2}'` - wyświetla listę wszystkich procesów, filtruje te zawierające słowo `proces`, a następnie wyświetla ich identyfikatory PID


## Zalety używania potoków

* **Efektywność**: Potoki pozwalają na przetwarzanie danych bez potrzeby zapisywania tymczasowych danych na dysku.
* **Elastyczność**: Łączenie wielu poleceń w jeden ciąg pozwala na wykonanie skomplikowanych operacji przetwarzania danych.
* **Szybkość**: Przekazywanie danych bezpośrednio między programami jest szybsze niż w przypadku przetwarzania plików tymczasowych.


## Ograniczenia potoków

* Sekwencyjne przekazywanie danych może nie nadawać się do zadań, które wymagają dostępu losowego do danych lub wielowątkowości.
* Potoki nie są zalecane do przetwarzania dużych zbiorów danych, ponieważ mogą prowadzić do problemów z wydajnością.


## Porównanie potoków Linux, Python i przetwarzania strumieniowego w Hadoop

## Potoki w Linux

### Charakterystyka
- **Linia poleceń**: Składają się z połączonych poleceń systemowych, gdzie wyjście jednego polecenia jest bezpośrednio przekazywane do wejścia kolejnego polecenia.
- **Synchroniczność**: Dane przepływają sekwencyjnie od początku do końca potoku.
- **Ograniczenia**: Przetwarzanie jest ograniczone do możliwości pojedynczego systemu.

### Zastosowanie
- Idealne do prostych zadań przetwarzania danych takich jak sortowanie, filtrowanie i podstawowa analiza danych.

## Tworzenie potoków w Pythonie

### Charakterystyka
- **Kodowanie skryptów**: Umożliwia tworzenie potoków danych poprzez skrypty, które mogą czytać i pisać do standardowego wejścia i wyjścia.
- **Elastyczność**: Możliwość użycia szerokiej gamy bibliotek do przetwarzania danych.
- **Złożoność**: Większa kontrola nad logiką przetwarzania, co pozwala na realizację bardziej złożonych scenariuszy.

### Zastosowanie
- Dobrze sprawdza się w automatyzacji zadań, przetwarzaniu danych oraz integracji z innymi aplikacjami i usługami.

## Przetwarzanie strumieniowe w Hadoop

### Charakterystyka
- **Dystrybucja**: Przetwarzanie danych odbywa się na wielu węzłach równocześnie, co jest idealne do obsługi bardzo dużych zbiorów danych.
- **Skalowalność**: Hadoop jest zaprojektowany do efektywnego skalowania w poziomie.
- **Elastyczność**: Obsługuje różnorodne formaty danych i źródła danych dzięki różnym narzędziom ekosystemu Hadoop.

### Zastosowanie
- Idealne do przetwarzania dużych zbiorów danych w czasie rzeczywistym, analityki big data i zadań wymagających intensywnego przetwarzania danych.

## Podsumowanie

Każde z rozważanych rozwiązań ma swoje miejsce w ekosystemie przetwarzania danych:

- **Potoki Linux** są szybkie i wydajne dla prostych zadań przetwarzania na pojedynczych maszynach.
- **Python** oferuje większą elastyczność i moc w tworzeniu złożonych potoków przetwarzania danych z możliwością integracji z różnymi systemami.
- **Hadoop** jest najlepszy dla skomplikowanych przetwarzań w dużych klastrach, zapewniając wysoką przepustowość i skalowalność.

Wybór odpowiedniej technologii zależy od specyfiki zadania, dostępnych zasobów oraz wymagań dotyczących przetwarzania danych.
