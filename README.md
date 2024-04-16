# Badanie perspektyw zawodowych absolwentów kierunku informatyka na polskich uczelniach

## Spis treści

1. [Tytuł pracy](#tytuł-pracy)
2. [Autorzy](#autorzy)
3. [Streszczenie](#streszczenie)
4. [Słowa kluczowe](#Słowa-Kluczowe)
5. [Wprowadzenie](#wprowadzenie)
6. [Przedmiot badania](#przedmiot-badania)
   - [Cel i zakres badania](#cel-i-zakres-badania)
   - [Przegląd literatury](#przegląd-literatury)
   - [Zmienne wybrane do analizy](#zmienne-wybrane-do-analizy)
   - [Wstępna analiza danych](#wstępna-analiza-danych)
     - [Statystyki opisowe](#statystyki-opisowe)
     - [Podstawowa wizualizacja](#podstawowa-wizualizacja)
     - [Braki danych](#braki-danych)
     - [Działanie programu uzupełniającego puste dane](#działanie-programu-uzupełniającego-puste-dane)
     - [Fragmenty kodu](#fragmenty-kodu)
     - [Obserwacje odstające](#obserwacje-odstające)
7. [Opis metod](#opis-metod)
   - [Analiza metodą Hellwiga](#analiza-metodą-hellwiga)
   - [Analiza metodą MUZ](#analiza-metodą-muz)
   - [Analiza metodą TOPSIS](#analiza-metodą-topsis)
   - [Analiza metodą Nowak](#analiza-metodą-nowak)
   - [Analiza metodą STRAHL](#analiza-metodą-strahl)
   - [Analiza metodą SSW](#analiza-metodą-ssw)
8. [Podsumowanie](#podsumowanie)
   - [Ocena realizacji celu](#ocena-realizacji-celu)
   - [Odniesienie do pozycji z przeglądu literatury](#odniesienie-do-pozycji-z-przeglądu-literatury)
8. [Rezultaty](#rezultaty)
   - [Tabele i grafiki](#tabele-i-grafiki)
   - [Omówienie wyników](#omówienie-wyników)
9. [Bibliografia](#bibliografia)

    
# Tytuł pracy
Badanie perspektyw zawodowych absolwentów kierunku informatyka na polskich uczelniach

# Autorzy
- Katarzyna Dudek 217369
- Jakub Czabok 217293
- Karolina Dekajło 217482
- Mateusz Chudowolski 217330

# Streszczenie
<div align="justify">
Niniejsza analiza prezentuje badanie ekonomicznej sytuacji absolwentów studiów informatycznych w Polsce. Wykorzystując metody statystyczne do porządkowania danych, zostanie stworzony ranking, umożliwiający porównanie uśrednionej sytuacji ekonomicznej po ukończeniu poszczególnych programów studiów.
</div>

# Słowa kluczowe
<div align="justify">
Perspektywy zawodowe, Absolwenci, Kierunek informatyka, Polskie uczelnie, Analiza ekonomiczna, Statystyki zarobków, Zatrudnienie absolwentów, Badanie empiryczne, Porządkowanie obiektów, Metody statystyczne, Ranking uczelni, Sytuacja ekonomiczna, Wynagrodzenia absolwentów, Mediana zarobków, Analiza danych, Techniki statystyczne, Obserwacje odstające, Badanie empiryczne, Kryteria skrajne, Metoda TOPSIS, Metoda Hellwiga, Metoda MUZ, Analiza porządkowania liniowego, Hierarchiczne uporządkowanie, Perspektywy zawodowe absolwentów, Zarobki absolwentów, Przegląd literatury, Uczenie się na studiach drugiego stopnia, Praca po ukończeniu studiów, Edukacja wyższa, Kształcenie informatyczne, Analiza danych społecznych, Rola uczelni w kształceniu zawodowym, Porównanie programów studiów, Studia informatyczne a kariera zawodowa, Technologie informacyjno-komunikacyjne a rynek pracy, Trendy w kształceniu informatycznym, Dynamika rynku pracy dla absolwentów, Działanie programu uzupełniającego puste dane, Ocena realizacji celu badania, Znaczenie wyboru uczelni i programu studiów, Ekonomiczne losy absolwentów, Literatura przedmiotu, Skuteczność metod analizy danych, Badanie perspektyw zawodowych, Znaczenie doświadczenia zawodowego, Analiza porównawcza, Metody badawcze, Ewaluacja efektów kształcenia, Badania empiryczne w zakresie edukacji informatycznej, Perspektywy rozwoju zawodowego, Kariery zawodowe w branży IT, Sytuacja rynku pracy dla informatyków, Znaczenie umiejętności informatycznych na rynku pracy, Ocena jakości kształcenia informatycznego, Tendencje na rynku pracy dla informatyków, Potencjał rynku pracy dla absolwentów kierunku informatyka, Wyzwania związane z zatrudnieniem absolwentów informatyki, Prognoza zmian na rynku pracy dla informatyków, Tendencje rozwojowe w sektorze IT, Ewaluacja efektywności kształcenia informatycznego, Ocena jakości kształcenia informatycznego, Znaczenie dodatkowych kwalifikacji dla kariery informatyka, Perspektywy zatrudnienia dla specjalistów informatycznych, Skuteczność programów studiów informatycznych, Analiza dynamiki rynku pracy dla informatyków, Perspektywy rozwoju zawodowego w branży IT, Trendy w zatrudnieniu absolwentów kierunku informatyka, Wpływ wyboru uczelni na perspektywy zawodowe, Ocena skuteczności programów studiów informatycznych, Znaczenie praktyk zawodowych dla absolwentów informatyki, Perspektywy kariery w branży IT, Analiza trendów rozwojowych w branży informatycznej, Rola edukacji informatycznej w kształtowaniu rynku pracy, Wpływ specjalizacji na perspektywy zawodowe, Perspektywy rozwoju branży IT na polskim rynku pracy, Znaczenie praktycznych umiejętności dla kariery informatyka, Analiza wpływu edukacji informatycznej na dynamikę rynku pracy, Ocena efektywności programów kształcenia informatycznego, Trendy w zatrudnieniu absolwentów kierunku informatyka, Perspektywy rozwoju zawodowego dla specjalistów IT, Wpływ doświadczenia zawodowego na karierę informatyka, Analiza zmian na rynku pracy dla informatyków, Ocena efektywności kształcenia informatycznego, Znaczenie kontynuacji nauki na studiach drugiego stopnia, Perspektywy zawodowe po kontynuacji nauki na studiach drugiego stopnia, Trendy w kontynuacji nauki na studiach drugiego stopnia, Wpływ uczelni na kontynuację nauki na studiach drugiego stopnia, Analiza danych społeczno-ekonomicznych
</div>

# Wprowadzenie
Absolwenci kierunku informatyka odgrywają kluczową rolę w dzisiejszym społeczeństwie opartym na technologii. Jednakże, ich ekonomiczne losy po ukończeniu studiów mogą znacząco się różnić w zależności od wielu czynników. Niniejsza praca ma na celu zbadanie tych różnic oraz stworzenie rankingów porównujących sytuację ekonomiczną absolwentów poszczególnych uczelni i programów studiów informatycznych w Polsce.

# Przedmiot badania
Celem badania jest zastosowanie metod statystycznych porządkowania obiektów w celu utworzenia rankingów porównujących uśrednione sytuacje ekonomiczne absolwentów studiów informatycznych w Polsce. Analiza obejmuje zmienne takie jak zarobki po ukończeniu studiów, stopień zatrudnienia, lokalizacja zatrudnienia oraz ewentualne dodatkowe kwalifikacje. W literaturze istnieją badania pokazujące, że wybór konkretnej uczelni czy specjalizacji może mieć istotny wpływ na karierę zawodową i zarobki absolwentów.

## Cel i zakres badania
**Cel**

Celem badania jest zrozumienie perspektyw zawodowych absolwentów kierunku informatyka na polskich uczelniach poprzez analizę ich perspektyw zawodowych po ukończeniu studiów. Chcemy zbadać wpływ różnych czynników, takich jak uczelnia, program studiów, doświadczenie zawodowe zdobywane podczas studiów, na zarobki i zatrudnienie absolwentów. Naszym celem jest stworzenie rankingów, które pozwolą porównać uśrednione sytuacje zawodowe absolwentów różnych programów studiów informatycznych na polskich uczelniach.

**Zakres**

Badanie będzie obejmować analizę sytuacji zawodowej absolwentów kierunku informatyka na polskich uczelniach. Będziemy korzystać z metod statystycznych, takich jak analiza porządkowania liniowego (metoda Hellwiga, metoda MUZ), oraz analiza TOPSIS. Obejmuje to zbieranie danych dotyczących zarobków po ukończeniu studiów, stopnia zatrudnienia, lokalizacji zatrudnienia oraz ewentualnych dodatkowych kwalifikacji. Analiza będzie opierać się na zestawie zmiennych, które zostały wybrane na podstawie przeglądu literatury oraz ich istotności w kontekście badanej problematyki. Dodatkowo, w ramach badania przeprowadzona zostanie wstępna analiza danych, w tym statystyki opisowe, podstawowa wizualizacja danych oraz obsługa brakujących danych.

## Przegląd literatury
W ramach porównania do naszej analizy wybraliśmy ranking polskich uczelni względem kierunku "Informatyka" przygotowany przez "Perspektywy".

Metodologia ich analizy obejmuje takie czynniki jak:
1. **Prestiż uczelni:** Ocena przez kadrę akademicką, liczba wskazań danej uczelni w badaniu ankietowym wśród kadry akademickiej.
2. **Losy zawodowe absolwentów:** Wskaźnik mierzony wysokością zarobków absolwentów uczelni oraz stopniem ich zatrudnienia.
3. **Potencjał akademicki:** Określony poprzez ocenę kategorii naukowej uczelni.
4. **Potencjał dydaktyczny:** Liczba posiadanych aktualnych akredytacji i certyfikatów międzynarodowych oraz jakość przyjętych na studia.
5. **Potencjał naukowy:** Liczba publikacji, cytowalność, wskaźnik FWCI, FWVI oraz obecność publikacji w top 10% najczęściej cytowanych czasopismach.
6. **Umiędzynarodowienie:** Udział publikacji we współpracy zagranicznej oraz liczba studentów obcokrajowców.

Pozostałymi pracami, na które warto zwrócić uwagę są te, w których wykorzystywaną są wspólne metody analizy statystycznej.



## Zmienne wybrane do analizy:

| Skrót zmiennej         | Opis                                                                                                                                       | Rodzaj zmiennej   |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| P_CZY_BEZR_P1          | Procent absolwentów, którzy mieli doświadczenie bycia bezrobotnym w pierwszym roku po uzyskaniu dyplomu                                   | Destymulanta       |
| P_CZY_BEZR_P4          | Procent absolwentów, którzy mieli doświadczenie bycia bezrobotnym w czwartym roku po uzyskaniu dyplomu                                      | Destymulanta       |
| P_ME_ZAR_STUD_P1       | Mediana średnich miesięcznych wynagrodzeń absolwentów ze wszystkich źródeł w pierwszym roku po uzyskaniu dyplomu w okresach, gdy studiowali po uzyskaniu dyplomu | Stymulanta         |
| P_ME_ZAR_STUD_P4       | Mediana średnich miesięcznych wynagrodzeń absolwentów ze wszystkich źródeł w czwartym roku po uzyskaniu dyplomu w okresach, gdy studiowali po uzyskaniu dyplomu    | Stymulanta         |
| P_IF_2st               | Procent osób, które po ukończeniu studiów I stopnia podjęły studia II stopnia w pierwszym roku po uzyskaniu dyplomu                        | Stymulanta         |
| P_IF_2st_ucz           | Procent osób kontynuujących studia I stopnia na studiach II stopnia kiedykolwiek w badanym okresie, które kontynuują je na tej samej uczelni | Stymulanta         |
| P_ME_ZAR_ETAT_DOSW_P4 | Mediana średnich miesięcznych wynagrodzeń z tytułu umów o pracę w czwartym roku po uzyskaniu dyplomu absolwentów wśród absolwentów z doświadczeniem pracy przed uzyskaniem dyplomu | Stymulanta         |
| P_ME_ZAR_ETAT_NDOSW_P4| Mediana średnich miesięcznych wynagrodzeń z tytułu umów o pracę w czwartym roku po uzyskaniu dyplomu absolwentów nie wśród absolwentów z doświadczeniem pracy przed uzyskaniem dyplomu | Stymulanta         |


**Uzasadnienie:**

- **Destymulanty:** Zmienne `P_CZY_BEZR_P1` i `P_CZY_BEZR_P4` są istotne, ponieważ odzwierciedlają procent absolwentów, którzy mieli doświadczenie bycia bezrobotnym w pierwszym i czwartym roku po uzyskaniu dyplomu. Stanowią istotne wskaźniki niepewności ekonomicznej po ukończeniu studiów.

- **Stymulanty:** Pozostałe zmienne, takie jak `P_ME_ZAR_STUD_P1`, `P_ME_ZAR_STUD_P4`, `P_ME_ZAR_ETAT_DOSW_P4` oraz `P_ME_ZAR_ETAT_NDOSW_P4`, odzwierciedlają różne aspekty sytuacji ekonomicznej absolwentów, takie jak poziom wynagrodzeń, czy mediany wynagrodzeń w zatrudnieniu etatowym z i bez doświadczenia pracy przed uzyskaniem dyplomu. Pozwalają one na zrozumienie różnic w zarobkach wśród absolwentów kierunku informatyka na polskich uczelniach. Aby wyniki były jak najbardzie obiektywne, rozdzieliliśmy czas (1 rok- zaraz po studiach i 4 lata- po zdobyciu pierwszych doświadczeń na rynku), co zmiejsza znacząco losowość analizy. Użyliśmy do analizy rówenież `P_IF_2st`, `P_IF_2st_ucz`, które mówią o kontynuacji nauki na wyższym poziomie na danej uczelni. Zakładamy, że im lepsza uczelnia, tym częściej jej studenci zdecydują się na kontynuacje tam studiów drugiego stopnia, zamiast podejmować te studia na innej uczelni.

**Charakterystyka zmiennych użytych do analizy**

***Podstawowe statystyki:***

![image](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/7c2650bf-641e-4934-9706-600d917403b1)


***Rozkłady zmiennych:***
![Rozkład zmiennej P_CZY_BEZR_P1](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/d0873579-7c43-49ae-88e4-64b5aa0dab5b)

![Rozkład zmiennej P_CZY_BEZR_P4](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/c5fd8867-42f0-49b3-957f-576d58f82832)

![Rozkład zmiennej P_ME_ZAR_STUD_P1](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/fdfd3b2a-3938-45b7-8217-6c76f071dc3a)

![Rozkład zmiennej P_ME_ZAR_STUD_P4](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/81112174-20d6-470a-9ad4-11dc60ed4cba)

![Rozkład zmiennej P_IF_2st](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/0473e689-bac3-4834-8de5-e6856f380a0f)

![Rozkład zmiennej P_IF_2st_ucz](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/9265d54a-2f33-4a0d-bfa5-7ba5ff0daf42)

![P_ME_ZAR_ETAT_DOSW_P4](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/e7bc0ec6-4ce8-425f-af7e-de0085f471cb)

![P_ME_ZAR_ETAT_NDOSW_P4](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/6edce142-54b4-44bf-b1ad-80f84e12470e)


***Dodatkowe cechy zmiennych:***

Większość kierunków informatycznych w Polsce, przyjętych do analizy to kierunki stacjonarne:
![435740204_738431308495392_706943029595757031_n](https://github.com/KDudek1104/computer-science-ranking/assets/139448704/f32d62aa-36d6-431a-afed-493a29ae9ce3)

Jako kierunki informatyczne potraktowaliśmy nie tylko kierunek o nazwie 'Informatyka', ale również kierunki blisko pokrewne. Wykres z liczebnością konkretnych kierunków względem ich nazwy został pokazany poniżej:
![435649959_782637977133761_7021763242141476053_n](https://github.com/KDudek1104/computer-science-ranking/assets/139448704/6c8d5fca-78a3-418f-b749-87db847534eb)

Już przy wstępnej analizie danych widać pierwsze charakterystyczne cechy poszczególnych zmiennych. Poniżej zamieszczony został wykres ukazujący wyraźne różnice między medianą zarobków po informatyce na polskich uczelniach po 1. roku po uzyskaniu dyplomu w porównaniu z 4. rokiem po uzyskaniu dyplomu. Ukazuje to wysoki wpływ doświadczenia zawodowego na wysokość zarobków w tej branży.
![435816852_449924534150871_1923132795031598496_n](https://github.com/KDudek1104/computer-science-ranking/assets/139448704/7da5b713-975e-43a2-9bd3-c805029204a7)

Zauważyliśmy również wyraźną różnicę, chociaż nie tak, jak na poprzednim wykresie, ilustrującą poziom mediany zarobków z umów o pracę u osób z doświadczeniem i osób bez doświadczenia zdobywanego podczas studiów. Osoby pracujące na studiach osiągają wyższe zarobki od niepracujących nawet cztery lata po uzyskaniu dyplomu.
![435634353_782539333826726_6390269249690547385_n](https://github.com/KDudek1104/computer-science-ranking/assets/139448704/08e31fc5-1bc3-4f91-a668-9ffd8a741662)



## Wstępna analiza danych

### Statystyki opisowe
Analiza wyników przy zastosowaniu różnych metod wielokryterialnych wykazała pewne statystycznie istotne tendencje, takie jak wyższe współczynniki dla uczelni publicznych w porównaniu z uczelniami prywatnymi. Wśród analizowanych kierunków, Informatyka na Politechnice Warszawskiej, szczególnie na Wydziale Elektrycznym, konsekwentnie zajmuje pozycję nr 1 niezależnie od zastosowanej metody (MUZ, TOPSIS, NOWAK, SSW, STRAHL). W ścisłej czołówce znajdują się również Informatyka na Politechnice Gdańskiej (Wydział Elektroniki, Telekomunikacji i Informatyki), Informatyka na Politechnice Warszawskiej (Wydział Elektroniki i Technik Informacyjnych), Informatyka na Akademii Górniczo-Hutniczej w Krakowie (Wydział Elektrotechniki, Automatyki, Informatyki i Inżynierii Biomedycznej) oraz Informatyka na Wojskowej Akademii Technicznej im. Jarosława Dąbrowskiego (Wydział Cybernetyki). Warto zauważyć, że wszystkie te programy znajdujące się w pierwszej piątce charakteryzują się silnym profilem technicznym, a także oferują kształcenie w trybie stacjonarnym. Istotnym wnioskiem w naszej analizie jest też duże zróżnicowanie zarobków w zależności od uczelni i wydziału. Ta analiza może być przydatna dla przyszłych studentów oraz instytucji edukacyjnych do lepszego zrozumienia i oceny jakości oferowanych programów studiów.

### Podstawowa wizualizacja

### Braki danych
Braki danych były ważnym problemem w analizie, który należało obsłużyć. Wszystkie uczelnie miały pełne dane dotyczące bezrobocia i procentu osób kontynujących studia 2. stopnia na tej samej uczelni. Niestety, nie dysponowaliśmy przy niektórych pozycjach informacjami odnośnie zarobków (zarówno rok jak i 4 lata po dyplomie). Pozycje, w których brakowało obu kolumn w danym roku po uzyskaniu dyplomu (1 lub 4) zarówno w medianie zarobków z tytułu o prace, jak i medianie zarobków ze wszystkich źródeł, były usuwane. Uważamy, że symulacja tak ważnych kolumn w naszej analizie nie byłaby wystarczająco obiektywna. Jeśli jednak mieliśmy dane odnośnie co najmniej jednej kolumny (patrząc osobno na rok 1. i rok 4.), symulowliśmy dane w kolumnie z tym samym rokiem po uzyskaniu dyplomu. Odpowiednio:
1. Gdy brakowało danej w kolumnie 'P_ME_ZAR_STUD_P1', ale mieliśmy tą daną w kolumnie 'P_ME_ZAR_STUD_P4', mnożyliśmy wartość dla tego wiersza z kolumny 'P_ME_ZAR_STUD_P4' przez współczynnik przejścia między średnią ze wszystkich wartości z kolumny 'P_ME_ZAR_STUD_P1', a 'P_ME_ZAR_STUD_P4'
2. Analogicznie w odwrotnym przypadku (gdy brakowało danej w kolumnie 'P_ME_ZAR_STUD_P4', ale mieliśmy tą daną w kolumnie 'P_ME_ZAR_STUD_P1')
3. Gdy brakowało danej w kolumnie `P_ME_ZAR_ETAT_DOSW_P4`, ale mieliśmy tą daną w kolumnie `P_ME_ZAR_ETAT_NDOSW_P4`, mnożyliśmy wartość dla tego wiersza z kolumny `P_ME_ZAR_ETAT_NDOSW_P4` przez współczynnik przejścia między średnią ze wszystkich wartości z kolumny `P_ME_ZAR_ETAT_DOSW_P4`, a `P_ME_ZAR_ETAT_NDOSW_P4`.
4. Analogicznie w odwrotnym przypadku (gdy brakowało danej w kolumnie `P_ME_ZAR_ETAT_NDOSW_P4`, ale mieliśmy tą daną w kolumnie `P_ME_ZAR_ETAT_DOSW_P4`)

W kolumnach dotyczących procentu osób podejmujących studia drugiego stopnia, w niektórych wierszach wartość była równa 0. Takie przypadki występują, gdy dana uczelnia nie oferuje programów studiów magisterskich z danego kierunku, co może wynikać z różnych czynników, takich jak brak odpowiednich zasobów, niska liczba zainteresowanych studentów lub specyfika profilu uczelni. Uważamy jednak, że nie wymaga to zmiany w naszych obliczeniach, ponieważ brak studiów magisterskich jest ogromną wadą i przeszkodą dla studentów chcących kontynuować studia.

#### Dzialanie programu uzupełniającego puste dane:
1. Program oblicza średnie wartości dla określonych kolumn, które są używane jako współczynniki w symulacji.
2. Tworzy maski dla komórek, które zawierają brakujące dane w poszczególnych kolumnach.
3. Na podstawie tych maski oraz wcześniej obliczonych średnich wartości, program przeprowadza mnożenie wartości w pustych komórkach przez odpowiednie współczynniki. Te współczynniki są stosowane proporcjonalnie do danych w innych kolumnach lub na podstawie innych czynników, które są istotne dla analizy.
4. Wartości te są używane do uzupełnienia brakujących danych, co pozwala zachować spójność i logiczność danych w analizie.

#### Fragmenty kodu:

```python
mean_P_ME_ZAR_STUD_P4 = df['P_ME_ZAR_STUD_P4'].mean()
mean_P_ME_ZAR_STUD_P1 = df['P_ME_ZAR_STUD_P1'].mean()
```
Obliczamy średnie wartości dla kolumn `P_ME_ZAR_STUD_P4` i `P_ME_ZAR_STUD_P1`.

```python
mask_P1 = df['P_ME_ZAR_STUD_P1'].isnull()
df.loc[mask_P1, 'P_ME_ZAR_STUD_P1'] = df.loc[mask_P1, 'P_ME_ZAR_STUD_P4'] * (mean_P_ME_ZAR_STUD_P1 / mean_P_ME_ZAR_STUD_P4)
```
Tworzymy maskę (`mask_P1`), która wskazuje, które wartości w kolumnie `P_ME_ZAR_STUD_P1` są puste. Używamy tej maski do znalezienia odpowiednich wierszy w kolumnie `P_ME_ZAR_STUD_P4`, aby uzyskać wartości, które wykorzystamy do uzupełnienia pustych miejsc w kolumnie `P_ME_ZAR_STUD_P1`. Wartości są uzupełniane na podstawie proporcji między średnimi wartościami `P_ME_ZAR_STUD_P4` i `P_ME_ZAR_STUD_P1`.

Analogiczne operacje wykonywane są dla pozostałych kolumn i wartości.

```python
df.to_excel('uzupelnione.xlsx', index=False)
```
Po uzupełnieniu pustych wartości, zapisujemy zmodyfikowane dane do nowego pliku Excel, który można wykorzystać do dalszych analiz.

### Obserwacje odstające
W naszej analizie ekonomicznych losów absolwentów kierunku informatyka na polskich uczelniach nie było potrzeby obsługiwać obserwacji odstających. Wynika to głównie z charakteru danych oraz sposobu ich zbierania. Dane te są agregatami liczbowymi, takimi jak procent absolwentów w różnych kategoriach, mediany wynagrodzeń i inne miary podobne, które zostały zebrane na poziomie grupy absolwentów. Usunięcie takich obserwacji mogłoby zniekształcić rzeczywisty obraz sytuacji ekonomicznej absolwentów. Jednocześnie, po wstępnej analizie nie zauważyliśmy wyników, które można byloby uznać za nieprawidłowe- a odchylenia- zarówno te większe, jak i mniejsze, są w naszej analizie bardzo ważne i pokazują jak bardzo różnią się losy absolwentów po różnych uczelniach. Dlatego też zdecydowaliśmy się na pozostawienie danych w ich pierwotnej formie, bez dalszego przetwarzania w celu obsługi ewentualnych obserwacji odstających.

# Opis metod

### Analiza metodą Hellwiga
W ramach naszej analizy danych skorzystaliśmy z metody Hellwiga, która została opracowana przez Leo A. Hellwiga w 1972 roku. Jest to jedna z najczęściej stosowanych technik analizy danych, zwłaszcza w kontekście porządkowania liniowego. Metoda ta bazuje na minimalizacji kryteriów skrajnych, co umożliwia wyłonienie istotnych cech lub zmiennych decyzyjnych. Poprzez dokładne porównanie poszczególnych zmiennych, analiza przy użyciu metody Hellwiga pozwala na ich uporządkowanie z uwzględnieniem ich znaczenia w kontekście badanych danych.

Wzór na wartość cechy syntetycznej pochodzący z artykułu: Kukuła, K., Luty, L. (2018) “O Wyborze Metody Porządkowania Liniowego do Oceny Gospodarki odpadami W polsce W Ujęciu Przestrzennym.” Zeszyty Naukowe SGGW w Warszawie - Problemy Rolnictwa Światowego, vol. 18, no. 2: 183–192

![image](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/833d406a-cb2c-476c-82ee-46edb8ea537e)

Pozostałe wzory wykorzystane w analizie tą metodą zaczerpnięte z tego samego artykułu co poprzedni wzór:

![image](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/75a3fda1-3f04-4e43-aa58-0338c25ec1a6)

### Analiza metodą MUZ
W naszym badaniu danych wykorzystaliśmy Metodę Ujednoliconego Zmniejszania (MUZ) do uporządkowania liniowego danych. MUZ, będąca techniką minimalizacji kryteriów skrajnych, umożliwia wyodrębnienie kluczowych cech lub zmiennych decyzyjnych. Poprzez dokładne porównanie poszczególnych zmiennych, analiza za pomocą MUZ pozwoliła nam na ich hierarchiczne uporządkowanie, uwzględniając ich istotność w badanym kontekście.

Wzór na wartość cechy syntetycznej pochodzący z artykułu: Kukuła, K., Luty, L. (2018) “O Wyborze Metody Porządkowania Liniowego do Oceny Gospodarki odpadami W polsce W Ujęciu Przestrzennym.” Zeszyty Naukowe SGGW w Warszawie - Problemy Rolnictwa Światowego, vol. 18, no. 2: 183–192

![image](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/3cd5c0ed-3736-4d67-819e-f2444edc4c3f)

gdzie:

- *Q<sub>i</sub>* to wartość cechy syntetycznej dla obiektu *i* 
- *x<sub>ij</sub>* to nominalna wartość cechy *j* dla obiektu *i*,
- *m* to liczba obiektów,
- *n* to liczba cech dla każdego obiektu.

  
Pozostałe wzory wykorzystane w analizie tą metodą zaczerpnięte z tego samego artykułu co poprzedni wzór:

![image](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/65840d9c-007d-425b-9c6d-4c9dbadd5015)

### Analiza metodą TOPSIS
Jako jedną z metod analizy danych wykorzystaliśmy TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) zaproponowaną w pracy Ching-Lai Hwang, K., Yoon (1981) "Multiple Attribute Decision Making: Methods and Applications" Lecture Notes in Economics and Mathematical Systems vol. 186. 
TOPSIS polega na utworzeniu wzorca jako zestaw najbardziej pożądanych wartości cech oraz antywzorca jako przeciwieństwo reprezentowane przez wektor najmniej pożądanych wartości. Po znormalizowaniu danych wejściowych i utworzeniu wzorca oraz antywzorca wynik analizy TOPSIS to iloraz odległości euklidesowej od antywzorca oraz sumy odległości od wzorca i antywzorca.

W tej metodzie normalizację danych przeprowadza się stosując poniższy wzór zaczerpnięty z pracy G., R.,  Jahanshahloo, F., Hosseinzadeh Lotfi, A., R., Davoodi (2009) "Extension of TOPSIS for decision-making problems with interval data: Interval efficiency" Mathematical and Computer Modelling, Volume 49, Issues 5–6: 1137-1142:

![435608291_1096683048221400_8963528647939478991_n](https://github.com/KDudek1104/computer-science-ranking/assets/139448704/0b4a4ae0-29d9-4dac-9111-37026587cc52)


gdzie:

- *n<sub>ij</sub>* to wartość cechy *j* dla obiektu *i* po znormalizowaniu,
- *x<sub>ij</sub>* to nominalna wartość cechy *j* dla obiektu *i*,
- *m* to liczba obiektów,
- *n* to liczba cech dla każdego obiektu.

W naszym przypadku ze względu na zastosowanie zarówno stymulant jak i destymulant wektor wzorca składa się z wartości maksymalnych każdej cechy po znormalizowaniu będącej stymulantem i minimalnych wartości dla destymulantów, natomiast wektor antywzorca będzie składał się z maksymalnych wartości dla destymulantów a minimalnych dla destymulantów. 


Odległość od wzorca i antywzorca to odpowiednio *d<sub>i+</sub>* oraz *d<sub>i-</sub>* według poniższych wzorów pochodzących z artykułu: Kukuła, K., Luty, L. (2018) “O Wyborze Metody Porządkowania Liniowego do Oceny Gospodarki odpadami W polsce W Ujęciu Przestrzennym.” Zeszyty Naukowe SGGW w Warszawie - Problemy Rolnictwa Światowego, vol. 18, no. 2: 183–192

![435657575_1101631484292102_8527506804191328804_n](https://github.com/KDudek1104/computer-science-ranking/assets/139448704/23b47b54-43b7-4117-bd3c-2884434c0b73)



gdzie:
- *z<sub>ij</sub>* to wartość cechy j dla obiektu i po znormalizowaniu
- *m* to liczba cech dla każdego obiektu

Ostateczny wynik analizy TOPSIS to wartość *Q* dla określonego obiektu, która jest wyrażona poniższym ilorazem zaczerpniętym z tej samej pracy co wzory na odległości od wzorca i antywzorca:

![436578556_1778419016002811_9064331869705549827_n](https://github.com/KDudek1104/computer-science-ranking/assets/139448704/935e0e62-d6e4-4aa7-9a05-89f2806727fe)


gdzie:
- *d<sub>i-</sub>* to odległość obiektu *i* od antywzorca
- *d<sub>i+</sub>* to odległość obiektu *i* od wzorca


### Analiza metodą Nowak

W tej metodzie wynik jest średnią wartości po znormalizowaniu z uwzględnieniem tego, że wartości cech, które są destymulantami są ujemne.

Normalizacja danych w metodzie Nowak polega na podzieleniu wartości każdej cechy każdego obiektu przez średnią wartość danej cechy dla wszystkich obiektów.

Następne obliczenia wykonujemy zgodnie z poniższym wzorem pochodzącym z pracy: Kukuła, K., Luty, L. (2018) “O Wyborze Metody Porządkowania Liniowego do Oceny Gospodarki odpadami W polsce W Ujęciu Przestrzennym.” Zeszyty Naukowe SGGW w Warszawie - Problemy Rolnictwa Światowego, vol. 18, no. 2: 183–192


![436088115_2066226290426594_7444667718072887934_n](https://github.com/KDudek1104/computer-science-ranking/assets/139448704/8c431add-a542-41a0-b306-bcd95091ab4c)

gdzie:
- *Q* oznacza wynik końcowy
- *m* to liczba cech
- *z<sub>ij</sub>* to wartość po znormalizowaniu cechy *j* obiektu *i*.

W przypadku naszej analizy ze względu na wykorzystanie destymulant, w ich przypadku wartości należało odjąć, a przy pozostałych cechach można było bezpośrednio korzystać ze wzoru.

### Analiza metodą STRAHL

Jedną z wykorzystanych metod do analizy jest ta zaproponowana w pracy: Strahl, D. (1978), "Propozycja konstrukcji miary syntetycznej" Przegląd Statystyczny

Wykorzystane wzory zaczerpnięte z artykułu Kukuła, K., Luty, L. (2018) “O Wyborze Metody Porządkowania Liniowego do Oceny Gospodarki odpadami W polsce W Ujęciu Przestrzennym.” Zeszyty Naukowe SGGW w Warszawie - Problemy Rolnictwa Światowego, vol. 18, no. 2: 183–192:

![436552681_359291277113938_9039028363359408260_n](https://github.com/KDudek1104/computer-science-ranking/assets/139448704/b7518344-6020-4be4-9fd5-745d0646e342)

gdzie:
*x<sub>ji</sub>* - wartość *j*-tej cechy dla *i*-tego kierunku i wydziału
*z<sub>ij</sub>* - to wartość unormowana dla *j*-tej cechy dla *i*-tego kierunku i wydziału
*Q* – Ostateczny wynik analizy D. Strahl dla określonego kierunku informatycznego

Aby otrzymać wartość unormowaną, dzielimy każdą poszczególną wartość w kolumnie przez wartość
maksymalną dla tej kolumny.

Następnie, aby otrzymać ostateczny wynik dla poszczególnych kierunków, sumujemy unormowane
wartości i dzielimy przez ilość cech, które porównujemy.


### Analiza metodą SSW

Analiza została wykonana na podstawie wzorów wykorzystanych w pracy Kukuła, K., Luty, L. (2018) “O Wyborze Metody Porządkowania Liniowego do Oceny Gospodarki odpadami W polsce W Ujęciu Przestrzennym.” Zeszyty Naukowe SGGW w Warszawie - Problemy Rolnictwa Światowego, vol. 18, no. 2: 183–192

![438154441_1453719338911414_3317707286583713279_n](https://github.com/KDudek1104/computer-science-ranking/assets/139448704/a4c3fe98-637f-40d2-a1c5-9a84afbd1a97)

# Wyniki
Poniższe tabele prezentują 20 najwyżej sklasyfikowanych kierunków według kolejnych metod porządkowania liniowego:


![top20hellwig](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/4750b411-bf3e-432c-80f1-896773862589)
![top20muz](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/c905bde7-faa0-4c56-8523-caa1122db3de)
![top20topsis](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/bf01d524-d0f4-42b6-aed7-a4b37796110f)
![top20nowak](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/898591cc-603a-41c2-a763-cc2c85518ea6)
![top20ssw](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/8ed22280-5dad-416d-9ae9-ad4dc8787e45)
![top20strahl](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/ba9c7b94-e265-4d6d-9daa-f3b6bae5054c)


20 najwyżej sklasyfikowanych kierunków według średniego miejsca (RANK) zajętego we wszystkich przeprowadzonych metodach:

![image](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/9d3cea24-1689-4914-b8d4-6d2e94d37fd0)



20 najwyżej sklasyfikowanych kierunków na podstawie średniej wartości ze wszystkich cech syntetycznych Qi

![image](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/8defc0fd-3968-4e0a-a005-4fcdb2c97134)


Macierz korelacji na podstawie współczynnika korelacji Pearsona

![image](https://github.com/KDudek1104/computer-science-ranking/assets/44409389/a924646a-7332-4a79-9614-e8def9ed368e)



# Podsumowanie
Praca skupiła się na badaniu ekonomicznych losów absolwentów studiów informatycznych w Polsce. Uzyskane wyniki potwierdzają istotność wyboru programu studiów i uczelni dla przyszłych perspektyw zawodowych i zarobków absolwentów. Odniesienie do literatury wskazuje na zgodność uzyskanych wyników z wcześniejszymi badaniami w dziedzinie.
## Ocena realizacji celu

Niniejsza analiza danych stanowi istotny krok w zrozumieniu perspektyw zawodowych absolwentów kierunku informatyka na polskich uczelniach. Cel badania został w pełni zrealizowany poprzez zastosowanie metod statystycznych porządkowania obiektów do utworzenia rankingów porównujących sytuacje ekonomiczne absolwentów różnych programów studiów informatycznych. Analiza uwzględniała istotne zmienne takie jak zarobki po ukończeniu studiów, stopień bezrobocia i odsetek osób pozostających na studiach drugiego stopnia na uczelni.

Wyniki uzyskane dzięki zastosowaniu metod analizy porządkowania liniowego, takich jak metoda Hellwiga i metoda MUZ, pozwoliły na hierarchiczne uporządkowanie danych. Dzięki przeprowadzonej analizie, studenci, badacze i instytucje edukacyjne mogą lepiej zrozumieć wpływ różnych czynników, takich jak uczelnia czy specjalizacja, na karierę zawodową i zarobki absolwentów.

Jednak należy pamiętać, że dynamika rynku pracy oraz inne czynniki zewnętrzne mogą wpływać na sytuację ekonomiczną absolwentów w sposób trudny do uchwycenia jedynie na podstawie danych historycznych. Dlatego też, w celu pełniejszego zrozumienia perspektyw zawodowych absolwentów kierunku informatyka, konieczne mogą być dalsze badania i analizy, uwzględniające zmiany w otoczeniu społeczno-ekonomicznym oraz rynku pracy.

## Odniesienie do pozycji z przeglądu literatury
**Różnice**

Zauważyliśmy liczne różnice w stusunku do znalezionej pozycji z przeglądu literatury.
Różnice między analizą w rankingu "Perspektywy" a naszą analizą obejmują:
- Stopień studiów: nasza analiza skupia się na absolwentach studiów inżynierskich i licencjackich, zaś ranking "Perspektyw" na studiach magisterskich.
- Specyfikę zmiennych i wskaźników branych pod uwagę w analizie, np. "Perspektywy" uwzględniają wskaźniki takie jak prestiż uczelni, potencjał akademicki i dydaktyczny oraz umiędzynarodowienie.
  W naszym rankingu został postawiony nacisk na losy zawoodowe studentów, czyli ich zarobki (podzielone na kilka odzdzielnych zmiennych), procent bezrobocia czy chęć zostania na studiach drugiego stonia na danej uczelni. Ostatnia wymieniona zmienna nie została w ogóle ujęta w rankingu "Perspektywy".
- Metodologie obliczeniowe, tj. sposób obliczania i wagi przypisywane poszczególnym zmiennym są w pewnej części różne między naszą analizą a rankingiem "Perspektywy".
- Zakres analizy, np. "Perspektywy" skupiły się bardziej ogólnie niż my, podczas gdy nasza analiza jest bardziej szczegółowa w określonej dziedzinie- zawodowe losy absolwentów.
- "Perspektywy" mają dwa osobne rankingi dla studiów informatycznych, z czego jeden jest jedynie dla programów z tytułem "magister inżynier", a jeden jedynie dla programów z tytułem "inżynier". Utrudnia to porównanie ze sobą dwóch kierunków informatycznych z innym nadawanym tytułem, czego chcieliśmy uniknąć w naszej analizie.
Warto również zaznaczyć, że nasza analiza może być bardziej spersonalizowana, pozwalając na dostosowanie metodologii do konkretnych potrzeb i celów badawczych.

# Bibliografia
1. Kukuła, K., Luty, L. (2018) “O Wyborze Metody Porządkowania Liniowego do Oceny Gospodarki odpadami W polsce W Ujęciu Przestrzennym.” Zeszyty Naukowe SGGW w Warszawie - Problemy Rolnictwa Światowego, vol. 18, no. 2: 183–192
2. Bąk, A. (2016) “Porządkowanie Liniowe Obiektów Metodą Hellwiga I Topsis – Analiza Porównawcza / Linear Ordering of Objects Using Hellwig and Topsis Methods – a Comparative Analysis.” Prace Naukowe Uniwersytetu Ekonomicznego we Wrocławiu, no. 426: 22–31. 
3. G., R.,  Jahanshahloo, F., Hosseinzadeh Lotfi, A., R., Davoodi (2009) "Extension of TOPSIS for decision-making problems with interval data: Interval efficiency" Mathematical and Computer Modelling, Volume 49, Issues 5–6: 1137-1142
4. Ching-Lai Hwang, K., Yoon (1981) "Multiple Attribute Decision Making: Methods and Applications" Lecture Notes in Economics and Mathematical Systems vol. 186
5. Kukuła, K. (1999) "Metoda unitaryzacji zerowanej na tle wybranych metod normowania cech diagnostycznych" Acta Scientifica Academiae Ostroviensis nr 4, 5-31
6. Strahl, D. (1978), "Propozycja konstrukcji miary syntetycznej" Przegląd Statystyczny
